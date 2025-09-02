import React, { useState } from "react";
import axios from "axios";
import { toast } from "react-toastify";
import { Link, useNavigate } from "react-router-dom";

const Signup = () => {
  const [email, setEmail] = useState("");
  const [name, setName] = useState("");
  const [password, setPassword] = useState("");
  const navigate = useNavigate();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const minPasswordLength = 8;
    if (password.length < minPasswordLength) {
      toast.error(
        `Password must be at least ${minPasswordLength} characters long.`
      );
      return; // Exit early without submitting
    }
    const formData = new FormData(); // Create a FormData object
    formData.append("email", email);
    formData.append("username", name);
    formData.append("password", password);
    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/signup",
        formData
      );
      console.log("Signup successful:", response.data);
      toast.success("Signup successful");
      navigate("/");
    } catch (error) {
      console.error("Signup error:", error);
      toast.error(error.response.data.message);
    }
  };

  return (
    <div className="container-1">
      <div className="signup-container">
        <h2 style={{ textAlign: "center" }}>Signup</h2>
        <form onSubmit={handleSubmit} className="signup-form">
          <div className="form-group">
            <label>Email:</label>
            <input
              type="email"
              value={email}
              onChange={(e) => setEmail(e.target.value)}
              required
            />
          </div>
          <div className="form-group">
            <label>Name:</label>
            <input
              type="text"
              value={name}
              onChange={(e) => setName(e.target.value)}
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
            Signup
          </button>
          <span>
            Already have an account <Link to="/">Login</Link>
          </span>
        </form>
      </div>
    </div>
  );
};

export default Signup;
