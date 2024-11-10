import { useState } from "react";
import "./recording.css";
import AudioRecorder from "./components/AudioRecorder";

export default function Recording() {
  const [recordings, setRecordings] = useState([]);
  const [recording, setRecording] = useState(false);
  const [analysis,setAnalysis]=useState(null);

  const deleteRecording = (index) => {
    setRecordings((prevRecordings) => prevRecordings.filter((_, i) => i !== index));
  };

  function handleAnalysis(){
    const responsedata=localStorage.getItem("response")
    if(responsedata){
      var data=JSON.parse(responsedata)
      console.log(data);
      setAnalysis(data)
    }
  }

  function handleClearAnalysis() {
    setAnalysis(null); 
  }

  return (
    <div className="recording-body">
      <section className="section-1 section">
        <div>
          <button className="analysis-btn" onClick={handleAnalysis}>Analyze audio</button>
        </div>
        <div>
          <div style={{ display: "flex", flexDirection: "column", gap: "10px", marginTop: "20px" }}>
            {recordings.map((recording, index) => (
              <div
                key={index}
                style={{
                  display: "flex",
                  alignItems: "center",
                  border: "1px solid #ccc",
                  padding: "10px",
                  borderRadius: "5px",
                  width: "90%",
                  justifyContent: "space-between",
                  alignSelf: "center"

                }}
              >
                {/* Audio player */}
                <audio controls src={recording.url} style={{ flexGrow: 0.8, marginRight: "10px", width: "5px" }}></audio>

                {/* Audio name */}
                <p style={{ marginRight: "10px", flexShrink: 0 }}>{recording.name}</p>

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
                  }}
                >
                  Delete
                </button>
              </div>
            ))}
          </div>
        </div>
      </section>

      <section className="section-2 section">
        <div className={`profile ${recording ? "wave" : ""}`}></div> {/* Conditionally add "recording" class */}

        <section className="recording-action">
          <AudioRecorder
            recordings={recordings}
            setRecordings={setRecordings}
            recording={recording} // Pass down the recording state
            setRecording={setRecording} // Pass down the setRecording function
          />
        </section>
      </section>

      <section className="section section-3">
        <h4>SPEECH ANALYSIS</h4>
        {analysis &&   <h3>
    Speech:-{" "}
    {analysis.words.map((word, index) => (
      <span
        key={index}
        style={{
          color: analysis.incorrect.includes(index) ? "red" : "black", // red for incorrect words
        }}
      >
        {word}{" "}
      </span>
    ))}
  </h3>}
  <div className="error-container">
  {!setAnalysis && <h2>ERRORS:-</h2>}
  {analysis && ( 
          <h2>{" "}  
            {analysis.incorrect.map((index ,i) => <li key={i} className="error-list">{analysis.words[index]}</li>)} 
            </h2>
)} 
  </div>

  <button className="analysis-btn" onClick={handleClearAnalysis}>Clear Analysis</button>

       </section>
    </div>
  );
}
