#Cleaning Text
#1) Create Text file and take text from it
#2) Convert the letters into lowercase ('Apple' is not equal to 'apple')
#3) Removing punctuations like.,!? etc. (Hi! This is buildwithpython.)

import string
text  = open("read.txt" , encoding= "utf-8").read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('' , '' , string.punctuation))
print(cleaned_text)