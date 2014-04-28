'''
Created on Apr 21, 2014

@author: fox
'''
from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
               
    def test_cannot_add_empty_list_items(self):
        self.browser.get(self.server_url)
        self.browser.find_element_by_id('id_new_item').send_keys('\n')
        
        
             