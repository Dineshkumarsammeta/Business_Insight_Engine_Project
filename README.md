
# Full-Stack Real-Time Sentiment Analysis Pipeline

A scalable, end-to-end system that combines **real-time data ingestion, deep learning, and LLM-based reasoning** to monitor customer sentiment at scale with high data reliability.

## 📌 Overview
This project ingests live Twitter data streams, processes them through an  Airflow ETL pipeline, applies advanced machine learning models (LSTM, CNN, hybrid LSTM-CNN), and integrates **GPT-4 via LangChain** for contextual reasoning and justifications. Results are visualized in a **responsive React UI** powered by a **Flask API**, enabling real-time predictions, anomaly detection, and trend monitoring.

## 🛠 Tech Stack
- **Data Engineering:** Python, Apache Spark, Apache Airflow  
- **Cloud & Storage:** AWS S3, Redshift, Glue, Lambda, Kinesis, boto3 SDK  
- **Machine Learning:** TensorFlow, Scikit-learn, GPT-4 (LangChain), zero/one/few-shot learning  
- **Frontend:** React, HTML, CSS  
- **Backend/API:** Flask (REST API)  
- **DevOps & Tools:** GitHub, Azure DevOps, Agile methodology

## 🚀 Features
- **Real-Time Data Ingestion** from Twitter API  
- **Hybrid Deep Learning Models** (LSTM, CNN, hybrid LSTM-CNN)  
- **LLM Integration** (GPT-4 via LangChain) for contextual reasoning  
- **Data Validation & Schema Checks** during ingestion  
- **Anomaly Detection** for unusual sentiment spikes  
- **Responsive UI** with real-time sentiment visualization  
- **Automated Monitoring** via Airflow alerts  
- **Cost-Optimized Cloud Deployment** on AWS

## 📂 Architecture
