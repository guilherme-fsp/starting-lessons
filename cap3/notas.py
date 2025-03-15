try:
    get_score = float(input("Insira nota: "))
       
    if get_score >= 0.9:
        print("A")
    elif get_score >= 0.8:
        print("B")
    elif get_score >= 0.7:
        print("C")
    elif get_score >= 0.6:
        print("D")
    else:
        print("F")
except:
    print("ERRO")