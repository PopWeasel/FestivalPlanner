from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class StartupTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def testCreatePerformer(self):
        self.browser.get("http://localhost:8000/performers")
        self.assertIn('Performers', self.browser.title)

        performerNameInput = self.browser.find_element_by_id('performerName')
        self.assertEqual(
            performerNameInput.get_attribute('placeholder'),
            'Enter name'
        )

        performerName = "The Lucksmiths"
        performerNameInput.send_keys(performerName)
        performerNameInput.send_keys(Keys.ENTER)

        performerTable = self.browser.find_element_by_id('performerTable')
        rows = performerTable.find_elements_by_tag_name('tr')
        self.assertIn(performerName, [row.text for row in rows])
        self.fail("Write more tests")



if __name__ == '__main__':
    unittest.main(warnings='ignore')
