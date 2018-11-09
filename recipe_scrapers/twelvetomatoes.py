from ._abstract import AbstractScraper
from ._utils import normalize_string


class Twelvetomatoes(AbstractScraper):
    '''
            'title',
            'total_time',
            'instructions',
            'ingredients',
            'links',
            'URL',
            'description',
            'imgURL',
            'sodium',
            'fat',
            'cholesterol',
            'carbs',
            'calories',
            'category',
            'datePublished'
    '''
    @classmethod
    def host(self):
        return '12tomatoes.com'

    def title(self):
        return self.soup.find(
            'h3',
            {'itemprop': 'name'}
        ).get_text()

    def total_time(self):
        return 0

    def description(self):
        description = self.soup.find("meta", property="og:description")
        return description['content']

    def imgURL(self):
        img = self.soup.find('meta', property='og:image')
        return img["content"]

    def ingredients(self):
        ingredients = self.soup.findAll(
            'li',
            {'itemprop': "recipeIngredient"}
        )
        ing = ""
        for ingredient in ingredients:
            ing += ingredient.getText()

        return ing


    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'itemprop': 'instruction'}
        )

        instr = ""
        for instruction in instructions:
            instr += instruction.getText()
        return instr

    def datePublished(self):
        date = self.soup.findAll(
            'time',
            {'itemprop': 'datePublished'}
        )

        dateClean = dateCleaner(date["datetime"],6)

        return dateClean


    def category(self):
        category = self.soup.findAll(
            'meta',
            {'itemprop': 'recipeCategory'}
        )


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
        return ""