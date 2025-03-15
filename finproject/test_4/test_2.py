import yfinance as yf
from biblioteca import chaves
import difflib

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  
    info = ticker.info
    return info

def main():
    # 1) Pergunta ao usuário o código B3
    user_text = input("Digite o código B3: ").strip().upper()
    
    # 2) Busca dados do Yahoo Finance
    dados = fetch_data(user_text)
    if not dados:
        print("Nenhum dado encontrado para esse ticker.")
        return  # Encerra a função se não encontrou nada

    # 3) Pergunta ao usuário qual dado deseja buscar no dicionário 'chaves'
    user_data_choice = input("Digite o dado da biblioteca: ").strip()

    # 4) Busca o valor correspondente no dicionário 'chaves'
    valor = chaves.get(user_data_choice)

    # 5) Verifica se encontrou algum valor
    if valor is None:
        print("Dado não encontrado no dicionário 'chaves'.")
    else:
        print(f"Dado encontrado: {valor}")

if __name__ == "__main__":
    main()
