import React, { useEffect, useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";
import Navbar from "./Navbar";

function Home() {
  const navigate = useNavigate();
  const [inputText, setInputText] = useState("");
  const [prediction, setPrediction] = useState("");
  const [file, setFile] = useState(null);
  const [data, setData] = useState([]);
  let token = localStorage.getItem("jwt");

  const handleFileChange = (event) => {
    setFile(event.target.files[0]);
  };

  const handleSubmit = async (event) => {
    event.preventDefault();

    if (!file) {
      alert("Please select a file");
      return;
    }

    const formData = new FormData();
    formData.append("csvfile", file);

    try {
      const response = await axios.post(
        "http://127.0.0.1:5000/upload",
        formData,
        {
          headers: {
            "Content-Type": "multipart/form-data",
            Authorization: token,
          },
        }
      );

      setData(response.data.csv_content);
    } catch (error) {
      console.error("Error uploading file:", error);
      if (error.response.status === 401) {
        navigate("/");
        toast.error("Please Login again");
      } else {
        toast.error(error.response.data.message);
      }
    }
  };

  console.log(data);

  useEffect(() => {
    if (!localStorage.getItem("jwt")) {
      navigate("/");
    }
  }, []);

  const handlePredict = async () => {
    if (!inputText) {
      toast.error("Please enter some text for prediction.");
      return;
    }

    try {
      const formData = new FormData(); // Create a FormData object
      formData.append("query", inputText);
      const response = await axios.post(
        "http://127.0.0.1:5000/predict",

        formData,
        {
          headers: {
            Authorization: token,
          },
        }
      );
      toast.success("Query stored successfully");
      console.log(response.data);
      setPrediction(response.data); // Assuming the API returns a "prediction" field
    } catch (error) {
      console.error("Prediction error:", error);
      toast.error(error.response.data.message);
      if (error.status === 401) {
        navigate("/");
        toast.error("Please Login again");
      }
    }
  };

  return (
    <div>
      <Navbar />
      <div className="home-container">
        <h2>Text Prediction</h2>
        <textarea
          value={inputText}
          onChange={(e) => setInputText(e.target.value)}
          rows={5}
          cols={2}
          placeholder="Enter your text here..."
          className="input-textarea"
        />
        <button onClick={handlePredict} className="predict-button">
          Predict
        </button>
        {prediction && (
          <div className="prediction-result">
            <h3>Prediction Result:</h3>
            <p>{prediction.Sentiment}</p>
            <p>{prediction.LLM_REASON}</p>
          </div>
        )}
      </div>

      <div className="container">
        <h2 style={{ color: "#fff" }}>Upload CSV File</h2>
        <form onSubmit={handleSubmit} className="form">
          <input type="file" onChange={handleFileChange} className="input" />
          <button type="submit" className="submit-button">
            Upload
          </button>
        </form>

        {data?.length > 0 && (
          <table
            border="1"
            cellPadding="10"
            style={{ width: "100%", textAlign: "left",marginTop:"5px" }}
          >
            <thead>
              <tr>
                {Object.keys(data[0]).map((key) => (
                  <th key={key}>{key}</th>
                ))}
              </tr>
            </thead>
            <tbody>
              {data.map((item, index) => (
                <tr key={index}>
                  {Object.values(item).map((value, idx) => (
                    <td key={idx} className="scrollable-cell">
                      <div className="scrollable-content">{value}</div>
                    </td>
                  ))}
                </tr>
              ))}
            </tbody>
          </table>
        )}
      </div>
    </div>
  );
}
export default Home;
