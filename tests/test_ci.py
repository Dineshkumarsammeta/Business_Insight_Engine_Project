import os
import pandas as pd
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from nltk.corpus import stopwords
import nltk

def test_tensorflow_import():
    """Check if TensorFlow loads properly"""
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
    dataset_path = "preprocessed_reviews.csv"
    if not os.path.exists(dataset_path):
        print("⚠️ Dataset not found, creating mock dataset for CI")
        df = pd.DataFrame({
            "review": ["I love this product", "Worst experience ever", "Not bad, could be better"],
            "label": [1, 0, 1]
        })
        df.to_csv(dataset_path, index=False)

    assert os.path.exists(dataset_path)
    df = pd.read_csv(dataset_path)
    assert "review" in df.columns
    assert "label" in df.columns
    print("✅ Dataset ready")

def test_tokenizer_pipeline():
    """Run a small tokenizer + padding pipeline"""
    df = pd.read_csv("preprocessed_reviews.csv")
    tokenizer = Tokenizer(num_words=1000, oov_token="<OOV>")
    tokenizer.fit_on_texts(df["review"].astype(str))
    sequences = tokenizer.texts_to_sequences(df["review"].astype(str))
    padded = pad_sequences(sequences, maxlen=10, padding="post")
    assert padded.shape[0] == len(df)
    print("✅ Tokenizer & padding pipeline works")
