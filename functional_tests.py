from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # look up homepage
        self.browser.get('http://localhost:8000')

        #see "To-DO"
        self.assertIn('To-Do',self.browser.title)
        header_test = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do',header_test)

        #app visit her add an item
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(
            inputbox.get_attribute('placeholder'),
            'Enter a to-do item'
        )

        #input "buy peacock feathers"
        inputbox.send_keys('Buy peacock feathers')

        #press enter,and the page reflash
        #list show "1\buy peacock feathers"
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1:Buy peacock feathers' for row in rows)
        )

        # appear text block on page,can input other items
        # she input "use peacock feathers to make a fly"
        self.fail('Finish the text!')

        # the page reflash again and show these two items
if __name__=='__main__':
     unittest.main(warnings='ignore')

