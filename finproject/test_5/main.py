import yfinance as yf
from biblioteca import chaves
import difflib

#count = 0 #-> Contagem de parametros
def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  
    info = ticker.info
    return info

if __name__ == "__main__":

    user_text = input("Digite o código B3: ")
    dados = fetch_data(user_text)
    
    if dados:
        print("\nDados coletados:")
        for chave, valor in dados.items():
            #count = count + 1 #-> Contagem de parametros
            print(f"{chave} : {valor}")
        #print(count) #-> Contagem de parametros

            
    else:
        print("Nenhum dado encontrado.")