import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import data
import codigo
from Locator import UrbanRoutesLocator

class UrbanRoutesPage:
    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*UrbanRoutesLocator.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*UrbanRoutesLocator.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*UrbanRoutesLocator.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*UrbanRoutesLocator.to_field).get_property('value')

    def click_ask_taxi(self):
        self.driver.find_element(*UrbanRoutesLocator.ask_taxi).click()

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_comfort(self):
        comfort_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.visibility_of_element_located(UrbanRoutesLocator.comfort_tariff)
        )
        comfort_element.click()
        assert 'Comfort' in comfort_element.text

    def set_comfort(self):
        self.click_ask_taxi()
        self.click_comfort()

    def phone_number(self):
        self.driver.find_element(*UrbanRoutesLocator.phone).click()

    def insert_phone_number(self):
        self.driver.find_element(*UrbanRoutesLocator.add_phone_number).send_keys(data.phone_number)

    def get_phone_number_text(self):
        return self.driver.find_element(*UrbanRoutesLocator.add_phone_number).get_attribute('value')

    def click_next_button(self):
        self.driver.find_element(*UrbanRoutesLocator.next_button).click()

    def insert_phone_code(self):
        self.driver.find_element(*UrbanRoutesLocator.add_code).send_keys(codigo.retrieve_phone_code(self.driver))

    def confirmation_phone(self):
        self.driver.find_element(*UrbanRoutesLocator.confirmation_code).click()

    def add_new_phone_number(self):
        self.phone_number()
        self.insert_phone_number()
        self.click_next_button()
        self.insert_phone_code()
        self.confirmation_phone()

    def click_payment_method(self):
        self.driver.find_element(*UrbanRoutesLocator.payment_method).click()

    def credit_card(self):
        self.driver.find_element(*UrbanRoutesLocator.card).click()

    def add_card_number(self):
        self.driver.find_element(*UrbanRoutesLocator.card_number).send_keys(data.card_number)

    def add_card_code(self):
        self.driver.find_element(*UrbanRoutesLocator.code_card).send_keys(data.card_code)

    def click_card_space(self):
        self.driver.find_element(*UrbanRoutesLocator.card_space).click()

    def add_new_credit_card(self):
        self.driver.find_element(*UrbanRoutesLocator.add_credit_card).click()

    def close_add_card(self):
        self.driver.find_element(*UrbanRoutesLocator.close_card_button).click()

    def new_credit_card(self):
        self.click_payment_method()
        self.credit_card()
        self.add_card_number()
        self.add_card_code()
        self.click_card_space()
        self.add_new_credit_card()
        self.close_add_card()

    def send_driver_message(self):
        self.driver.find_element(*UrbanRoutesLocator.driver_message).send_keys(data.message_for_driver)

    def click_blanket_switch(self):
        self.driver.find_element(*UrbanRoutesLocator.blanket_tissues).click()

    def get_blanket_switch_state(self):
        return self.driver.find_element(*UrbanRoutesLocator.blanket_check).is_selected()

    def add_ice_cream(self):
        ice_cream_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.element_to_be_clickable(UrbanRoutesLocator.ice_cream)
        )
        ice_cream_element.click()
        time.sleep(0.5)
        ice_cream_element.click()

    def reserve_taxi_button(self):
        self.driver.find_element(*UrbanRoutesLocator.reserve_button).click()

    def get_driver(self):
        WebDriverWait(self.driver,60).until(expected_conditions.visibility_of_element_located(UrbanRoutesLocator.driver))
        self.driver.find_element(*UrbanRoutesLocator.details).click()
            #return self.driver.find_element(*UrbanRoutesLocator.)

class TestUrbanRoutes:
    driver = None

    @classmethod
    def setup_class(cls):
        # no lo modifiques, ya que necesitamos un registro adicional habilitado para recuperar el código de confirmación del teléfono
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(3)

    def test_set_route(self):
        self.driver.get(data.urban_routes_url)
        routes_page = UrbanRoutesPage(self.driver)
        address_from = data.address_from
        address_to = data.address_to
        routes_page.set_route(address_from, address_to)
        assert routes_page.get_from() == address_from
        assert routes_page.get_to() == address_to

    def test_tariff_picker(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.set_comfort()

    def test_select_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_new_phone_number()
        assert routes_page.get_phone_number_text() == data.phone_number

    def test_new_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.new_credit_card()

    def test_send_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.send_driver_message()

    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        #routes_page.send_request_order()
        routes_page.click_blanket_switch()
        assert routes_page.get_blanket_switch_state() == True

    def test_add_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream()

    def test_click_reserve_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.reserve_taxi_button()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
