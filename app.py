num1 = input("Ingrese el primer número: ")
num2 = input("Ingrese el segundo número: ")

operator = input("Ingrese la operación que desea realizar con " + num1 + " y " + num2 + "\n" +
                 "1 = suma\n" +
                 "2 = resta\n" +
                 "3 = multiplicación\n" +
                 "4 = división\n")

if num1 and num2 and operator:
    num1 = float(num1)
    num2 = float(num2)
    operator = int(operator)

    if operator == 1:
        result = num1 + num2
        print("Resultado:", result)

    elif operator == 2:
        result = num1 - num2
        print("Resultado:", result)

    elif operator == 3:
        result = num1 * num2
        print("Resultado:", result)

    elif operator == 4:
        try:
            result = num1 / num2
            print("Resultado:", result)
        except ZeroDivisionError:
            print("Error: No se puede dividir entre cero.")

    else:
        print("Error: Operador inválido. Debe ser 1, 2, 3 o 4.")

else:
    print("Error: Ambos números y la operación deben ser ingresados.")