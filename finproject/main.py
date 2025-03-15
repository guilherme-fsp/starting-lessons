import yfinance as yf
from biblioteca import chaves

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")
    info = ticker.info
    return info


def search_data():
    user_text = input("Insira código da ação B3: ").strip().upper()
    dados = fetch_data(user_text)

    if not dados:
        print("Código inválido")
        return
    
    dict_chaves = chaves()

    user_select = input ("Insira variavel para visualização: ").strip()

    if not user_select:
        print("Dado requisitado inexistente.")
        return
    
    matching_keys = [k for k, v in dict_chaves.items() if v == user_select]

    if matching_keys:
        print("\n Dados coletados")
        for chave in matching_keys:
            valor = dados.get(chave, 'N/A')
            print(f"{chave} ({user_select}):  {valor}")
    else:
        print("Nenhum parametro que combine com a descrição encontrado")

if __name__ == "__main__":
    search_data()