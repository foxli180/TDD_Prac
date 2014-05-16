'''
Created on Apr 21, 2014

@author: fox
'''
from .base import FunctionalTest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys



  
class NewVisitorTest(FunctionalTest):  
    def test_can_start_a_list_and_retrieve_it_later(self):
        self.browser.get(self.server_url)
        
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)
        
        inputbox =self.get_item_input_box()
        self.assertEqual(
                         inputbox.get_attribute('placeholder'),
                         'Enter a to-do item'
                         )
        
        inputbox.send_keys('Buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        edith_list_url = self.browser.current_url
        
        
        self.assertRegex(edith_list_url, '/lists/.+')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        
        inputbox =self.get_item_input_box()
        inputbox.send_keys('Use peacock feathers to make a fly')
        inputbox.send_keys(Keys.ENTER) 
        
        
        self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
        self.check_for_row_in_list_table('1: Buy peacock feathers')
        

        self.browser.quit()
        self.browser = webdriver.Firefox()
        self.browser.maximize_window()
        
        self.browser.get(self.server_url)
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertNotIn('make a fly',page_text)
        
        inputbox =self.get_item_input_box()
        inputbox.send_keys('Buy Milk')
        inputbox.send_keys(Keys.ENTER)         
        
        francis_list_url = self.browser.current_url
        self.assertRegex(francis_list_url, '/lists/.+')
        self.assertNotEqual(francis_list_url, edith_list_url) 
        
        
  
        page_text = self.browser.find_element_by_tag_name('body').text
        self.assertNotIn('Buy peacock feathers', page_text)
        self.assertIn('Buy Milk', page_text)         
        '''
        self.assertTrue(
                        any(row.text == '1: Buy peacock feather' for row in rows),
                        "New to-do item did not appear in teble -- its text was :\n%s" %
                        table.text,
                        )
        '''
        #using asserIn replace assertTrue
        #self.assertIn('1: Buy peacock feathers', [row.text for row in rows])
        #self.assertIn('2: Use peacock feathers to make a fly', [row.text for row in rows])

