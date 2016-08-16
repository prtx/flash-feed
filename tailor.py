#!/usr/bin/python
# -*- coding: utf-8 -*-

import nltk, sys, json, os

reload(sys)
sys.setdefaultencoding("utf8")
home = os.getcwd()


all_files = []
offset_length = 15


def fetch(offset, category, directory="English"):

    for path, subdirs, files in os.walk(home + "/Summaries/" + directory):
        for name in files:
            all_files.append([os.path.join(path, name), int(name.split(".")[0])])
    all_files.sort(key=lambda x: x[1])

    newspaper = []
    counter = offset

    for a_file in all_files[offset:]:
        article = json.load(open(a_file[0]))
        if category != [] and article["category"] not in category:
            continue
        article["id"] = str(a_file[1])
        counter += 1
        if counter == offset + offset_length:
            break
        newspaper.append(article)

    fetch_file = open(home + "/Fetch/fetch.json", "w")
    json.dump(newspaper, fetch_file, indent=4)
    fetch_file.close()
