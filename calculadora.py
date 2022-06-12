num1 = float(input("Introduce tu primer número: "))
num2 = float(input("Introduce tu segundo número: "))

opcion = 0
while True:
    print("""
    Dime, ¿qué quieres hacer
    
    1) Sumar los dos números
    2) Restar los dos números
    3) Multiplicar los dos números
    4) Dividir los dos números
    5) Cambiar los números elegidos
    6) Apagar calculadora
    """)
    opcion = int(input("Elige una opción: "))

    if opcion == 1:
        print(" ")
        print("Resultado: La suma de", num1, "+", num2, "es igual a", num1+num2)
    elif opcion == 2:
        print(" ")
        print("Resultado: La resta de", num1, "-", num2, "es igual a", num1-num2)
    elif opcion == 3:
        print(" ")
        print("Resultado: La multiplicación de", num1, "*", num2, "es igual a", num1*num2)
    elif opcion == 4:
        print(" ")
        print("Resultado: La división de", num1, "/", num2, "es igual a", num1/num2)
    elif opcion == 5:
        num1 = float(input("Introduce tu primer número: "))
        num2 = float(input("Introduce tu segundo número: "))
    elif opcion == 6:
        print("Gracias por usar mi calculadora de python")
        break
    else:
        print("Opción incorrecta")