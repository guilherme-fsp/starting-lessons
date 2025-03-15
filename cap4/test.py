def compute_pay():
    try:
        worked_hours = float(input("Enter Hours: "))
        rate_hours = float(input("Enter Rate: "))
        return check_pay(worked_hours, rate_hours)
    except ValueError:
        print("Por favor insira um número válido")

def check_pay(worked_hours, rate_hours):    
    if worked_hours <= 40:
        pay = worked_hours * rate_hours
    else:
        pay_reg = 40 * rate_hours
        pay_ot = (worked_hours - 40) * (rate_hours * 1.5)
        pay = pay_reg + pay_ot
    print(f"Pay: {pay}")
    return pay

compute_pay()
