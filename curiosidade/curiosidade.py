import PySimpleGUI as sg

# Exemplo de dicionário
chaves_desejadas = {
    'address1': 'endereço',
    'address2': 'endereço2',
    'city': 'endereço3'
}

# Extrai as descrições (valores) do dicionário
opcoes = list(set(chaves_desejadas.values()))

layout = [
    [sg.Text("Selecione uma descrição:")],
    [sg.Combo(opcoes, key='-OPCAO-', size=(20,1))],
    [sg.Button("Ok"), sg.Button("Cancelar")]
]

window = sg.Window("Seleção por Drop-down", layout)

while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == "Cancelar":
        break
    if event == "Ok":
        descricao_selecionada = values['-OPCAO-']
        # Acha todas as chaves que tenham esse valor
        chaves_encontradas = [k for k, v in chaves_desejadas.items() if v == descricao_selecionada]
        sg.popup(f"Você selecionou: {descricao_selecionada}\nChaves correspondentes: {', '.join(chaves_encontradas)}")
window.close()
