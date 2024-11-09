import "./recording.css"
import recordicon from "../src/assets/record.png"
import FileUpload from "./components/fileUpload"
export default function Recording(){

    return <div className="recording-body">

        <section className="section-1 section">
            <div>
            <button className="analysis-btn">Analyze audio</button>
            </div>
        </section>


        <section className="section-2 section">
        <div className="profile"></div>

        <section className="recording-action">
            <FileUpload/>
            <img src={recordicon} alt=""  className="icon"/>
        </section>
        
        </section>

        <section className="section section-3">
            <h4>Here are the words
            you missed</h4>
        </section>
    </div>
}