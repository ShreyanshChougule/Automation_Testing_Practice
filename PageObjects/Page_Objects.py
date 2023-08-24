import time
from selenium.webdriver.common.by import By


class Objects:
    name = (By.XPATH, "//input[@id='name']")
    email = (By.XPATH, "//input[@id='email']")
    phone = (By.XPATH, "//input[@id='phone']")
    address = (By.XPATH, "//textarea[@id='textarea']")
    male = (By.XPATH, "//input[@id='male']")
    sunday = (By.XPATH, "//input[@id='sunday']")
    monday = (By.XPATH, "//input[@id='monday']")
    tuesday = (By.XPATH, "//input[@id='tuesday']")
    friday = (By.XPATH, "//input[@id='friday']")
    saturday = (By.XPATH, "//input[@id='saturday']")
    country = (By.XPATH, "//select[@id='country']")
    colors = (By.XPATH, "//select[@id='colors']")
    date = (By.XPATH, "//input[@id='datepicker']")
    date_picker = (By.ID, "datepicker")

    def __init__(self, driver):
        self.driver = driver

    def enter_name(self, Name):
        self.driver.find_element(*Objects.name).clear()
        self.driver.find_element(*Objects.name).send_keys(Name)

    def enter_email(self, Email):
        self.driver.find_element(*Objects.email).clear()
        self.driver.find_element(*Objects.email).send_keys(Email)

    def enter_phone(self, Phone):
        self.driver.find_element(*Objects.phone).clear()
        self.driver.find_element(*Objects.phone).send_keys(Phone)

    def enter_address(self, Address):
        self.driver.find_element(*Objects.address).clear()
        self.driver.find_element(*Objects.address).send_keys(Address)

    def click_male(self):
        self.driver.find_element(*Objects.male).click()

    def click_sunday(self):
        self.driver.find_element(*Objects.sunday).click()

    def click_monday(self):
        self.driver.find_element(*Objects.monday).click()

    def click_tuesday(self):
        self.driver.find_element(*Objects.tuesday).click()

    def click_friday(self):
        self.driver.find_element(*Objects.friday).click()

    def click_saturday(self):
        self.driver.find_element(*Objects.saturday).click()

    def select_date(self, DD=int, MM=str, YYYY=int):
        self.driver.find_element(*Objects.date_picker).click()
        time.sleep(2)

        mon = self.driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
        yer = self.driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text
        while mon != MM and yer != YYYY:
            self.driver.find_element(By.XPATH, "//span[@class='ui-icon ui-icon-circle-triangle-e']").click()
            time.sleep(1)
            mon = self.driver.find_element(By.CLASS_NAME, "ui-datepicker-month").text
            yer = self.driver.find_element(By.CLASS_NAME, "ui-datepicker-year").text

        for r in range(1, 6):
            for c in range(1, 8):
                v = self.driver.find_element(By.XPATH, f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{r}]/td[{c}]')
                if v.text == str(DD):
                    self.driver.find_element(By.XPATH, f'//*[@id="ui-datepicker-div"]/table/tbody/tr[{r}]/td[{c}]').click()