# -*- coding: utf-8 -*-
"""
autores: jose.cordovaa@codeecuador.com / aaron.parodip@codeecuador.com

ultima vez editado: 4/06/2021 15:24
"""
import random
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

# opts = Options()
# opts.add_argument("user-agent=Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
# "Ubuntu Chromium/71.0.3578.80 Chrome/71.0.3578.80 Safari/537.36")

usr = str(input("Por favor ingrese su mail\t"))
clave = str(input("Por ingrese su clave\t"))
print("Conexión exitosa")
time.sleep(2)

driver = webdriver.Chrome('./chromedriver.exe')

driver.get("https://linkedin.com") # url semilla.
time.sleep(2)

# ************ INICIA SESION **************
username = driver.find_element_by_xpath("//input[@name='session_key']")
password = driver.find_element_by_xpath("//input[@name='session_password']")

time.sleep(2)
username.send_keys(usr)

clave = open('clave.txt').readline().strip()
password.send_keys(clave)

submit = driver.find_element_by_xpath("//button[@type='submit']").click()
time.sleep(2)

n_pages = 3

# ************ Lazo for para iterar la paginacion ***********
for n in range (1,n_pages):

    driver.get("https://www.linkedin.com/search/results/people/?network=%5B%22F%22%5D&origin=FACETED_SEARCH&page=" + str(n))
    time.sleep(2)

    all_buttons = driver.find_elements_by_tag_name("button")
    message_buttons = [btn for btn in all_buttons if btn.text == "Enviar mensaje"]

    for i in range (0, len(message_buttons)):

        message_buttons[i].click()

        driver.execute_script("arguments[0].click();", message_buttons[i])
        time.sleep(2)

        main_div = driver.find_element_by_xpath("//div[starts-with(@class, 'msg-form__msg-content-container')]")
        main_div.click()
        driver.execute_script("arguments[0].click();", main_div)

        # ********* Escribe el mensaje *************
        paragraphs = driver.find_elements_by_tag_name("p")
        all_span = driver.find_elements_by_tag_name("span")
        all_span = [s for s in all_span if s.get_attribute("aria-hidden") == "true"]

        idx = [*range(1, 23, 2)]
        print(idx)
        # counter =0
        # for i in all_span:
        #     print(counter)
        #     print(i.text)
        #     counter +=1
        greetings = ["Hola", "Que tal", "Hola, Buen día"]

        all_names= []

        print()
        for j in idx:
            print(all_span[j].text.split(" "))
            name = all_span[j].text.split(" ")[0]
            all_names.append(name)
        print(all_names)

        greetings_idx = random.randint(0, len(greetings)-1)
        message = greetings[greetings_idx] + " " + all_names [i] + ", mucho gusto, por favor sigue mi página https://www.linkedin.com/company/codeecuador/?viewAsMember=true Gracias de antemano!"

        paragraphs[-5].send_keys(message)
        time.sleep(2)

        #*********** Envia el mensaje **************
        submit = driver.find_element_by_xpath("//button[@type='submit']").click()
        time.sleep(2)

        # ********** Cierra la etiqueta DIV ********
        close_button = driver.find_element_by_xpath("//button[starts-with(@data-control-name, 'overlay.close_conversation_window')]")
        driver.execute_script("arguments[0].click();", close_button)
        time.sleep(2)

