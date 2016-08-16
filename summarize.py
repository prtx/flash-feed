#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk, sys, json, os

reload(sys)
sys.setdefaultencoding("utf8")
home = os.getcwd()


def all_sentences(text):

    text = text.replace(".", ".\n")
    text = text.replace("?", "?\n")
    text = text.replace("!", "!\n")
    text = text.replace("\t", "")
    text = text.split("\n")

    return [sentence for sentence in text if sentence != ""]


def all_words(text):

    text = text.lower()
    text = text.replace("\n", " ")
    text = text.replace("?", "\n")
    text = text.replace("\t", " ")
    text = text.replace("!", "\n")
    text = text.replace(".", " ")
    text = text.split()

    return text


def summarize(file_name, directory):

    article = json.load(open(file_name))
    stopwords = [stopword.strip() for stopword in open("stopwords.txt").readlines()]

    words = all_words(article["news"])
    word_rank = [
        [word, words.count(word)] for word in list(set(words)) if word not in stopwords
    ]
    word_rank.sort(key=lambda x: x[1], reverse=True)

    words = zip(*word_rank)[0]
    word_rank = zip(*word_rank)[1]
    stem_words = list(
        map((lambda word: nltk.PorterStemmer().stem_word(word.decode("utf-8"))), words)
    )
    sentences = all_sentences(article["news"])
    sentence_rank = []

    for sentence in sentences:
        sentence_rank.append([sentence, 0])
        for word in all_words(sentence):
            if word in words:
                sentence_rank[-1][1] += word_rank[words.index(word)]
            if word in stem_words:
                sentence_rank[-1][1] += word_rank[stem_words.index(word)]
            if word in list(set(article["title"].lower().split("-"))):
                try:
                    sentence_rank[-1][1] += word_rank[words.index(word)]
                except:
                    pass

    sentence_rank.sort(key=lambda x: x[1], reverse=True)

    summary_dict = {}
    json_file = open(
        home + "/Summaries/" + directory + "/" + file_name.split("/")[-1], "w"
    )

    summary_dict["title"] = article["title"]
    summary_dict["category"] = article["category"]
    summary_dict["summary"] = ""

    for sentence in sentences:
        if sentence in zip(*sentence_rank[:4])[0]:
            summary_dict["summary"] += sentence.strip() + " "

    json.dump(summary_dict, json_file, indent=4)
    json_file.close()


if __name__ == "__main__":
    for path, subdirs, files in os.walk(home + "/Articles/English"):
        for name in files:
            summarize(os.path.join(path, name), "English")
    for path, subdirs, files in os.walk(home + "/Articles/Nepali"):
        for name in files:
            summarize(os.path.join(path, name), "Nepali")
