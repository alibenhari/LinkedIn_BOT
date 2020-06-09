from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from secrets import username, password
from time import sleep



class linkedinbot():
	def __init__(self):
		self.driver = webdriver.Chrome()
	def login(self):
		self.driver.get("https://www.linkedin.com/login")

		sleep(2)

		#switch to login popup
		email_in = self.driver.find_element_by_xpath('//*[@id="username"]')
		email_in.click()
		email_in.send_keys(username)

		password_in = self.driver.find_element_by_xpath('//*[@id="password"]')
		password_in.send_keys(password)

		login_button = self.driver.find_element_by_xpath('//*[@id="app__container"]/main/div[2]/form/div[3]/button')
		login_button.click()

		#Publish your post her
		text="Bonjour les ami(e)s. Je suis à l'écoute du marché pour un rôle de Data scientist. Je suis disponible immédiatement. Merci de consulter mon profil LinkedIn pour avoir une idée sur mon parcours professionnel. Merci pour tous les gens qui m'ont souhaité bon courage dans ma recherche d'emploi."
		mypost = self.driver.find_element_by_xpath('//*[@id="ember48"]/div/div[1]/button[1]')
		mypost.click()
		self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[1]/div[1]/div[2]/div/div/div/div/div[1]').send_keys(text)
		sleep(3)
		self.driver.find_element_by_xpath('/html/body/div[4]/div/div/div[2]/div/div[2]/div[2]/button').click()



bot = linkedinbot()
bot.login()


