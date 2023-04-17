def calcul(num1,operateur,num2):
    if operateur=="+":
        return num1+num2
    elif operateur=="-":
        return num1-num2
    elif operateur=="%":
        return num1%num2
    elif operateur=="/":
        return num1/num2
    else:
        return "C'est fini..."
print(calcul(70,"*",10))