from selenium.webdriver.support.ui import Select
from PageObjects.Page_Objects import Objects
from Utilities.Logger import LogGenerator
from Utilities.Read_Excel_File import Read_Excel_File


class Test_Automation:
    log = LogGenerator.getLog()

    def test_Automation_Testing_Practice(self, setup):
        self.log.info("Automation Testing Practice Test is Started")
        self.driver = setup
        self.log.info("Invoking Browser And Opening URL")
        o = Objects(self.driver)
        r = Read_Excel_File()

        for i in range(6, 10):
            o.enter_name(r.read_excel(i, 5))
            self.log.info(f"Entring Name as: {r.read_excel(i, 5)}")
            if i == 6:
                r.write_excel(i, 9, "Pass")
                self.driver.implicitly_wait(2)
            else:
                r.write_excel(i, 9, "Fail")
                self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Name-{i}.png")
                r.write_excel(i, 10, f"Image::Name-{i}")
                self.driver.implicitly_wait(2)

        for k in range(10, 12):
            o.enter_email(r.read_excel(k, 5))
            self.log.info(f"Entring Email as: {r.read_excel(k, 5)}")
            if k == 10:
                r.write_excel(k, 9, "Pass")
                self.driver.implicitly_wait(2)
            else:
                r.write_excel(k, 9, "Fail")
                self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Email-{k}.png")
                r.write_excel(k, 10, f"Image::Email-{k}")
                self.driver.implicitly_wait(2)

        for j in range(12, 14):
            o.enter_phone(r.read_excel(j, 5))
            self.log.info(f"Entring Phone as: {r.read_excel(j, 5)}")
            if j == 12:
                r.write_excel(j, 9, "Pass")
                self.driver.implicitly_wait(2)
            else:
                r.write_excel(j, 9, "Fail")
                self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Phone-{j}.png")
                r.write_excel(j, 10, f"Image::Phone-{j}")
                self.driver.implicitly_wait(2)

        for l in range(14, 16):
            o.enter_address(r.read_excel(l, 5))
            self.log.info(f"Entring Address as: {r.read_excel(l, 5)}")
            if l == 14:
                r.write_excel(l, 9, "Pass")
                self.driver.implicitly_wait(2)
            else:
                r.write_excel(l, 9, "Fail")
                self.driver.get_screenshot_as_file(f"C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Address-{l}.png")
                r.write_excel(l, 10, f"Image::Address-{l}")
                self.driver.implicitly_wait(2)

        ele = self.driver.find_element(*Objects.saturday)
        self.driver.execute_script("arguments[0].scrollIntoView();", ele)
        o.click_male()
        self.log.info("Clicking on Male Opction")
        r.write_excel(16, 9, "Pass")

        o.click_sunday()
        o.click_monday()
        o.click_tuesday()
        o.click_friday()
        o.click_saturday()
        self.log.info("Clicking on 'Sunday, Munday,Tuesday,Friday,Saturday' Opctions")
        self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Clicked Days.png")
        r.write_excel(17, 9, "Pass")

        cuntry = Select(self.driver.find_element(*Objects.country))
        cuntry.select_by_value(r.read_excel(18, 5))
        self.log.info(f"Selected Country is: {r.read_excel(18, 5)}")
        r.write_excel(18, 9, "Pass")

        clrs = Select(self.driver.find_element(*Objects.colors))
        clrs.select_by_index(2)
        self.log.info("Selected Colour is: Green")
        r.write_excel(19, 9, "Pass")
        self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Selected Country & Colour.png")

        el = self.driver.find_element(*Objects.date_picker)
        self.driver.execute_script("arguments[0].scrollIntoView();", el)
        o.select_date(r.read_excel(20, 5), str(r.read_excel(21, 5)), r.read_excel(22, 5))
        self.log.info(f"Select Date is: {r.read_excel(20, 5)}-{r.read_excel(21, 5)}-{r.read_excel(22, 5)}")
        self.driver.get_screenshot_as_file("C:\\Users\\Tejas\\Automation Testing Practice\\Screenshots\\Date.png")
        r.write_excel(20, 9, "Pass")

        self.log.info("Automation Testing Practice Test is Completed")

# pytest --html="C:\\Users\\Tejas\\Automation Testing Practice\\Reports\\All_Reports.html" -rA
