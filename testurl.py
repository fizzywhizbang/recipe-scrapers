#!/usr/bin/env python3

from recipe_scrapers import scrape_me
import sys, types

print("%s" % (sys.argv[1]))  # for testing
url = sys.argv[1]
if not url.endswith("/"):
    url = url + "/"

#12tomatoes
#https://12tomatoes.com/cowboy-soup/
#url = "https://www.101cookbooks.com/archives/quick-blistered-cherry-tomato-spaghetti/"

def listToString(list1):
    return '\n'.join(list1)

scrape_me = scrape_me(url)

title = scrape_me.title()
totalTime = scrape_me.total_time()

ingredients = scrape_me.ingredients()

if type(ingredients) is list:
    ingredients = listToString(ingredients)

instructions = scrape_me.instructions()
if type(instructions) is list:
    instructions = listToString(instructions)

description = scrape_me.description()
category = scrape_me.category()
imgURL = scrape_me.imgURL()
sodium = scrape_me.sodium()
fat = scrape_me.fat()
carbs = scrape_me.carbs()
calories = scrape_me.calories()
#datePublished = scrape_me.datePublished()
cholesterol = scrape_me.cholesterol()
rawdata = scrape_me.rawData()

print("Title:%s" % title)
print("Link:%s" % url)
#print("Date Published:%s" % datePublished)
print("Description:%s" % description)
print("TotalTime:%s" % totalTime)
print("Ingredients:%s" % ingredients)
print("Instructions:%s" % instructions)
print("Category:%s" % category)
print("IMG:%s" % imgURL)
print("Sodium:%s" % sodium)
print("Fat:%s" % fat)
print("Carbs:%s" % carbs)
print("Calories:%s" % calories)
print("Cholesterol:%s" % cholesterol)

print(rawdata)