print("Validación de Email")
print("Introduzca su email")
email = input()
#if (email.find("@") == -1):
if (email.count("@") == 0):
    print("No existe @ en el email")
elif (email.find(".") == -1):
    print("El email no tiene .")
elif(email.startswith("@") or email.endswith("@")):
    print("@ al inicio o al final")
elif (email.find("@") != email.rfind("@")):
    print("Existe mas de una @")
elif (email.rfind(".") < email.find("@")):
    print("Debe existir un punto despues de la @")
else:
    ultimoPunto = email.rfind(".")
    dominio = email[ultimoPunto + 1:]
    longDominio = len(dominio)
    if (longDominio >= 2 and longDominio <= 3):
        print("Email correcto")
    else:
        print("El dominio debe ser de 2 a 4 caracteres")
print("Fin de programa")
