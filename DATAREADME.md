Amazon Fine Food Reviews Dataset
📚 Source

Dataset: Amazon Fine Food Reviews (also known as SNAP Amazon Fine Foods)

Available on Kaggle: snap/amazon-fine-food-reviews

Also hosted by Stanford’s SNAP group. 
Kaggle
+1

🔍 Description & Statistics
Property	Details
Number of reviews	~568,454 reviews 
SNAP

Number of users	~256,059 users 
SNAP

Number of products	~74,258 products 
SNAP

Timespan	From October 1999 to October 2012 
SNAP

Median words per review	≈ 56 words 
SNAP
🔣 Format / Columns

Each record in the dataset has the following fields:

productId: ASIN / product identifier

userId: identifier for the user who wrote the review

profileName: user’s display name

helpfulness: fraction “helpful votes / total votes”

score: rating (1.0 to 5.0)

time: UNIX timestamp of review 
SNAP

summary: short summary / title of the review

text: full review text 
SNAP

⚙ Usage in Our Project

We used the dataset to train / validate sentiment classification models (positive vs negative).

Reviews with score >= 4 considered positive, score <= 2 considered negative. (Neutral or 3-star reviews may be filtered out or used as needed.)

Preprocessing steps applied included:

Cleaning text (lowercasing, removing punctuation, stop-words)

Splitting into training / validation sets

Tokenization / vectorization (depending on model, e.g. TF-IDF or embeddings)

🚧 Limitations & Biases

Reviews are user-generated, so have natural bias (e.g. more likely to review when extremely satisfied or dissatisfied).

Time distribution is skewed toward older reviews — performance on newer linguistic styles or slang might differ.

Some reviews are very short, some have missing fields.

🛠 How to Load

Example code to load in Python:

import pandas as pd

# Suppose you've downloaded and unzipped the dataset file, e.g. `Reviews.csv` or `finefoods.txt.gz`
df = pd.read_csv("data/amazon_fine_food_reviews.csv")  # or `pd.read_table` if needed
# Inspect fields
print(df.columns)
print(df.head())

✅ Citation

If you use this dataset, please cite:

J. McAuley and J. Leskovec. From amateurs to connoisseurs: modeling the evolution of user expertise through online reviews. WWW, 2013. 
SNAP
