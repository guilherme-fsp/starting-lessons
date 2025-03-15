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
        # Se não há dados, retorne um dicionário vazio e o user_text
        return {}, user_text
    
    dict_chaves = chaves()

    user_select = input("Insira variável para visualização: ").strip()

    if not user_select:
        print("Dado requisitado inexistente.")
        # Se o usuário não digitar nada, retorne dicionário vazio
        return {}, user_text

    matching_keys = [k for k, v in dict_chaves.items() if v == user_select]

    if matching_keys:
        print("\nDados coletados")
        for chave in matching_keys:
            valor = dados.get(chave, 'N/A')
            print(f"{chave} ({user_select}):  {valor}")
    else:
        print("Nenhum parâmetro que combine com a descrição encontrado")

    # Agora, independente do que aconteceu, retornamos 'dados' e 'user_text'
    return dados, user_text

def save_data(dados, user_text):
    # Use a f-string para inserir user_text no nome do arquivo
    with open(f"dados_coletados_{user_text}.txt", "w", encoding="utf-8") as file:
        for chave, valor in dados.items():
            linha = f"{chave}: {valor}\n"
            file.write(linha)

if __name__ == "__main__":
    dados, user_text = search_data()
    if dados:
        save_data(dados, user_text)
