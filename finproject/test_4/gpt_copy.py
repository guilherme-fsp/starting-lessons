import yfinance as yf

def fetch_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")
    info = ticker.info
    return info

def search_data():
    user_text = input("Digite o código B3: ").strip().upper()  # Exemplo: BBAS3
    dados = fetch_data(user_text)

    if not dados:
        print("Nenhum dado encontrado.")
        return

    # Definindo o dicionário chaves_desejadas: {chave_tecnica: descricao_amigavel}
    chaves_desejadas = {
        'address1': 'endereço',
        'address2': 'endereço2',
        'city': 'endereço3'
    }

    user_select = input('Digite a descrição desejada (ou pressione Enter para parâmetros básicos): ').strip()

    if not user_select:
        # Se o usuário não digitou nada, imprime todos os parâmetros básicos
        print("\nDados coletados (parâmetros básicos):")
        for chave, descricao in chaves_desejadas.items():
            valor = dados.get(chave, 'N/A')
            print(f"{descricao}: {valor}")
    else:
        # Se o usuário digitou uma descrição, procurar a chave correspondente
        chave_correspondente = None
        for k, v in chaves_desejadas.items():
            if v == user_select:
                chave_correspondente = k
                break

        if chave_correspondente:
            # Encontrou a chave correspondente
            valor = dados.get(chave_correspondente, 'N/A')
            print("\nDados coletados:")
            print(f"{user_select}: {valor}")
        else:
            print("Nenhum parâmetro encontrado com essa descrição.")

if __name__ == "__main__":
    search_data()
