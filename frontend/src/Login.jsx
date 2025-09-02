import React, { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import { useNavigate, Link } from "react-router-dom";

const Login = () => {
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault(); // Prevent page reload on form submit

    const formData = new FormData(); // Create a FormData object
    formData.append("username", username);
    formData.append("password", password);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/signin",
        formData
      ); // Send data to the backend
      localStorage.setItem("jwt", response.data.token);
      toast.success("Login successful");
      navigate("/home");
      // Perform further actions on successful login, like redirecting to another page
    } catch (error) {
      console.error("Login error:", error);
      toast.error(error.response.data.message);
    }
  };

  return (
    <div className="container-1">
      <div className="login-container">
        {" "}
        {/* Center the card */}
        <h2 style={{ textAlign: "center" }}>Login</h2>
        <form onSubmit={handleSubmit} className="login-form">
          {" "}
          {/* Center form elements */}
          <div className="form-group">
            <label>Username:</label>
            <input
              type="text"
              value={username}
              onChange={(e) => setUsername(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Password:</label>
            <input
              type="password"
              value={password}
              onChange={(e) => setPassword(e.target.value)}
              required
            />
          </div>
          <button type="submit" className="submit-button">
            Login
          </button>
          <div>
            Don't have an account?{" "}
            <Link to="/signup" className="signup-link">
              Signup
            </Link>{" "}
            {/* Link to sign-up page */}
          </div>
        </form>
      </div>
    </div>
  );
};

export default Login;
