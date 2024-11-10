// Recording.js
import { useState } from "react";
import "./recording.css";
import AudioRecorder from "./components/AudioRecorder";

export default function Recording() {
  const [recordings, setRecordings] = useState([]);

  const deleteRecording = (index) => {
    setRecordings((prevRecordings) => prevRecordings.filter((_, i) => i !== index));
  };

  return (
    <div className="recording-body">
      <section className="section-1 section">
        <div>
          <button className="analysis-btn">Analyze audio</button>
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
        <div className="profile"></div>

        <section className="recording-action">
          <AudioRecorder recordings={recordings} setRecordings={setRecordings} />
        </section>
      </section>

      <section className="section section-3">
        <h4>Here are the words you missed</h4>
      </section>
    </div>
  );
}
