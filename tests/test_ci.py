import os
import pandas as pd
import tensorflow as tf
from nltk.corpus import stopwords
import nltk

def test_tensorflow_import():
    """Check if TensorFlow loads properly """
    assert tf.__version__ is not None
    print(f"✅ TensorFlow version: {tf.__version__}")

def test_nltk_stopwords():
    """Ensure stopwords are available"""
    try:
        words = stopwords.words("english")
        assert len(words) > 0
    except LookupError:
        nltk.download("stopwords", quiet=True)
        words = stopwords.words("english")
        assert len(words) > 0
    print("✅ NLTK stopwords loaded")

def test_dataset_exists_or_create_mock():
    """Check dataset exists or create mock CSV"""
    dataset_path = "data/mock_twitter_data.csv"
    os.makedirs("data", exist_ok=True)
    if not os.path.exists(dataset_path):
        print("⚠️ Dataset not found, creating mock dataset for CI")
        df = pd.DataFrame({
            "tweet": [
                "I love this product!",
                "Worst experience ever.",
                "Not bad, could be better."
            ],
            "label": [1, 0, 1]
        })
        df.to_csv(dataset_path, index=False)

    assert os.path.exists(dataset_path)
    df = pd.read_csv(dataset_path)
    assert "tweet" in df.columns and "label" in df.columns
    print("✅ Dataset ready")

def test_tokenizer_pipeline():
    """Run a small tokenizer + padding pipeline"""
    from tensorflow.keras.preprocessing.text import Tokenizer
    from tensorflow.keras.preprocessing.sequence import pad_sequences

    df = pd.read_csv("data/mock_twitter_data.csv")
    tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
    tokenizer.fit_on_texts(df["tweet"].astype(str))
    sequences = tokenizer.texts_to_sequences(df["tweet"].astype(str))
    padded = pad_sequences(sequences, maxlen=10, padding="post")
    assert padded.shape[0] == len(df)
    print("✅ Tokenizer & padding pipeline works")
