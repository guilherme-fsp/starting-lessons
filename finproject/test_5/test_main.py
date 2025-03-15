import yfinance as yf
from biblioteca import chaves

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")
    info = ticker.info
    return info

def search_data():
    user_text = input("Digite o código B3: ").strip().upper()  # Ex: BBAS3
    dados = fetch_data(user_text)

    if not dados:
        print("Nenhum dado encontrado.")
        return
    dict_chaves = chaves()

    user_select = input('Digite a descrição desejada (ex: "endereço"): ').strip()

    # Se o usuário não digitou nada, você pode tratar esse caso
    if not user_select:
        print("Você não digitou nenhuma descrição.")
        return

    # Procurar todas as chaves que tenham o valor igual a user_select
    matching_keys = [k for k, v in dict_chaves.items() if v == user_select]

    if matching_keys:
        print("\nDados coletados:")
        # Agora iteramos sobre todas as chaves encontradas
        for chave in matching_keys:
            valor = dados.get(chave, 'N/A')
            # Aqui imprimimos tanto a chave quanto o valor. 
            # Se quiser apenas o valor, pode omitir o nome da chave e user_select tbm.
            print(f"{chave} ({user_select}): {valor}")
    else:
        print("Nenhum parâmetro encontrado com essa descrição.")

if __name__ == "__main__":
    search_data()
