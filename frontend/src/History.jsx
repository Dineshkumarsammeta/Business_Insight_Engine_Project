import axios from "axios";
import React, { useEffect, useState } from "react";
import { toast } from "react-toastify";
import { CircularProgress } from "@mui/material";
import { useNavigate } from "react-router-dom";

function History() {
  const [data, setData] = useState([]);
  const token = localStorage.getItem("jwt");
  const navigate = useNavigate();
  const [loader, setLoader] = useState(true);

  const fetchHistory = async () => {
    try {
      const res = await axios.get("http://127.0.0.1:5000/fetch_searches", {
        headers: {
          Authorization: token,
        },
      });
      setData(res.data.searches);
      setLoader(false);
    } catch (error) {
      setLoader(false);
      toast.error(error.response?.data?.message || "Failed to fetch history");
      if (error.response?.status === 401) {
        navigate("/");
        toast.error("Please login again");
      }
    }
  };

  useEffect(() => {
    fetchHistory();
  }, []);

  // Function to format the timestamp to date only
  const formatDate = (timestamp) => {
    const date = new Date(timestamp);
    return date.toLocaleDateString();
  };

  return (
    <>
      {loader ? (
        <div
          style={{
            display: "flex",
            justifyContent: "center",
            alignItems: "center",
            height: "100vh",
          }}
        >
          <CircularProgress />
        </div>
      ) : (
        <div className="history-container">
          {data?.length === 0 && (
            <div
              style={{
                display: "flex",
                justifyContent: "center",
                alignItems: "center",
                height: "90vh",
              }}
            >
              <p style={{ color: "#fff" }}>No Searches Found</p>
            </div>
          )}
          {data.map((item, index) => (
            <div key={index} className="history-card">
              <div className="history-query-container ">
                {" "}
                {/* Scrollable section */}
                <h3 className="history-query scrollable-cell">
                  Query: {item.query}
                </h3>
              </div>
              <p className="history-timestamp">
                Date: {formatDate(item.timestamp)}
              </p>
              <p className=" history-sentiment scrollable-cell">
                Sentiment: {item.result.Sentiment}
              </p>
              <div className="history-query-container ">
                <p className=" history-reason">{item.result.LLM_REASON}</p>
              </div>{" "}
            </div>
          ))}
        </div>
      )}
    </>
  );
}

export default History;
