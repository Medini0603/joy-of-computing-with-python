# first of all we need to download your
# facebook data, you need to login to your facebook account and then you need to go to 
# settings and download your facebook information there we need to store your
# information In an excel file that I have already explained then you need to import the
# pandas library it basically provide you easy to use data structure for data analysis then
# you need to import nltk library nltk library will help you to process the human
# language it will basically help you to analyse the human data it will help you in
# sentimental analysis of human data, sentiment analysis involves working out whether
# a piece of text is a positive negative or neutral I have already given you a example of
# a positive neutral and negative sentences then you will not be using only nltk will be
# using vader too vader also takes into account the intensity of the sentiment, yes then
# you need to download the vader lexicon, lexicon acts as a dictionary here, you also
# need to convert your excel sheet that you have created to a data frame, what is a data
# frame? Data frame is basically two dimensional structures in the form of table which
# # is provided by panda’s library 

import pandas as pd
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import csv
nltk.downloader.download('vader_lexicon')
file='facebookana.csv'
# xl=pd.ExcelFile(file)#read from excel file
# now convert our data to dataframes for easy analysis using panda library 
# xl = pd.read_csv(file)
xl = pd.read_csv(file,usecols=['sentiment'])
print(xl)
# dfs=xl.parse(xl.sheet_names[2]) #Parsing excel sheet to data frame
xl=list(xl['sentiment'])
print(xl)
sid=SentimentIntensityAnalyzer()
str1="utf-8"  #to skip timeline info if any
for data in xl:
    if(type(data)!=str):
        data=str(data)
    a=data.find(str1)
    if(a==-1):
        ss=sid.polarity_scores(data)
        print(data)
        for k in ss:
            print(k,ss[k])
        


