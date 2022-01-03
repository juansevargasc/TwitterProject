

exclude_words = ['el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'al', 'del', 'lo', 'le', 'y', 'e', 'o', 'u', 'de', 'a', 'en', 'que', 'es', 'por', 'para', 'con', 'se', 'su', 'les', 'me', 'q', 'te', 'pero', 'mi', 'ya', 'cuando', 'como', 'estoy', 'voy', 'porque', 'he', 'son', 'solo', 'tengo', 'muy']


def analyze(topic):

    top_words = {}
    tweets_topic = open(topic, encoding='utf-8')
    for line in tweets_topic:
        words = line.strip().lower().split()
        for word in words:
            if word not in exclude_words:
                top_words[word] = top_words.get(word, 0) + 1
    
    tweets_topic.close()
    return top_words

def most_mentioned_people(top_words, most_used_words):
    count_u = 0
    for word in most_used_words:
        if count_u < 10 and word.startswith('@'):
            print(top_words[word], word)
            count_u += 1
    print('*' * 40) # esto es para separar visualmente la información

def top20_words(top_words, most_used_words):
    count = 0
    for word in most_used_words:
        if count < 20:
            print(top_words[word], word)
            count += 1
 
top = analyze('#ParoIndefinido2021.txt') # Returns array of top words
top_sorted = sorted(top, key = top.get, reverse = True) # Orders by quantity of words

#So Results:
most_mentioned_people(top, top_sorted)
top20_words(top, top_sorted)

