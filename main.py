from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv
import random
import sys

navegador = webdriver.Chrome()
navegador.get("https://www.saucedemo.com/")

with open('Login - Login.csv', 'r') as arquivo_login:
    leitor = csv.reader(arquivo_login)
    linha = list(leitor)

linha_login = random.choice(linha)
user = linha_login[0]
senha = linha_login[1]

mensagem_de_erro = {
    'locked_out_user' : "Usuário bloqueado! Tente novamente",
    'problem_user' : "Algo deu errado com o usuário! Tente novamente",
    'error_user' : "Algo deu errado com o usuário! Tente novamente"
}

if user in mensagem_de_erro:
    print(mensagem_de_erro[user])
    navegador.quit()
    sys.exit()

WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "user-name"))).send_keys(user)
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "password"))).send_keys(senha)

navegador.find_element(By.ID, "login-button").click()

WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)"))).click()
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"))).click()
WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.ID, "add-to-cart-sauce-labs-bike-light"))).click()

WebDriverWait(navegador, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "shopping_cart_badge"))).click()

navegador.find_element(By.ID, "checkout").click()

with open('Login - Cadastro.csv', 'r') as arquivo_cadastro:
    reader = csv.reader(arquivo_cadastro)
    linha_cadastro = list(reader)

cadastro_random = random.choice(linha_cadastro)
nome = cadastro_random[0]
sobrenome = cadastro_random[1]
cep = cadastro_random[2]

WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "first-name"))).send_keys(nome)
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "last-name"))).send_keys(sobrenome)
WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "postal-code"))).send_keys(cep)

navegador.find_element(By.ID, "continue").click()

WebDriverWait(navegador, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, "summary_total_label")))
elemento = navegador.find_element(By.CLASS_NAME, "summary_total_label")
total = elemento.text
print(total)

WebDriverWait(navegador, 10).until(EC.presence_of_element_located((By.ID, "finish"))).click()

navegador.quit()