import configparser

data = configparser.RawConfigParser()
data.read("C:\\Users\\Tejas\\Automation Testing Practice\\Configuration\\Config.ini")


class Read_Confi_File:

    @staticmethod
    def get_URL():
        UL = data.get("Automation_Testing_Practice", "URL")
        return UL

    @staticmethod
    def get_Excel_Path():
        Path = data.get("Automation_Testing_Practice", "Excel_Path")
        return Path