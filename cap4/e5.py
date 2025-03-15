def compute_pay():
    try:
        worked_hours = float(input("Enter Hours: "))
        rate_hours = float(input("Enter Rate: "))
    except ValueError:
        print("Por favor insira um número")  
        
        return   


    if worked_hours <= 40:
         pay = worked_hours * rate_hours
        
    else:
         pay_reg = 40 * rate_hours
         pay_ot = (worked_hours - 40) * (rate_hours * 1.5)
         pay = pay_reg + pay_ot
         
    print(f"Pay: {pay}")
    return pay
 


compute_pay() 
#O uso de compute_pay() no final do código é para iniciar a execução do programa.
#Quando você define funções em Python, elas não são executadas automaticamente. 
# Você precisa chamar a função para que ela seja executada.
#Aqui está o que acontece:

#Definição das Funções: Primeiro, você define as funções compute_pay e check_pay.
#Chamada da Função: Ao chamar compute_pay() no final, você está dizendo ao Python para executar essa função.
#Fluxo do Programa: A função compute_pay então solicita a entrada do usuário, chama check_pay para calcular o pagamento e imprime o resultado.
#Sem a chamada compute_pay(), o programa não faria nada além de definir as funções. É como escrever um plano de ação sem nunca colocá-lo
#em prática.





  
