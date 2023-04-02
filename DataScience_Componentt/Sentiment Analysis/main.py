#Cleaning Text
# 1)Create Text file and take text from it
#2)Conver the letters into lowercase
#3)Removing punctuations

import string
text  = open("read.txt" , encoding= "utf-8").read()
lower_case = text.lower()
cleaned_text = lower_case.translate(str.maketrans('' , '' , string.punctuation))
print(cleaned_text)



