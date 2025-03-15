import yfinance as yf

def fetch_yfinance_data(ticker_symbol):
    ticker = yf.Ticker(ticker_symbol + ".SA")  # Adiciona ".SA" para ações da B3
    info = ticker.info
    return info

if __name__ == "__main__":
    user_text = input("Digite o código B3: ")  # Exemplo: BBAS3
    dados = fetch_yfinance_data(user_text)
    
    if dados:
        print("\nDados coletados:")
        for chave, valor in dados.items():
            print(f"{chave}: {valor}")
    else:
        print("Nenhum dado encontrado.")