from nltk.tokenize import word_tokenize,sent_tokenize,PunktSentenceTokenizer
import nltk
import json
from nltk.corpus import opinion_lexicon
from nltk.sentiment.vader import SentimentIntensityAnalyzer


data_set=[]
loc_data_set=[]
neg_data_set=[]

with open('neutral_tweets.json', 'r', newline='\n') as f:
    for line in f:
        tweet = json.loads(line)
        cent_tokens = sent_tokenize(tweet['text'])
        words=nltk.word_tokenize(tweet['text'])

        tagged=nltk.pos_tag(words)
        extractor = r"""SS:  {<NN.?><PR.?>*<VB.?><RB.?><JJ.?>*}   """
        eparser = nltk.RegexpParser(extractor)
        parsed = eparser.parse(tagged)
        print(neg_sents)


def get_data_set(file):
    with open(file, 'r', newline='\n') as f:
        for line in f:
            tweet = json.loads(line)

            data_set.append(tweet['text'])
            loc_data_set.append(tweet['user']['location'])
        return

def parse_data(sentence,loc):

        sid = SentimentIntensityAnalyzer()
        ss = sid.polarity_scores(sentence[0])

        if ss['neg']*100>44:
            fdata = {'Tweet': sentence[0], 'Location': loc}
            neg_data_set.append(fdata)
            print(fdata)


        # negative_data_set.append(cent_tokens)
        #  words = nltk.word_tokenize(twet['text'])
        # tagged = nltk.pos_tag(words)
        #  extractor = r"""SS:  {<NN.?><PR.?>+<VB.?><RB.?><JJ.?>*}   """
        # eparser = nltk.RegexpParser(extractor)
        # parsed = eparser.parse(tagged)

def dump_to_new_file():
    for text, loc in zip(data_set,loc_data_set):
        data={'Tweet': text, 'Location': loc}


        with open('output.json','a+') as file:
            json.dump(data, file) #intermediary file to write locations and Tweets in.
def dump_to_final_file(data):
    for f,d in data:



        with open('final.json','a+') as file:
            json.dump(f, file)

get_data_set('neutral_tweets.json')
new_data_set=[]
new_location_set=[]
for i in data_set:
    cent_tokens = sent_tokenize(i)

    new_data_set.append(cent_tokens)
for data,location in zip(new_data_set,loc_data_set):
    parse_data(data,location)

dump_to_new_file()
dump_to_final_file(new_data_set)
