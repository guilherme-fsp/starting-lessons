import yfinance as yf

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  # Adiciona ".SA" para ações da B3
    info = ticker.info
    return info



def search_data():
    user_text = input("Digite o código B3: ")  # Exemplo: BBAS3
    dados = fetch_data(user_text)
    user_select = input('Digite os parâmetros desejados: ') #depois, quer selecionar os parametros? se sim, .... / se nao... "parametros basicos".

  
    if dados:

        print("\nDados coletados:")
        chaves_desejadas = [{user_select}]
        for chave in chaves_desejadas:
            valor = dados.get(chaves_desejadas,'N/A')
            print(f"{chave}: {valor}")
            #return chave,valor
                

    else:
        print("Nenhum dado encontrado.")

if __name__ == "__main__":
    search_data()