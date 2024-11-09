import { useState } from "react";
import "../recording.css"
import uplaodicon from "../assets/upload.png"

export default function FileUpload(){

    const [fileName, setFileName] = useState('');


    const handleFileChange = (event) => {
      const selectedFile = event.target.files[0];
      if (selectedFile) {
        setFileName(selectedFile.name); 
      }
    };

    return <div>
        <div className="file-upload-container">
        <input type="file" id="file-input" onChange={handleFileChange} style={{ display: 'none' }} />

        <label htmlFor="file-input" className="upload-icon">
          <img src={uplaodicon} alt="Upload Icon" className="icon"/>
        </label>

        {fileName && <p>Selected file: {fileName}</p>}
        </div>
    </div>
}