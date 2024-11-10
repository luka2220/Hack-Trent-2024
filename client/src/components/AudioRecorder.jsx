import { useState, useRef } from "react";
import uploadicon from "../assets/upload.png";
import stop from "../assets/stop-button.png";
import record from "../assets/microphone.png";
import "./AudioRecorder.css";

const AudioRecorder = ({ recordings, setRecordings, recording, setRecording }) => { 
  const [mediaRecorder, setMediaRecorder] = useState(null);
  const audioChunks = useRef([]);

  const uploadAudio = async (audioBlob) => {
    try {
      const formData = new FormData();
      formData.append("file", audioBlob, "recording.wav");

      const response = await fetch("http://127.0.0.1:8001/api/upload/audio", {
        method: "POST",
        body: formData,
      });

      if (response.ok) {
        console.log(response);
      } else {
        console.log("Failed to upload audio.");
      }
    } catch (error) {
      console.error("Error uploading audio:", error);
    }
  };

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    const recorder = new MediaRecorder(stream);

    recorder.ondataavailable = (event) => {
      audioChunks.current.push(event.data);
    };

    recorder.onstop = () => {
      const audioBlob = new Blob(audioChunks.current, { type: "audio/wav" });
      const audioURL = URL.createObjectURL(audioBlob);
      const recordingName = `Recording ${recordings.length + 1}`;
      setRecordings((prevRecordings) => [
        ...prevRecordings,
        { url: audioURL, name: recordingName },
      ]);
      audioChunks.current = [];
    };

    recorder.start();
    setMediaRecorder(recorder);
    setRecording(true);  
  };

  const stopRecording = () => {
    mediaRecorder.stop();
    setRecording(false); 

    const audioBlob = new Blob(audioChunks.current, { type: "audio/wav" });

    uploadAudio(audioBlob);
  };

  const handleFileUpload = (event) => {
    const file = event.target.files[0];
    if (file) {
      const MAX_NAME_LENGTH = 10;
      const fileExtension = file.name.split('.').pop();
      const shortFileName = file.name.length > MAX_NAME_LENGTH
        ? file.name.substring(0, MAX_NAME_LENGTH) + '...' + fileExtension
        : file.name;
      const audioURL = URL.createObjectURL(file);
      setRecordings((prevRecordings) => [
        ...prevRecordings,
        { url: audioURL, name: shortFileName },
      ]);
    } else {
      alert("Please upload a valid MP3 or WAV file");
    }
  };

  return (
    <div className="record-actions">
      {recording ? (
        <button onClick={stopRecording}>
          <img src={stop} alt="Stop" />
        </button>
      ) : (
        <button onClick={startRecording}>
          <img src={record} alt="Record" />
        </button>
      )}

      <div style={{ marginTop: "0px" }}>
        <label htmlFor="file-upload">
          <img src={uploadicon} alt="Upload Icon" className="icon" />
        </label>
        <input
          id="file-upload"
          type="file"
          accept="audio/mp3, audio/wav"
          onChange={handleFileUpload}
          style={{ display: "none" }}
        />
      </div>
    </div>
  );
};

export default AudioRecorder;
