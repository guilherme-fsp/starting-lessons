import requests
from bs4 import BeautifulSoup

# URL da página
url = 'https://statusinvest.com.br/acoes/bbas3'

# Cabeçalhos para simular um navegador
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}

# Fazendo a requisição
response = requests.get(url, headers=headers)

if response.status_code == 200:
    # Parse do HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extraindo "Preço médio"
    preco_medio = soup.find('span', {'data-item': 'unitValue_F'}).text.strip()
    print(f"Preço médio: {preco_medio}")

    # Extraindo "Preço atual"
    preco_atual = soup.find('span', {'data-item': 'price_F'}).text.strip()
    print(f"Preço atual: {preco_atual}")

    # Extraindo "Variação HOJE"
    variacao_hoje = soup.find('span', {'data-item': 'variation_F'}).text.strip()
    print(f"Variação HOJE: {variacao_hoje}%")

    # Extraindo "Variação total"
    variacao_total = soup.find('span', {'data-item': 'profitabilityPercent_F'}).text.strip()
    print(f"Variação total: {variacao_total}%")

    # Extraindo "Patrimônio"
    patrimonio = soup.find('span', {'data-item': 'currentValue_F'}).text.strip()
    print(f"Patrimônio: {patrimonio}")
    
    #Extraindo dividendo -> Extraiu valor atual
    dividend_yeld = soup.find('strong', {'class': 'value'})
    if dividend_yeld:
        print(f"Variação total: {dividend_yeld.text.strip()}%")
    else:
        print("Dividendo nao encontrado")    

else:
    print(f"Erro ao acessar a página: {response.status_code}")
