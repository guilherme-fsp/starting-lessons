import requests
import re
from bs4 import BeautifulSoup

def go_to():
    url = 'https://www.statusinvest.com.br/acoes/'
    user_tick = input('Insira o tick desejado: ' )
    final_url = url + user_tick
    headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
    
    response = requests.get(final_url, headers=headers)
    if response.status_code == 200:

        soup = BeautifulSoup(response.text, 'html.parser')

        #Codigo para pegar as informaçoes
        texto = soup.find_all('strong', class_="value")
        for item in texto:
            valor = item.text.strip()
            origem = item.find_parent('div')
            sibling = item.find_next_sibling()
            if origem:
                origem_classe = origem.get('class')
                print(f"Valor origem: {valor}, veio de: {origem_classe}, valor irmão: {sibling}")
            else:
                print(f"Valor origem: {valor}, origem desconhecida, irmão {sibling} desconhecido")
            #print('DY: ', item.text.strip())

        #dividend_yeld = soup.find('strong', {'class': 'value'})
        #if dividend_yeld:
        #    print(f"Variação total: {dividend_yeld.text.strip()}%")
        #else:
         #   print("Dividendo nao encontrado")    




    else:
        print(f"Erro ao acessar a página: {response.status_code}")
        


if __name__ == "__main__":
    go_to()
