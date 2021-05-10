from ._abstract import JSONScraper
from ._utils import get_minutes, normalize_string, timecalc


class BBCFood(JSONScraper):

    @classmethod
    def host(self):
        return 'bbc.co.uk'

    def title(self):
        return self.data["name"]
    #need to figure out something for date published
    def datePublished(self):
        date = dateCleaner("null",6)
        return date

    def description(self):
        return self.data["description"]


    def total_time(self):
        cooktime = data["cookTime"]
        preptime = data["prepTime"]
        print(cooktime)
        total_time = timecalc(cooktime) + timecalc(preptime)

        return total_time


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
        return self.data["recipeCategory"]

    def imgURL(self):
        return self.data["image"]


    def sodium(self):
        return "999999"

    def fat(self):
        return "999999"

    def carbs(self):
        return "999999"

    def calories(self):
        return "999999"


    def cholesterol(self):
        return "999999"

    def rawData(self):
        return self.data
