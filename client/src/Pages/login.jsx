import AnchorButton from "../components/AnchorButton.jsx";
import img1 from "../assets/login-img.jpg"
import "./login.css"
import google from "../assets/search.png"
export default function Login(){
    return <div className="login-body">
      {/* <h1>Hack Trent 24</h1> */}
      <div className="login-sections">
      <section className="login-sec1">
        <h1>Welcome To Vocalytics!</h1>
        <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Reiciendis ipsam laborum consequuntur illo atque illum vel? Et sit odio quas!</p>
      <div className="buttons">
      <section className="google">
                <div>
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