import requests
from bs4 import BeautifulSoup

def fetch_status_data():
    status_url = 'https://statusinvest.com.br/acoes/'
    user_text = input("Digite o codigo B3: ")
    full_url = status_url + user_text

    try:
        response = requests.get(full_url)

        if response.status_code == 200:
            soup = BeautifulSoup(response.text, 'html.parser')

            dy_element = soup.find('div', class_='info')

            if dy_element:
                dy_text = dy_element.text.strip()
                print(f"Dividend Yeld (DY) do ativo {user_text}: {dy_text}")
            else:
                print("Não foi possível encontrar os dados de DY.")
        else:
            print(f"Erro ao acessar a pagina: {response.status_code}")
    except Exception as e:
        print(f"Ocorreu um erro {e}")
if __name__ == "__main__":
    fetch_status_data()