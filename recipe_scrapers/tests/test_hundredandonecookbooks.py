import os
import unittest

from recipe_scrapers.hundredandonecookbooks import HundredAndOneCookbooks


class TestHundredAndOneCookbooksScraper(unittest.TestCase):
    def setUp(self):
        # tests are run from tests.py
        with open(os.path.join(
            os.getcwd(),
            'recipe_scrapers',
            'tests',
            'test_data',
            '101cookbooks.testhtml'
        )) as file_opened:
            self.harvester_class = HundredAndOneCookbooks(file_opened, test=True)

    def test_host(self):
        self.assertEqual(
            '101cookbooks.com',
            self.harvester_class.host()
        )

    def test_title(self):
        self.assertEqual(
            self.harvester_class.title(),
            "Curried Tomato Tortellini Soup"
        )

    def test_total_time(self):
        self.assertEqual(
            0,
            self.harvester_class.total_time()
        )

    def test_ingredients(self):
        self.assertEqual(
                "4  big handfuls spinach, chopped (or frozen equiv) "
                "2 tablespoons extra virgin olive oil"
                "1  medium yellow onion, diced"
                "3 cloves garlic, minced"
                "2 1/2 teaspoons curry powder"
                "3/4 teaspoon sweet (or smoked) paprika"
                "1/2 teaspoon ground turmeric"
                "3/4 teaspoon red chile flakes"
                "1 28- ounce can whole tomatoes, with liquid"
                "3/4 cup dried red lentils, rinsed"
                "4 cups water"
                "1 teaspoon fine grain sea salt, plus more to taste"
                "8 ounces / 1/2 pound fresh tortellini"
                "to serve: a bit of grated cheese, lemon (optional)"
            ,
            self.harvester_class.ingredients()
        )

    def test_instructions(self):
        return self.assertEqual(
            "If you're using frozen spinach, set it on the counter to thaw a bit. In the meantime, heat the olive oil in a large pot over medium-high heat. Stir in the onion and cook, stirring occasionally, for 5 minutes or so, until the onion has softened a bit. Stir in the garlic, wait a minute, then add the curry powder, paprika, turmeric, and chile flakes, and stir well.&nbsp;",
            "Break up the tomatoes with your hands as you add them to the pot along with the tomato liquid, stir in the lentils, and the water. Cover and allow to cook for 15 minutes or so, until the lentils have cooked through. Stir in the salt, and then the tortellini. Cover and cook for another 3-5 minutes, or per package instructions - until tender and cooked through. Stir in the spinach bring back to a simmer, and serve with a dusting of cheese and a squeeze of lemon juice. If you need to thin out with a bit more water, do so, and re-season. Enjoy!",
            self.harvester_class.instructions()
        )
