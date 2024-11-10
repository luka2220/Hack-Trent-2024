import Recording from "../../recording";
import "./home.css"
import Nav from "../../components/nav";
function Home() {
  return (
    <div className="home-body">
      <Nav/>
      <Recording/>
    </div>
  );
}

export default Home;
