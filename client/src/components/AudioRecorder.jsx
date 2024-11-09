import React, { useState, useRef } from "react";

const AudioRecorder = () => {
  const [recording, setRecording] = useState(false); // Track if recording is in progress
  const [recordings, setRecordings] = useState([]); // Store each recording as an array of Blob URLs
  const [mediaRecorder, setMediaRecorder] = useState(null); // Store the MediaRecorder instance
  const audioChunks = useRef([]); // Ref to store audio data chunks

  // Function to start recording
  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true }); // Request microphone access
    const recorder = new MediaRecorder(stream); // Initialize MediaRecorder with audio stream

    recorder.ondataavailable = (event) => {
      audioChunks.current.push(event.data); // Push each chunk to audioChunks array
    };

    recorder.onstop = () => {
      const audioBlob = new Blob(audioChunks.current, { type: "audio/wav" }); // Create Blob from chunks
      const audioURL = URL.createObjectURL(audioBlob); // Generate a playback URL for the recording
      setRecordings((prevRecordings) => [...prevRecordings, audioURL]); // Add the new recording URL to recordings array
      audioChunks.current = []; // Reset chunks for next recording
    };

    recorder.start(); // Start recording
    setMediaRecorder(recorder); // Save MediaRecorder instance in state
    setRecording(true); // Set recording state to true
  };

  // Function to stop recording
  const stopRecording = () => {
    mediaRecorder.stop(); // Stop the MediaRecorder, triggering onstop
    setRecording(false); // Set recording state to false
  };

  // Function to delete a recording by its index
  const deleteRecording = (index) => {
    setRecordings(
      (prevRecordings) => prevRecordings.filter((_, i) => i !== index) // Filter out the recording at the specified index
    );
  };

  // Function to handle file upload
  const handleFileUpload = (event) => {
    const file = event.target.files[0]; // Get the first file from the file input

    if (file && (file.type === "audio/mp3" || file.type === "audio/wav")) {
      const audioURL = URL.createObjectURL(file); // Generate an object URL for the uploaded file
      setRecordings((prevRecordings) => [...prevRecordings, audioURL]); // Add the file URL to recordings
    } else {
      alert("Please upload a valid MP3 or WAV file");
    }
  };

  return (
    <div>
      <h3>Audio Recorder</h3>

      {/* Start or Stop button depending on recording state */}
      {recording ? (
        <button onClick={stopRecording}>Stop Recording</button>
      ) : (
        <button onClick={startRecording}>Start Recording</button>
      )}

      {/* File upload input for uploading MP3 or WAV files */}
      <div style={{ marginTop: "20px" }}>
        <input
          type="file"
          accept="audio/mp3, audio/wav"
          onChange={handleFileUpload}
          style={{ marginBottom: "20px" }}
        />
      </div>

      {/* Display each recorded audio file with playback controls and a delete button */}
      <div
        style={{
          display: "flex",
          flexDirection: "column", // Stack recordings vertically
          gap: "10px",
          marginTop: "20px",
        }}>
        {recordings.map((recordingURL, index) => (
          <div
            key={index}
            style={{
              display: "flex", // Flexbox row for audio player, name, and delete button
              alignItems: "center", // Vertically align items in the center
              border: "1px solid #ccc",
              padding: "10px",
              borderRadius: "5px",
              width: "100%", // Full width for each recording item
              justifyContent: "space-between", // Space out elements on one line
            }}>
            {/* Audio player */}
            <audio
              controls
              src={recordingURL}
              style={{ flexGrow: 1, marginRight: "10px" }}></audio>

            {/* Audio name */}
            <p style={{ marginRight: "10px", flexShrink: 0 }}>
              Recording {index + 1}
            </p>

            {/* Delete button */}
            <button
              onClick={() => deleteRecording(index)}
              style={{
                background: "red",
                color: "white",
                border: "none",
                padding: "5px",
                borderRadius: "3px",
                cursor: "pointer",
              }}>
              Delete
            </button>
          </div>
        ))}
      </div>
    </div>
  );
};

export default AudioRecorder;
