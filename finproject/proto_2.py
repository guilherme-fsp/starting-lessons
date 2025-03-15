import yfinance as yf
import sys
import requests
from biblioteca import chaves

def fetch_data(ticker_symbol):
    try:#(1)
        ticker = yf.Ticker(ticker_symbol + ".SA")
        info = ticker.info
        return info
    except requests.exceptions.HTTPError as e: #(1)
        sys.exit(1)#(1)


def search_data():
    user_text = input("Insira código da ação B3: ").strip().upper()
    dados = fetch_data(user_text)
    if 'longName' not in dados: #pequenos ajustes (1)
        print('Codigo errado encerrando programa:')
        sys.exit(1)#(1)
        
    if not dados:
        print("Código inválido")
        return {}, user_text
    
    dict_chaves = chaves()

    user_select = input("Insira variavel para visualização: ").strip()

    if not user_select:
        print("Dado requisitado inexistente.")
        return {}, user_text
    
    matching_keys = [k for k, v in dict_chaves.items() if v == user_select]

    if matching_keys:
        print("\n Dados coletados")
        for chave in matching_keys:
            valor = dados.get(chave, 'N/A')
            print(f"{chave} ({user_select}):  {valor}")
    else:
        print("Nenhum parametro que combine com a descrição encontrado")
    return dados, user_text
        
def save_data(dados, user_text):
    with open(f"dados_coletados_{user_text}.txt", "w", encoding="utf-8") as file:
        for chave, valor in dados.items():
            linha = f"{chave}: {valor}\n"
            file.write(linha)

if __name__ == "__main__":
    dados, user_text = search_data()
    if dados:
        save_data(dados, user_text)
