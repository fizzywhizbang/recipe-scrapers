from ._abstract import AbstractScraper
from ._utils import normalize_string


class bhg(AbstractScraper):
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
        return 'bhg.com'

    def title(self):
        title = self.soup.find('meta',property='og:title')
        return title["content"]

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

        return [
            normalize_string(ingredient.get_text())
            for ingredient in ingredients
        ]

    def instructions(self):
        instructions = self.soup.findAll(
            'li',
            {'class': 'recipe__direction'}
        )

        return '\n'.join([
            normalize_string(instruction.get_text())
            for instruction in instructions
        ])

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
        #return category

    def sodium(self):
        return self.soup.find(
            'span',
            {'itemprop': 'sodiumcontent'}
        ).get_text()

    def fat(self):
        return self.soup.find(
            'span',
            {'itemprop': 'fatcontent'}
        ).get_text()

    def carbs(self):
        return self.soup.find(
            'span',
            {'itemprop': 'carbohydratecontent'}
        ).get_text()

    def calories(self):
        return self.soup.find(
            'span',
            {'itemprop': 'calories'}
        ).get_text()


    def cholesterol(self):
        return self.soup.find(
            'span',
            {'itemprop': 'cholesterolcontent'}
        ).get_text()

    def rawData(self):
        return ""