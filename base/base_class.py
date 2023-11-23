import datetime


class Base():

    def __init__(self, driver):
        self.driver = driver

    """Method get current url - возврат нашей юрл"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print("Current url " + get_url)

    """Method assert word - проверка по слову"""

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print("Good value word")

    """Method screenshot - скрин"""

    def get_screenshot(self):
        new_date = datetime.datetime.utcnow().strftime("%Y,%m,%d,%H,%M,%S")
        name_screenshot = 'screenshot' + new_date + '.png'
        self.driver.save_screenshot('D:\\Мои проекты и тестирование\\Тестирование\\Новая папка\\Smoke-test\\screen\\' + name_screenshot)

    """Method assert url - проверка юрл"""
    def assert_url(self, result):
        get_url = self.driver.current_url
        assert get_url == result
        print("Good value URL")