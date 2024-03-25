def change():
    expense = 23.75
    money = 100

    print("Ingresar gasto:",expense)
    print("Dinero recibido:", money)
    print()
    print("Vuelto")
    print()
    print("Pesos:")
    print(int(money-expense))
    print("Centavos:")
    print((money - expense) - int(money-expense))
