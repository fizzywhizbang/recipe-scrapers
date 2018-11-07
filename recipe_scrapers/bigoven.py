
from ._abstract import JSONScraper
from ._utils import get_minutes, normalize_string, dateCleaner

class BigOven(JSONScraper):

    @classmethod
    def host(self):
        return 'bigoven.com'

    def title(self):
        return self.data["name"]

    #need to figure out something for date published
    def datePublished(self):
        date = dateCleaner(self.data["datePublished"],6)
        return date

    def description(self):
        return self.data["description"]


    def total_time(self):
        return get_minutes(data["prepTime"])


    def ingredients(self):
        ing = ""
        ingList = self.data['recipeIngredient']
        i = 0
        while i < len(ingList):
            ing += ingList[i] + "\n"
            i += 1
        return ing


    def instructions(self):
        #this is a nested array
        instrList = self.data['recipeInstructions']
        i = 0
        instr = ""
        while i < len(instrList):
            instr += instrList[i] + "\n"
            i += 1

        return instr

    def category(self):
        if len(self.data["recipeCategory"][0]) == 1:
            return self.data["recipeCategory"]
        else:
            return self.data["recipeCategory"][0]

    def imgURL(self):
        if len(self.data["image"][0]) == 1:
            return self.data["image"]
        else:
            return self.data["image"][0]


    def sodium(self):
        return self.data["nutrition"]["sodiumContent"]

    def fat(self):
        return self.data["nutrition"]["fatContent"]

    def carbs(self):
        return self.data["nutrition"]["carbohydrateContent"]

    def calories(self):
        return self.data["nutrition"]["calories"]

    def cholesterol(self):
        return self.data["nutrition"]["cholesterolContent"]

    def rawData(self):
        return self.data