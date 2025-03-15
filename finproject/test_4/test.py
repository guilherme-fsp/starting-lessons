import yfinance as yf
from biblioteca import chaves
import difflib

def fetch_data(ticker_symbol):
    """Busca os dados do ticker informado."""
    ticker = yf.Ticker(ticker_symbol + ".SA")  
    info = ticker.info
    return info

def save_data(dados):
    """Exibe e salva os dados coletados."""
    if dados:
        print("\nDados coletados:")
        # Salva os dados em um arquivo TXT
        with open("dados_coletados.txt", "w", encoding="utf-8") as file:
            for chave, valor in dados.items():
                linha = f"{chave}: {valor}\n"
                #print(linha.strip())  # Exibe no console
                file.write(linha)    # Salva no arquivo
    else:
        print("Nenhum dado encontrado.")

def buscar_similar(chave):
    """Busca palavras similares usando difflib."""
    traducoes = chaves()
    chaves_disponiveis = traducoes.keys()
    similar = difflib.get_close_matches(chave, chaves_disponiveis, n=1)
    if similar:
        return traducoes[similar[0]]
    return "Chave não encontrada"

if __name__ == "__main__":
    # Entrada do usuário
    user_tick = input("Digite o código B3: ")
    dados = fetch_data(user_tick)
    user_data = input("Digite os dados que voce quer ver: ")
    user_input_request_data = buscar_similar(user_data)
    print(f"{dados} {user_input_request_data} ")


    # Salva os dados em um arquivo
    save_data(dados)
    buscar_similar(user_input_request_data)
