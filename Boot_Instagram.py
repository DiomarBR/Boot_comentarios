from selenium import webdriver
import time
import random
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By




class BotInstagram(): 
    
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = webdriver.Chrome(executable_path="chromedriver.exe")
    def login(self):
        driver = self.driver
        driver.get("https://www.instagram.com/")
        time.sleep(2)
        #//input[@name="username"]
        #//input[@name="password"]
        user = driver.find_element_by_xpath('//input[@name="username"]')
        user.click()
        user.clear()
        user.send_keys(self.username)
        senha = driver.find_element_by_xpath('//input[@name="password"]')
        senha.click()
        senha.send_keys(self.password)
        senha.send_keys(Keys.RETURN)
        time.sleep(5)
        self.comentar_nas_fotos('ClyMzh4ujkU')
        
        @staticmethod
        def digite_como_pessoa(frase, ondedigitar):
            for letra in frase:
                ondedigitar.send_keys(letra)
                time.sleep(random.randint(1,5)/30)
                
    def comentar_nas_fotos(self, continuacao):
        driver = self.driver
        driver.get('https://www.instagram.com/p/'+ continuacao +'/')
        time.sleep(5)
        
        try:
            comentario = ["@diomar_goncalve"]
            cp_comentario = driver.find_element_by_class_name('x1i0vuye xvbhtw8 x76ihet xwmqs3e x112ta8 xxxdfa6 x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 x1bq4at4 xaqnwrm xs3hnx8').click()
            cp_comentario = driver.find_element_by_class_name('x1i0vuye xvbhtw8 x76ihet xwmqs3e x112ta8 xxxdfa6 x5n08af x78zum5 x1iyjqo2 x1qlqyl8 x1d6elog xlk1fp6 x1a2a7pz xexx8yu x4uap5 x18d9i69 xkhd6sd xtt52l0 xnalus7 x1bq4at4 xaqnwrm xs3hnx8')
            time.sleep(random.randint(2,10))
            self.digite_como_pessoa(random.choice(comentario),cp_comentario)
            time.sleep(random.randint(30,150))
        except Exception as e:
            print(e)
    
                
                
ComentariosBot = BotInstagram('diomar_goncalve','Diomar02012')
ComentariosBot.login()
























# navegador.find_element("xpath", '//*[@id="loginForm"]/div/div[1]/div/label/input').send_keys("diomarbr4@gmail.com")

# navegador.find_element("xpath", '//*[@id="loginForm"]/div/div[2]/div/label/input').send_keys("Diomar02012")

# navegador.find_element("xpath", '//*[@id="loginForm"]/div/div[3]').click()
# time.sleep(5)

# navegador.find_element(By.CSS_SELECTOR, "_ab8w  _ab94 _ab99 _ab9f _ab9m _ab9p  _abcj _abcm").click()


