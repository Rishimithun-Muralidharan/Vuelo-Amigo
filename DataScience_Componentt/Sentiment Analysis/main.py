#Cleaning Text

import string
from collections import Counter
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import matplotlib.pyplot as plt
from nltk.sentiment.vader import SentimentIntensityAnalyzer


text = input("Please enter your openion about our service: ")           #manual input cheak and is succesful
#text = open('read.txt' , encoding='utf-8').read()                        #reading the text file
lower_case = text.lower()                                                #Converting into Lower case
#print(lower_case)
#print("-----------------------------------------------------------")

cleaned_text = lower_case.translate(str.maketrans('' , '' , string.punctuation))                  #Removing punctuation
#print(cleaned_text)
#print("-----------------------------------------------------------")

#splitting text into words
#tokenized_words = cleaned_text.split()
tokenized_words = word_tokenize(cleaned_text, "english")
#print(tokenized_words)
#print("-----------------------------------------------------------")

#stop_words = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              #"yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              #"they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              #"those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              #"does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              #"of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              #"after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              #"further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              #"few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              #"too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]

final_words = []                       #Removing stop words
for word in tokenized_words:           #if word not in stop_words:
    if word not in stopwords.words('english'):
        final_words.append(word)

#print(final_words)
#print("-----------------------------------------------------------")

emotion_list = []
with open('emotions.txt' , 'r') as file:     #Analysing emotion in the sentance
    for line in file:
        clear_line = line.replace('\n' , '').replace(',' , '').replace("'" , '').strip()    #Formatting emotions list
        word, emotion = clear_line.split(':')
        #print('word :' + word + ' ' + 'Emotion :' + emotion)

        if word in final_words:
            emotion_list.append(emotion)

print(emotion_list)
w = Counter(emotion_list)
print(w)

def sentiment_analyse(sentiment_text) :
    score = SentimentIntensityAnalyzer().polarity_scores(sentiment_text)
    neg = score ['neg']
    pos = score['pos']
    if neg > pos:
        print("-----------------This is a Negative Review-----------------")
    elif pos > neg:
        print("-----------------This is a Positive Review-----------------")
    else:
        print("-----------------This is a Neutral Review-----------------")


    #print(score)

sentiment_analyse(cleaned_text)

#Plotting the emotions on the graph
fig , ax1 = plt.subplots()
ax1.bar(w.keys(), w.values())
fig.autofmt_xdate()
plt.savefig('grahp.png')
plt.show
