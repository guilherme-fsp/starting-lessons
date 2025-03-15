import yfinance as yf
from biblioteca import chaves
import difflib

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  
    info = ticker.info
    return info

def tick_choice():
    user_text = input("Digite o código B3: ").strip().upper()
    dados = fetch_data(user_text)
    
    if dados:
        print("\nDados coletados:")
        for chave, valor in dados.items():
            print(f"{chave} : {valor}")
            
    else:
        print("Nenhum dado encontrado.")
    return chave, valor

# Interação usuário
if __name__ == "__main__":
    user_text = input("Digite o código B3: ")
    dados = fetch_data(user_text)
    user_data_choice = input ("Digite o dado da biblioteca: ")



fetch_data()
tick_choice()