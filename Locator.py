
from selenium.webdriver.common.by import By
import data
import codigo
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
# Se cambio el nombre a UrbanRoutes Page y se añadio las interacciones con los localizadores
class UrbanRoutesPage:

    from_field = (By.ID, 'from')
    to_field = (By.ID, 'to')
    mode_button = (By.CSS_SELECTOR, ".modes-container")
    ask_taxi = (By.CLASS_NAME, 'button.round')
    comfort_tariff = (By.CSS_SELECTOR, "div.tcard:nth-child(5)>div:nth-child(3)")
    # Se cambio el selector a css selector para elegir la tarifa Comfort
    selected_tariff = (By.CLASS_NAME, 'r-sw-label')
    #Se cambio el selector para verificar la tarifa Comfort haciendo uso de requisito manta y pañuelos
    phone = (By.CLASS_NAME, "np-button")
    add_phone_number = (By.ID, 'phone')
    get_number = (By.CLASS_NAME, 'np-text')
    next_button = (By.CLASS_NAME, "button.full")
    add_code = (By.ID, 'code')
    confirmation_code = (By.CSS_SELECTOR, '.section.active>form>.buttons>:nth-child(1)')
    payment_method = (By.CLASS_NAME, 'pp-button.filled')
    card = (By.CLASS_NAME, 'pp-plus-container')
    card_number = (By.CSS_SELECTOR, '#number.card-input')
    code_card = (By.CSS_SELECTOR, '#code.card-input')
    card_space = (By.CSS_SELECTOR, '.plc')
    add_credit_card = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[2]/form/div[3]/button[1]')
    close_card_button = (By.XPATH, '//*[@id="root"]/div/div[2]/div[2]/div[1]/button')
    driver_message = (By.ID, "comment")
    blanket_tissues = (By.XPATH,"//*[@id='root']/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[1]/div/div[2]/div/span")
    blanket_check = (By.CSS_SELECTOR, '.r-sw > div > input')
    ice_cream = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[3]')
    get_ice = (By.XPATH, '//*[@id="root"]/div/div[3]/div[3]/div[2]/div[2]/div[4]/div[2]/div[3]/div/div[2]/div[1]/div/div[2]/div/div[2]')
    reserve_button = (By.CLASS_NAME, "smart-button")
    details = (By. CLASS_NAME, 'order-body')
    timer = (By.CLASS_NAME, 'order-header-content')

    def __init__(self, driver):
        self.driver = driver

    def set_from(self, from_address):
        self.driver.find_element(*self.from_field).send_keys(from_address)

    def set_to(self, to_address):
        self.driver.find_element(*self.to_field).send_keys(to_address)

    def get_from(self):
        return self.driver.find_element(*self.from_field).get_property('value')

    def get_to(self):
        return self.driver.find_element(*self.to_field).get_property('value')

    def click_ask_taxi(self):
        self.driver.find_element(*self.ask_taxi).click()

    def set_route(self, address_from, address_to):
        self.set_from(address_from)
        self.set_to(address_to)

    def click_comfort(self):
        comfort_element = self.driver.find_element(*self.comfort_tariff)
        comfort_element.click()

    def get_comfort(self):
        return self.driver.find_element(*self.selected_tariff).text


    def set_comfort(self):
        self.click_ask_taxi()
        self.click_comfort()

    def phone_number(self):
        self.driver.find_element(*self.phone).click()

    def insert_phone_number(self):
        self.driver.find_element(*self.add_phone_number).send_keys(data.phone_number)

    def get_phone_number_text(self):
        return self.driver.find_element(*self.get_number).text #Se agrego esta funcion para comprobar el numero y la forma de comprobarlo

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def insert_phone_code(self):
        self.driver.find_element(*self.add_code).send_keys(codigo.retrieve_phone_code(self.driver))

    def confirmation_phone(self):
        self.driver.find_element(*self.confirmation_code).click()

    def add_new_phone_number(self):
        self.phone_number()
        self.insert_phone_number()
        self.click_next_button()
        self.insert_phone_code()
        self.confirmation_phone()

    def click_payment_method(self):
        self.driver.find_element(*self.payment_method).click()

    def credit_card(self):
        self.driver.find_element(*self.card).click()

    def add_card_number(self):
        self.driver.find_element(*self.card_number).send_keys(data.card_number)

    def get_card_number(self):
        return self.driver.find_element(*self.card_number).get_property('value')

    def add_card_code(self):
        self.driver.find_element(*self.code_card).send_keys(data.card_code)

    def get_card_code(self):
        return self.driver.find_element(*self.code_card).get_property('value')

    def click_card_space(self):
        self.driver.find_element(*self.card_space).click()

    def add_new_credit_card(self):
        self.driver.find_element(*self.add_credit_card).click()

    def close_add_card(self):
        self.driver.find_element(*self.close_card_button).click()

    def new_credit_card(self):
        self.click_payment_method()
        self.credit_card()
        self.add_card_number()
        self.add_card_code()
        self.click_card_space()
        self.add_new_credit_card()
        self.close_add_card()

    def send_driver_message(self):
        self.driver.find_element(*self.driver_message).send_keys(data.message_for_driver)

    def get_message(self):
        return self.driver.find_element(*self.driver_message).get_property('value')

    def click_blanket_switch(self):
        self.driver.find_element(*self.blanket_tissues).click()

    def get_blanket_switch_state(self):
        return self.driver.find_element(*self.blanket_check).is_selected()

    def add_ice_cream(self):
        ice_cream_element = WebDriverWait(self.driver, 4).until(
            expected_conditions.element_to_be_clickable(self.ice_cream)
        )
        ice_cream_element.click()
        ice_cream_element.click()

    def get_ice_cream(self):
        return self.driver.find_element(*self.get_ice).text

    def reserve_taxi_button(self):
        self.driver.find_element(*self.reserve_button).click()

    def get_order_section(self):
        return self.driver.find_element(*self.details).is_displayed()

    def driver_info(self):
        #time.sleep(20)
        WebDriverWait(self.driver, 60).until(expected_conditions.visibility_of_element_located(UrbanRoutesPage.details))
        return self.driver.find_element(*self.timer).is_displayed()
