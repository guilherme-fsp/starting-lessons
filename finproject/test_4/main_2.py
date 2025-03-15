import yfinance as yf
from biblioteca import chaves
import difflib

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  
    info = ticker.info
    return info

def chaves_invertidas():
    comercial = chaves()  # chama sua função que retorna o dicionário
    invertido = {}
    for k, v in comercial.items():
        # Aqui cada valor (v) pode mapear para várias chaves. Vamos juntar numa lista:
        invertido.setdefault(v, []).append(k)
    return invertido

def main():
    
    user_text = input("Digite o codigo B3: ").strip().upper()

    dados = fetch_data(user_text)
    if not dados:
        print("Nenhum dado encontrado")
        return

    dict_chaves=chaves()
    user_data_choice = input("Digite o dado da biblioteca: ").strip()
    string_corresp = dict_chaves.get(user_data_choice)
    valor = dados.get(chaves, 'N/A')
    

    if string_corresp is None:
        print("Dado não encontrado na biblioteca")
    else:
        print(f"Dado encontrado: {string_corresp} : {valor}")

if __name__ == "__main__":
    main()
