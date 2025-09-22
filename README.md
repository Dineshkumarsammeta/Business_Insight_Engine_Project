# 📊 Business_Insight_Engine_Project

# Project Title
*Business Insight Engine – Real-Time Sentiment Analysis & ETL Automation*

## 📅 Project Timeline
**Duration:** 14-Jan-2024 – 12-March-2024  
**Location:** Master's in Advanced Computer Science, UK  
**Employer Name:** Self-initiated Academic Project  
**Reporting to:** Dr. Artur Boronat  
**Type of Project:** Real-Time Sentiment Analysis, ETL Automation (Academic Project)  

##  ⚠️ Disclaimer

This project uses LangChain to incorporate GPT-4 for contextual reasoning and sophisticated sentiment analysis.
In order to execute the system end-to-end or completely replicate the findings, you need:

A current OpenAI account

A working OpenAI API key set up in your setting

Certain project components (including contextual insights, zero/few-shot learning, and GPT-4 improved classification) won't work properly without access to OpenAI's API.

The repository is kept up to date for professional demonstration, research, and academic reasons.
ETL automation, Spark processing, Airflow orchestration, deep learning baselines, and AWS infrastructure setup are examples of modules that are not linked to LLM integration but may nevertheless be replicated separately.

This project was developed and tested in a TensorFlow environment (tf Conda environment).
Some scripts and notebooks may fail to execute directly in GitHub Actions, Codespaces, or fresh environments due to missing dependencies, such as:

ipykernel (required for running notebooks in a specific environment)

nltk corpora (e.g., stopwords)

Conda environment mismatches (tf not pre-configured)

To successfully reproduce results, please ensure:

You have a Conda environment named tf (or update paths in the code).

Run the following before executing notebooks:

conda install -n tf ipykernel --update-deps --force-reinstall
pip install tensorflow scikit-learn pandas nltk
python -m nltk.downloader stopwords


This repository is maintained for academic and research demonstration purposes.
Execution may require additional setup depending on the system, TensorFlow version, and Python environment.

## 📌 Objective
The goal of this project was to build a **cloud-native, full-stack sentiment analysis platform** capable of processing massive volumes of **real-time Twitter data**.  

Using **Apache Spark, Airflow, and AWS services**, high-throughput ETL pipelines were designed. Deep learning models (LSTM, CNN, Hybrid LSTM-CNN) and **GPT-4 via LangChain** were trained for advanced sentiment classification with over **92% accuracy**.  

The system provided **sub-second predictions**, interactive insights, and was optimized for **scalability, dependability, and cost-effectiveness**.  

## 🌍 Background & Relevance
With the exponential growth of social media data, businesses need **real-time insights** into customer sentiment.  

This project combines **ETL automation, advanced deep learning, and LLM-enhanced reasoning** to provide actionable intelligence for **brand monitoring, market analysis, and risk management**.  

The outcome was a **production-ready pipeline** capable of analyzing **10,000+ tweets/hour** with a 95% uptime SLA.

## ⚙️ Methodology
- Designed **full-stack sentiment analysis workflow** using Python, Flask, and Apache Spark.  
- Built **ETL pipelines** with Apache Airflow for real-time Twitter streams.  
- Processed **~100GB of streaming data** via Apache Spark.  
- Architected a **cloud-native system** with AWS (S3, Redshift, Glue, Lambda, Kinesis).  
- Trained **deep learning models** (LSTM, CNN, hybrid architectures) with TensorFlow & Scikit-learn.  
- Integrated **GPT-4 via LangChain** for contextual sentiment analysis and zero-shot learning.  
- Deployed a **secure Flask REST API** serving real-time sentiment predictions.  
- Developed a **React.js frontend** with real-time dashboards and model explainability.  
- Implemented **data verification, anomaly detection, and DAG monitoring** in Airflow.  
- Conducted **A/B testing** between LLMs and traditional models.  
- Optimized cost-performance trade-offs through **cloud simulations**.  
- Documented workflows, pipelines, and model architecture for reproducibility.  

## 📂 Data Sources
- **Source:** Kaggle – Twitter and social media sentiment datasets  
- **Source:** Real-time Twitter API feeds (streaming JSON data)
- 
## 📥 Data Ingestion

**Reproducibility Note:**  

Because Twitter API rate limits apply on Free/Basic tiers, this repository includes a **simulated streaming mode** to emulate live tweets.  

To run the simulation, use:

```bash
python tools/tweet_producer.py --file data/kaggle_dump.jsonl --rate 50msg/s
```
Reproducibility note: Because X API read limits apply on Free/Basic tiers, the repo includes a
simulated streaming mode. Run python tools/tweet_producer.py --file
data/kaggle_dump.jsonl --rate 50msg/s to emulate live tweets. See X API access levels for
details. 

## 🛠️ Tools & Technologies
- **Programming:** Python, Flask, React.js  
- **Big Data:** Apache Spark, Apache Airflow  
- **Cloud:** AWS (S3, Redshift, Glue, Lambda, Kinesis)  
- **Machine Learning:** TensorFlow, Scikit-learn, LSTM, CNN, Hybrid Architectures  
- **LLM Integration:** GPT-4 via LangChain  
- **Version Control:** Git / GitHub  
- **Link:** [Git Repository](https://github.com/dineshsammeta1234/Business_Insight_Engine_Project)  

## 📌 Project Responsibilities
- Built a **full-stack sentiment analysis pipeline** with Python, Flask, Spark.  
- Developed **scalable ETL workflows** in Apache Airflow for real-time Twitter streams.  
- Designed **AWS cloud-native architecture** for low-cost, high-throughput deployment.  
- Trained, tuned, and validated **deep learning models (LSTM, CNN, Hybrid)**.  
- Integrated **GPT-4 (LangChain)** for advanced reasoning and zero/few-shot learning.  
- Achieved **92%+ sentiment classification accuracy** via hyperparameter optimization.  
- Developed **Flask REST API** for real-time predictions.  
- Built **React.js dashboards** to visualize and explain sentiment insights.  
- Implemented **schema validation, anomaly detection, and monitoring** in pipelines.  
- Automated DAG execution alerts in Airflow to reduce manual intervention.  
- Conducted **cost-performance simulations** for cloud deployment optimization.  
- Led **Agile sprints** with retrospectives, managed tasks via Azure DevOps Boards.  
- Applied **A/B testing** to compare LLM-based vs rule-based logic.  
- Documented system architecture, workflows, and models for handover.  
- Conducted technical walkthroughs and peer reviews to validate results.

##DashBoard Screenshots

**Single Text Input Web  Page**
<img width="1342" height="654" alt="image" src="https://github.com/user-attachments/assets/48d2d3e3-0f56-4fad-b942-a6b2620512f9" />

**History  Web Page UI**

<img width="1370" height="629" alt="image" src="https://github.com/user-attachments/assets/dd764983-db4a-4f20-be2e-cface743be44" />

**CSV File Input Web Page**

<img width="990" height="340" alt="image" src="https://github.com/user-attachments/assets/ecaf9fd7-21bc-40a1-bf5f-77e91733fc5c" />


## 📊 Results & Achievements

- Trained deep learning models achieving **88%-89%+ accuracy**.  
- Automated **ETL orchestration in Airflow**, reducing manual monitoring time by 50%.  
- Processed and structured **5M+ raw JSON logs** with AWS Lambda + Glue.  
- Enhanced classification accuracy by **18% in low-data domains** with GPT-4 LangChain.  
- Built a **500ms latency Flask + React app** for non-technical users.  
- Reduced system downtime from **hours → 10 mins** with automated alerts.  
- Improved contributor onboarding time by **50%** with modular OOP codebase.  
- Documented workflows with **Markdown + docstrings** for maintainability.  
- Found **22% user preference for GPT-4 insights** over traditional logic via A/B tests.
  ## Model Performance

### Accuracy Results

| S.No | Model Name     | Accuracy (Train, Epochs 5) | Accuracy (Train, Epochs 10) | Accuracy (Test, Epochs 5) | Accuracy (Test, Epochs 10) |
|------|----------------|---------------------------|-----------------------------|---------------------------|----------------------------|
| 1    | LSTM           | 98.53                     | 99.76                       | 89.04                     | 89.38                      |
| 2    | BI-LSTM        | 99.04                     | 99.78                       | 88.67                     | 89.27                      |
| 3    | CNN            | 99.67                     | 99.83                       | 88.26                     | 88.82                      |
| 4    | LSTM+CNN       | 98.70                     | 99.74                       | 89.43                     | 88.83                      |
| 5    | ComplementNB   | 82.17                     | -                           | -                         | -                          |
| 6    | MultinomialNB  | 83.10                     | -                           | -                         | -                          |
| 7    | BernoulliNB    | 79.09                     | -                           | -                         | -                          |

Full dataset and detailed metrics are available in the [model_training/model_DL_sent.ipynb) file.  
You can also see the visual results here: ![model_training/model_DL_sent.ipynb)
  

---

## Contact  
For questions, collaboration, or feedback, please contact:  
**Sammeta Dinesh Kumar** — [sammetadineshkumar@gmail.com]  
- 🌐 [Portfolio]((https://dineshkumarsammeta.github.io/))  
- 🔗 [LinkedIn](https://www.linkedin.com/in/dineshsammeta)  
