import re
from bs4 import BeautifulSoup
import pickle
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences

def decontracted(phrase):
    # specific
    phrase = re.sub(r"won't", "will not", phrase)
    phrase = re.sub(r"can\'t", "can not", phrase)

    # general
    phrase = re.sub(r"n\'t", " not", phrase)
    phrase = re.sub(r"\'re", " are", phrase)
    phrase = re.sub(r"\'s", " is", phrase)
    phrase = re.sub(r"\'d", " would", phrase)
    phrase = re.sub(r"\'ll", " will", phrase)
    phrase = re.sub(r"\'t", " not", phrase)
    phrase = re.sub(r"\'ve", " have", phrase)
    phrase = re.sub(r"\'m", " am", phrase)
    return phrase


def preprocessed(review): 
    sentance = re.sub(r"http\S+", "", review)
    sentance = BeautifulSoup(sentance, 'lxml').get_text()
    sentance = decontracted(sentance)
    sentance = re.sub("\S*\d\S*", "", sentance).strip()
    sentance = re.sub('[^A-Za-z]+', ' ', sentance)
    sentance = ' '.join(e.lower() for e in sentance.split() if e.lower() not in stopwords.words('english'))
    return sentance.strip()


def predict(text,model,tokenizer,chain) : 
    
    review = text
    print("Review : " , review)
    preprocessed_re = preprocessed(review)
    print(preprocessed_re)
    token_sent = tokenizer.texts_to_sequences([preprocessed_re])
    seq = pad_sequences(token_sent, maxlen = 40, padding = "pre", truncating = "post")
    print(seq)
    c = model.predict(seq)

    o = np.argmax(c, axis=1)
    d = {1:"Positive", 0 : "Negative"}
    llm_output = chain.run(Review = review, Sentiment = d[o[0]], verbose = False)
    print("Sentiment Predicted By Deep Learning Model LSTM: ",d[o[0]])
    print("\n")
    print(llm_output)
    
    print("\n")
    print("Sentiment Label & Reason Predicted by LLM")

    llm_output = chain2.run(Review = review,verbose = False)
    print(llm_output)

    return {"Sentiment": d[o[0]],"LLM_REASON":llm_output}
