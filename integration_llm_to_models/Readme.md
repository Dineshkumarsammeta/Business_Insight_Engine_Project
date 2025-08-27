script provides:

✅ Sentiment classification (Positive / Negative)

✅ Explanation (Reason) in plain text or JSON

⚙️ Setup

Install dependencies

pip install openai langchain


Set your OpenAI API key
Inside the script:

OPENAI_API_KEY = "your_api_key_here"


Or as an environment variable:

export OPENAI_API_KEY="your_api_key_here"


Run the script

python sentiment_script.py

🧾 Example Output

Input Review:

"I have bought several of the Vitality canned dog food products and have found them all to be of good quality."


Output (Example 1 – Reason JSON):

{"Reason": "The review highlights good quality, better smell, and that the pet prefers it."}


Output (Example 2 – Sentiment + Reason):

Sentiment: Positive  
Reason: The reviewer praises the quality, smell, and their pet’s satisfaction.

📚 Libraries Used

LangChain – Prompt templating & LLM chain

OpenAI – GPT model for classification

📌 Notes

This script is for demonstration and works with small text inputs.

You can swap the review text to test different samples.

Extendable to larger datasets for automated sentiment analysis.
