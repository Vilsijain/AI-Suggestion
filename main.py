import os
from flask import Flask,jsonify
import nltk
nltk.download("wordnet")
nltk.download('omw-1.4')
from nltk.corpus import wordnet

app = Flask(__name__)

@app.get('/<string:word>')
def part(word):
    synonyms = []
    result = set()
    for syn in wordnet.synsets(word):
        for each_lemmas in syn.lemmas():
            synonyms.append(each_lemmas.name())
            for each_synonym in synonyms: 
                result.add(each_synonym.replace('_', ''))
    return jsonify(list(result))
                      
  
if __name__ == '__main__':
    port = os.getenv('PORT',None) or 80
    app.run(host='0.0.0.0',port=port)