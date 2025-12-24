import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from anticaptchaofficial.recaptchav2proxyless import recaptchaV2Proxyless
import undetected_chromedriver as uc
import os
from dotenv import load_dotenv

# Configuração do WebDriver com undetected_chromedriver
driver = uc.Chrome(use_subprocess=True)

load_dotenv() # Carrega o arquivo .env
api_key = os.getenv("API_KEY")

try:
    link = "https://google.com/recaptcha/api2/demo"
    driver.get(link)

    # Espera explícita para garantir que o elemento carregou antes de tentar pegar a key
    sitekey_element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, 'recaptcha-demo'))
    )
    key_captcha = sitekey_element.get_attribute('data-sitekey')

    print(f"SiteKey encontrada: {key_captcha}")

    # Configuração do AntiCaptcha
    solver = recaptchaV2Proxyless()
    solver.set_verbose(1)
    solver.set_key(api_key)
    solver.set_website_url(link)
    solver.set_website_key(key_captcha)

    # Tentativa de resolução
    print("Iniciando resolução do Captcha...")
    response = solver.solve_and_return_solution()

    if response != 0:
        print(f"Captcha resolvido! Token: {response}")
        
        # 1. Injeta o token no campo oculto do recatpcha
        driver.execute_script(f"document.getElementById('g-recaptcha-response').innerHTML='{response}';")
        
        # 2. Em alguns sites, é necessário chamar a função de callback também.
        # No demo do Google não precisa, mas se precisasse seria algo como:
        # driver.execute_script(f"___grecaptcha_cfg.clients[0].aa.l.callback('{response}')")

        # 3. Clica no botão de envio
        submit_button = driver.find_element(By.ID, 'recaptcha-demo-submit')
        submit_button.click()
        
        print("Formulário enviado com sucesso.")
        
        # Pausa para você ver o resultado visualmente antes de fechar
        time.sleep(5) 
        
    else:
        print(f"Erro ao resolver: {solver.err_string}")

except Exception as e:
    print(f"Ocorreu um erro durante a execução: {e}")

finally:
    # Garante que o navegador feche mesmo se der erro
    driver.quit()