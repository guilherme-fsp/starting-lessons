from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def fetch_status_data_selenium():
    # Configurar o caminho para o Chromedriver (substitua pelo caminho correto no seu sistema)
    service = Service("C:/chromedriver-win64/chromedriver.exe")  # Atualize este caminho!
    options = Options()
    options.add_argument("--headless")  # Para rodar sem abrir o navegador (opcional)
    options.add_argument("--disable-gpu")  # Melhora a compatibilidade em alguns sistemas
    options.add_argument("--no-sandbox")  # Necessário em alguns ambientes Linux

    # Inicializa o driver do Chrome
    driver = webdriver.Chrome(service=service, options=options)
    try:
        # URL base
        url = 'https://finance.yahoo.com/quote/'
        user_text = input("Digite o código B3: ")  # Exemplo: BBAS3
        last_url = '.SA/key-statistics/'
        final_url = url + user_text + last_url

        # Acessa a página
        print(f"Acessando a URL: {final_url}")
        driver.get(final_url)

        # Aguarda o carregamento completo
        driver.implicitly_wait(10)  # Ajuste o tempo de espera se necessário

        # Captura o HTML renderizado
        html = driver.page_source
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
        # Inspecione o HTML carregado (opcional para debug)
        # print(soup.prettify())

        # Processa os dados da página
        dados = library_data(soup)
        print("\nDados coletados:")
        for nome, valor in dados.items():
            print(f"{nome}: {valor}")
            print(soup.prettify())
