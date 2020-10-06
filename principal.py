from selenium import webdriver
import unittest
import time
#from pages.pageindex import *
#from pages.pageitemlist import *
#from pages.pageitem import *

#clase donde van a estar los casos de prueba
#hereda de unittest
class Items(unittest.TestCase):


    def test_view_item_page(self):

        driver = webdriver.Chrome('chromedriver.exe')
        driver.get('http://localhost:9380/dependencias/crear')#abre el navegador en esta dirección

        #busca el campo por "id" e ingresa el dato, para todos los campos
        driver.find_element_by_id('nombre').send_keys('nombre')
        driver.find_element_by_id('tipo').send_keys('tipo')
        driver.find_element_by_id('localizacion').send_keys('localizacion')
        driver.find_element_by_id('fecha').send_keys('fecha')

        #Presiona el botón guardar
        driver.find_element_by_name('guardar').click()
        
        #espera 4 segundos, a veces la página no carga rápido y marca error
        time.sleep(4)

        #¿esto hay que repetirlo siempre?

        '''
        page_index = Page_index(self.driver)
        page_item_list = Page_item_list(self.driver)
        page_item = Page_item(self.driver)
        page_index.search_items('dress')
        page_item_list.click_first_item()
        page_item.verify_text('Printed Summer Dress')

        '''

    def test_search_with_no_items(self):

        '''
        page_index = Page_index(self.driver)
        page_index.search_items('computer')

        '''

'''
    def tearDown(self):
        self.driver.quit()

'''


#Ejecutar la clase
if __name__ == '__main__':
    unittest.main()