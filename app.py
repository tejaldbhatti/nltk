from flask import Flask, render_template , request 
import nltk
from nltk.stem import WordNetLemmatizer

import pickle
from nltk.corpus import stopwords
stopwords = stopwords.words('english')
import string

punct = string.punctuation
app = Flask(__name__)


@app.route('/')
def hello():
    return render_template('form.html')

@app.route('/submit', methods = ['POST'])
def form_data():
   user_data = request.form.get('user_data')
   lemma = WordNetLemmatizer()
   sent = nltk.sent_tokenize(user_data)
   words = nltk.word_tokenize(user_data)

   stop_words = []
   for i in words:
        if i in stopwords:
            stop_words.append(i)
        


   return render_template('predict.html', data = f'num of sentences {sent},count of sentences {len(sent)}, num of words {words}, count of words {len(words)}, nu of stop words {stop_words}')

if __name__ == '__main__':
    app.debug = True
    app.run()
