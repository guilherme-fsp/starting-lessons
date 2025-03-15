import webbrowser
def open_status_web():
    status_url = 'https://statusinvest.com.br/acoes/'
    user_text = input("Digite o código do tick b3: ")
    full_url = status_url + user_text
    webbrowser.open(full_url)
    
def main():
    for line in open_status_web:
        if line.startswith('DY'):
            print(line)
    open_status_web()


if __name__ =="__main__":
    main()

