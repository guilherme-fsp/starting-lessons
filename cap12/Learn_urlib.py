import urllib.request

# URL da página que você deseja acessar
url = "https://www.globo.com"

try:
    # Envia a solicitação HTTP
    response = urllib.request.urlopen(url)

    # Lê o conteúdo da página
    content = response.read()

    # Decodifica o conteúdo em texto (usando UTF-8 como padrão)
    print(content.decode('utf-8'))

except Exception as e:
    print(f"Erro ao acessar a página: {e}")