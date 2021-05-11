from ._abstract import JSONScraper
from ._utils import get_minutes, normalize_string, dateCleaner

class Eatingwell(JSONScraper):
    @classmethod
    
    def host(self):
        return 'eatingwell.com'

    def title(self):
        return self.data[1]["name"]
    #need to figure out something for date published
    def datePublished(self):
        date = dateCleaner("null",6)
        return date

    def description(self):
        return self.data[1]["description"]


    def total_time(self):
        return get_minutes(data["totalTime"])


    def ingredients(self):
        ing = ""
        ingList = self.data[1]['recipeIngredient']
        i = 0
        while i < len(ingList):
            ing += ingList[i] + "\n"
            i += 1
        return ing


    def instructions(self):
        #this is a nested array
        instrList = self.data[1]['recipeInstructions']
        i = 0
        instr = ""
        while i < len(instrList):
            instr += instrList[i]['text'] + "\n"
            i += 1

        return instr

    def category(self):
        return self.data[1]["recipeCategory"][0]

    def imgURL(self):
        return self.data[1]["image"]['url']


    def sodium(self):
        return self.data[1]["nutrition"]["sodiumContent"]

    def fat(self):
        return self.data[1]["nutrition"]["fatContent"]

    def carbs(self):
        return self.data[1]["nutrition"]["carbohydrateContent"]

    def calories(self):
        return self.data[1]["nutrition"]["calories"]


    def cholesterol(self):
        return self.data[1]["nutrition"]["cholesterolContent"]

    def rawData(self):
        return self.data[1]