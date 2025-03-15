from selenium import webdriver
from selenium.webdriver.chrome.service import Service

# Caminho do Chromedriver
service = Service("C:/chrome-win64/chrome.exe")  # Atualize conforme necessário

# Configuração do navegador
driver = webdriver.Chrome(service=service)

# Teste acessando o Google
driver.get("https://www.google.com")
print("Título da página:", driver.title)

driver.quit()