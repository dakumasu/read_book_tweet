#!python2
# -*- coding: utf-8 -*-
import requests
from bs4 import BeautifulSoup
import re
import tweepy


def setup():
    CONSUMER_KEY = 'xxxxxxxxxxxxxxxx'
    CONSUMER_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    ACCESS_TOKEN = 'xxxxxxxxx-xxxxxxxxxxxxxxxxxxxxxxxxxxx'
    ACCESS_SECRET = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'
    auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
    return auth

def search(word):
    t = 0
    list = [] 
    ty = 'search-alias%3Ddigital-text'
    target = 'https://www.amazon.co.jp/s/?keywords={}&url={}'.format(word, ty)
    url = requests.get(target)
    soup = BeautifulSoup(url.text, "lxml")
    h = ('a-link-normal '
         's-access-detail-page s-'
         'color-twister-title-link a-text-normal')
    get = soup.find_all('a', class_=h)
    for element in get:
        element = str(element)
        title = str(re.findall('title="(.*)"><h2 class', element)[0])
        link = str(re.findall('href="(.*)" target', element)[0])
        print('No.{} {}'.format(t, title))
        t += 1
        list.append(title)
        list.append(link)
    return list


def tweet(list, no, api):
    sentence = 'I read this book\n{} {}'.format(list[2 * no], list[2 * no + 1])
    api.update_status(sentence)
    print('Tweet had already done : {}'.format(sentence))



search_word = input('Fill in the book name>>>')
result = search(search_word)
number = int(input('Select number.\nNo>>>'))
api = setup()
tweet(result, number, api)
