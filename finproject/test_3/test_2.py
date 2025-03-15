import yfinance as yf

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  # Adiciona ".SA" para ações da B3
    info = ticker.info
    return info

def search_data():
    user_text = input("Digite o código B3: ").strip().upper()  # Exemplo: BBAS3
    dados = fetch_data(user_text)

    if not dados:
        print("Nenhum dado encontrado.")
        return

    chaves_desejadas = {
        'address1': 'endereço',
        'address2': 'endereço',
        'city': 'endereço'
    }

    user_select = input('Digite os parâmetros desejados separados por vírgula (ou pressione Enter para parâmetros básicos): ').strip()
    if not user_select:
        print ("\nDados Coletados com sucesso(parametros basicos):")
        for chave, descricao in chaves_desejadas.items():
            valor = dados.get(chave, 'N/A')
            print(f"{descricao}: {valor}")
    else:
        chave_correspondente = None
        for k, v in  chaves_desejadas.items():
            if v == user_select:
                chave_correspondente = k
                break
        if chave_correspondente:
            valor = dados.get(chave_correspondente, 'N/A')
            print("\nDados coletados:")
            print(f"{user_select}: {valor}")
        else:
            print("Nenhum parâmetro encontrado com essa descrição.")
   
if __name__ == "__main__":
    search_data()
