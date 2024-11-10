import { useState } from "react"
import dropdownimg from "../assets/dropdown.png"
import avatar from "../assets/user.png"
import "./nav.css"
export default function Nav(){
    const [dropdown,setDropdown]=useState(false)

    function handleDropdown(){
       setDropdown(!dropdown)
    }
//     const [userData, setUserData] = useState(null);
//   const [error, setError] = useState(null);

//   useEffect(() => {
//     // Make the API call to get user data
//     fetch('http://127.0.0.1:8001/api/user/current', {
//       method: 'GET',
//       headers: {
//         'Content-Type': 'application/json',
//         'Authorization': 'Bearer your-auth-token'
//       }
//     })
//       .then(response => {
//         if (!response.ok) {
//           throw new Error('Network response was not ok');
//         }
//         return response.json();
//       })
//       .then(data => {
//         setUserData(data);
//       })
//       .catch(error => {
//         setError(error.message);
//       });
//   }, []);

//   if (error) return <div>Error: {error}</div>;
//   if (!userData) return <div>Loading...</div>;

    return <div className="nav-body">
        <h1>Vocalytics</h1>
        <div className="nav-action">
            <div className="nav-dropdown">
            <h2>Welcome <img src={avatar} alt="" className="avatar-img"/></h2>
            <img src={dropdownimg} alt="" onClick={handleDropdown} className="dropdown-img"/>
            </div>
            {dropdown && <h4>Logout</h4>}
        </div>
    </div>
}