import requests
import re
from bs4 import BeautifulSoup


def fetch_status_data():
    url = 'https://finance.yahoo.com/quote/'
    user_text = input("Digite o codigo B3: ")
    last_url = '.SA/key-statistics/'
    final_url = url + user_text  + last_url
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
        
    response = requests.get(final_url, headers=headers)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')
        return soup
    else:
         print(f"Erro ao acessar a página: {response.status_code}")
         return None

def library_data(soup):
        if not soup:
             return {}
        
        data_range = soup.find_all('td')
        cabecalhos = soup.find_all('th')
        dados = {}
        for i in range(len(cabecalhos)):
             nome = cabecalhos[i].text.strip()
             valor = data_range[i].text.strip()if i < len(data_range) else 'N/A'
             dados[nome] = valor
        return dados

if __name__ == "__main__":
    soup = fetch_status_data()

    if soup:
         dados = library_data(soup)
         print("Dados coletados:")
         for nome, valor in dados.items():
              print(f"{nome}: {valor}")
