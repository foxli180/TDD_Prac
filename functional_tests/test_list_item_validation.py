'''
Created on Apr 21, 2014

@author: fox
'''
from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
    
    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error') 
               
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        
        error = self.get_error_element()
        self.assertEqual(error.text,"You can't have an empty list item")
        
        self.get_item_input_box().send_keys('Buy Milk\n')
        self.check_for_row_in_list_table('1: Buy Milk')
        
        self.get_item_input_box().send_keys('\n')
        
        self.check_for_row_in_list_table('1: Buy Milk')
        error = self.get_error_element()
        self.assertEqual(error.text,"You can't have an empty list item")       
        
        self.get_item_input_box().send_keys('Make Tea\n')
        self.check_for_row_in_list_table('1: Buy Milk')  
        self.check_for_row_in_list_table('2: Make Tea')     
    
    def test_cannot_add_duplicate_items(self):
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy wellies\n')
        self.check_for_row_in_list_table('1: Buy wellies')
        
        self.get_item_input_box().send_keys('Buy wellies\n')
        
        self.check_for_row_in_list_table("1: Buy wellies")
        error = self.get_error_element()
        self.assertEqual(error.text,"You've already got this in your list")
        
    def test_error_message_are_cleared_on_input(self): 
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())
        
        self.get_item_input_box().send_keys('a')
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())
        
  
        
        
        
        
        
               