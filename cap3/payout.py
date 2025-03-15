
try:
    worked_hours = float(input("Enter Hours: "))
    rate_hours = float(input("Enter Rate: "))
    
    if worked_hours <= 40:
        pay = worked_hours * rate_hours
    
    else:
        pay_reg = 40 * rate_hours
        pay_ot = (worked_hours - 40) * (rate_hours * 1.5)
        pay = pay_reg + pay_ot
        
        print(f"Pay: {pay}")
except:
    print("Por favor insira um número")
