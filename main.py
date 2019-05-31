import re
import csv
import sys
from textblob import TextBlob
from textblob_fr import PatternTagger, PatternAnalyzer

class TweetSentiment():
    def get_tweet_sentiment(self, row): 
        analysis = TextBlob(str(row), pos_tagger=PatternTagger(), analyzer=PatternAnalyzer())
        strAnalysis = str(analysis.sentiment)
        sentiment = strAnalysis[strAnalysis.find('(')+1:strAnalysis.find(',')]
    
        if float(sentiment) > 0:
            return 'positive'
        elif float(sentiment) == 0:
            return 'neutral'
        else:
            return 'negative'

    def analyse(self, csvfile):
        reader = csv.reader(f)
        tweets = []
        for row in reader:
            parsed_tweet = {}
            parsed_tweet['text'] = row
            parsed_tweet['sentiment'] = self.get_tweet_sentiment(row = row)
            tweets.append(parsed_tweet)
        return tweets
    
    def saveResult(self, data):
        rescsv = open('sentimentres.csv', 'w', encoding="latin1")
        #spamwriter = csv.writer(csvfile)
        for row in data:
            sent = str(row['sentiment'])
            texte = str(row['text'])
            rescsv.write("{},{},\n".format(sent, texte))

    def saveStat(self, data):
        stat = {}
        stat['nbPos'] = 0
        stat['nbNeg'] = 0
        stat['nbNeu'] = 0
        for sent in data:
            if sent['sentiment'] == 'positive':
                stat['nbPos'] += 1
            elif sent['sentiment'] == 'negative':
                stat['nbNeg'] += 1
            else:
                stat['nbNeu'] += 1
        statcsv = open('stat.csv', 'w', encoding="latin1")
        total = stat['nbPos'] + stat['nbNeg'] + stat['nbNeu']
        statcsv.write("{},{},\n".format('Positif',str(stat['nbPos'])))
        statcsv.write("{},{},\n".format('Negatif',str(stat['nbNeg'])))
        statcsv.write("{},{},\n".format('Neutre',str(stat['nbNeu'])))
        statcsv.write("{},{},\n".format('Total',str(total)))
        return 0


f = open('resinput.csv', 'rt', encoding='latin1')
result = []
ts = TweetSentiment()
result = ts.analyse(csvfile = f)
ts.saveResult(data = result)
ts.saveStat(data = result)


#text = ""
#    for line in file.readlines():
#        text += line.split(",")[2] + " "