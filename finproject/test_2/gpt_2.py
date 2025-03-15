from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium_stealth import stealth
from bs4 import BeautifulSoup

def fetch_status_data_selenium():
    # Atualize o caminho para o Chromedriver
    service = Service("C:/chromedriver-win64/chromedriver.exe")  # Atualize este caminho!
    options = Options()
    # options.add_argument("--headless")  # Desative o modo headless para depuração
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    options.add_argument("--disable-extensions")
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--allow-running-insecure-content')
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                         "AppleWebKit/537.36 (KHTML, like Gecko) "
                         "Chrome/114.0.5735.90 Safari/537.36")

    driver = webdriver.Chrome(service=service, options=options)
    try:
        url = 'https://finance.yahoo.com/quote/'
        user_text = input("Digite o código B3: ")  # Exemplo: BBAS3
        last_url = '.SA/key-statistics/'
        final_url = url + user_text + last_url

        print(f"Acessando a URL: {final_url}")
        driver.get(final_url)

        # Aumenta o tempo de espera
        wait = WebDriverWait(driver, 30)

        # Verifica se o corpo da página está presente
        wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))

        # Salva o HTML para depuração
        html = driver.page_source
        with open('pagina_carregada.html', 'w', encoding='utf-8') as f:
            f.write(html)

        soup = BeautifulSoup(html, 'html.parser')
        return soup
    finally:
        driver.quit()

def library_data(soup):
    if not soup:
        return {}

    # Encontrar os dados na página
    data_range = soup.find_all('td')
    cabecalhos = soup.find_all('th')
    dados = {}

    # Associa cabeçalhos e valores
    for i in range(len(cabecalhos)):
        nome = cabecalhos[i].text.strip()
        valor = data_range[i].text.strip() if i < len(data_range) else 'N/A'
        dados[nome] = valor

    return dados
if __name__ == "__main__":
    soup = fetch_status_data_selenium()

    if soup:
        # Processa os dados da página
        dados = library_data(soup)
        print("\nDados coletados:")
        for nome, valor in dados.items():
            print(f"{nome}: {valor}")
