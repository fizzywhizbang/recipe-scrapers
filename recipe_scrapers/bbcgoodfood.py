from ._abstract import AbstractScraper
from ._utils import get_minutes, normalize_string


class BBCGoodFood(AbstractScraper):
        @classmethod
        def host(self):
            return 'bbcgoodfood.com'

        def title(self):
            title = self.soup.find("meta", property="og:title")
            return title['content']

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
                {'itemprop': "ingredients"}
            )

            return [
                normalize_string(ingredient["content"])
                for ingredient in ingredients

            ]

        def instructions(self):
            instructions = self.soup.findAll(
                'li',
                {'itemprop': 'recipeInstructions'}
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

            dateClean = date["datetime"] + " 00:00:00"

            return dateClean

        def category(self):
            category = self.soup.findAll(
                'meta',
                {'itemprop': 'recipeCategory'}
            )

        def sodium(self):
            return self.soup.find(
                'h3',
                {'itemprop': 'sodiumContent'}
            ).get_text()

        def fat(self):
            return self.soup.find(
                'h3',
                {'itemprop': 'fatContent'}
            ).get_text()

        def carbs(self):
            return self.soup.find(
                'h3',
                {'itemprop': 'carbohydrateContent'}
            ).get_text()

        def calories(self):
            return self.soup.find(
                'h3',
                {'itemprop': 'calories'}
            ).get_text()

        def cholesterol(self):
            return "999999"

        def rawData(self):
            return self.soup