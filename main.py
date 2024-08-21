
from selenium import webdriver
import data
from Locator import UrbanRoutesPage
from selenium.webdriver.support.ui import WebDriverWait


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
        assert routes_page.get_comfort() == 'Comfort' #Se añadio el assert en las pruebas

    def test_select_phone(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_new_phone_number()
        assert routes_page.get_phone_number_text() == data.phone_number

    def test_new_credit_card(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.new_credit_card()
        assert routes_page.get_card_number() == data.card_number
        assert routes_page.get_card_code() == data.card_code

    def test_send_message(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.send_driver_message()
        assert routes_page.get_message() == data.message_for_driver

    def test_blanket(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.click_blanket_switch()
        assert routes_page.get_blanket_switch_state() == True

    def test_add_ice_cream(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.add_ice_cream()
        assert routes_page.get_ice_cream() == '2'

    def test_click_reserve_taxi(self):
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.reserve_taxi_button()
        assert routes_page.get_order_section() == True
        WebDriverWait(self.driver,5)

    def test_driver_info(self):
        routes_page = UrbanRoutesPage(self.driver)
        assert routes_page.driver_info() == True
        WebDriverWait(self.driver, 5)


    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
