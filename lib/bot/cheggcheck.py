from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from datetime import datetime as dt

path = r"C:\firefoxdriver\geckodriver.exe"

class QuestionBot:
    def __init__(self, path, username, mail_address):
        self.start = dt.now()
        options = Options()
        options.headless = True
        self.path = path
        self.browser = webdriver.Firefox(options = options, executable_path=path)
        self.site_link = "https://techlacarte.com/how-to-get-chegg-answers-for-free/"
        self.browser.get(self.site_link)
        self.refresh_browser()
        self.username = username
        self.mail_address = mail_address

    def refresh_browser(self):
        self.browser.refresh()

    def x_path(self):
        username_xpath = '//*[@id="wpforms-13116-field_1"]'
        mail_xpath = '//*[@id="wpforms-13116-field_2"]'
        question_xpath = '//*[@id="wpforms-13116-field_4"]'
        submit_xpath = '//*[@id="wpforms-submit-13116"]'
        self.user = self.browser.find_element_by_xpath(username_xpath)
        self.mail = self.browser.find_element_by_xpath(mail_xpath)
        self.question = self.browser.find_element_by_xpath(question_xpath)
        self.submit = self.browser.find_element_by_xpath(submit_xpath)

    def main(self,question_link):
        self.x_path()
        self.user.send_keys(self.username)
        self.mail.send_keys(self.mail_address)
        self.question.send_keys(question_link)
        self.submit.click()
        self.browser.quit()
        print(dt.now()-self.start)


if __name__ == "__main__":
    question_link = "https://www.chegg.com/homework-help/questions-and-answers/label-type-different-types-protons-write-splitting-patterns-approximate-chemical-shifts-si-q37931799?trackid=afa3d0d1fce8&strackid=caf4009efa92"

    username = "User"
    mail_address = "mail"
    bot = QuestionBot(path, username, mail_address)
    bot.main(question_link)