import AnchorButton from "../components/AnchorButton.jsx";
import { useEffect } from "react";
import img1 from "../assets/login-img.jpg"
import "./login.css"
import google from "../assets/search.png"
export default function Login(){

  useEffect(() => {
    // Check if the user is already authenticated by checking session or token
    const user = sessionStorage.getItem("user_id"); // Or use localStorage or any session management method
    if (user) {
      window.location.href = "/home"; // Redirect to home page if already authenticated
    }
  }, []);

  function googlesignin(){
    window.location.href = "http://localhost:8001/login";
}



    return <div className="login-body">
      {/* <h1>Hack Trent 24</h1> */}
      <div className="login-sections">
      <section className="login-sec1">
        <h1>Welcome To Vocalytics!</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis ipsam laborum consequuntur illo atque illum vel? Et sit odio quas!</p>
      <div className="buttons">
      <section className="google">
                <div onClick={googlesignin}>
                    <img src={google} alt="" />
                    <button>Sign in with Google</button>
                </div>
            </section>
        <AnchorButton
          reference="Home"
          text="login"
        />
      </div>
      </section>

      <section className="login-sec2">
        <img src={img1} alt="" />
      </section>
      </div>
    </div>
}