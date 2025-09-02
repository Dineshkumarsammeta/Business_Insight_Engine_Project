import React from "react";
import { Link, useNavigate } from "react-router-dom";

const Navbar = () => {
  const navigate = useNavigate();

  const logout = () => {
    localStorage.removeItem("jwt"); // Remove JWT from localStorage
    navigate("/"); // Redirect to login page
  };

  return (
    <nav className="navbar">
      {" "}
      {/* Navbar container */}
      <div className="navbar-links">
        {" "}
        {/* Link container */}
        <Link to="/history" className="navbar-link">
          History
        </Link>{" "}
        {/* History link */}
        <button onClick={logout} className="navbar-link1">
          Logout
        </button>{" "}
        {/* Logout button */}
      </div>
    </nav>
  );
};

export default Navbar;
