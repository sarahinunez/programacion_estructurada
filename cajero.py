

def comprobar(valor):
    if valor % 50 == 0:
        print("Es valido")
        monto_es_mayor(valor)

    else:
        print("No valido")

def monto_es_mayor(valor):
    if valor < 6000:
        print("Saldo suficiente ")
    else:
        print("Saldo insuficiente ")

saldo = 6000

e = 0
while (True):
    monto = int(input("ingrese un monto; "))
    comprobar(monto)
    saldo = saldo - monto
    e +=monto

    print(saldo)
    print(e)

    if e >= 6000:
        print("limite diario excedido")
        break
    else:
        print("retiro exitoso y entregado")



# e se uso para el monto

