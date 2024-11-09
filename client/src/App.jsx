import "./App.css";
import AnchorButton from "./components/AnchorButton";
function App() {
  //render title, learn button and sign in button

  return (
    <>
      <h1>Hack Trent 24</h1>
      <div className="buttons">
        <AnchorButton
          reference=""
          text="Learn more"
        />
        <AnchorButton
          reference="Home"
          text="login"
        />
      </div>
    </>
  );
}

export default App;
