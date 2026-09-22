print("triaje de paciente y asignacion de color")
temperatura = float(input("ingrese la temperatura"))
frecuencia = int(input(" ingrese la frecuencia"))
saturacion = int(input("ingrese la saturacion de oxigeno"))

print(f"temperatura: {temperatura}, frecuencia: {frecuencia}, saturacion_de_oxigeno: {saturacion}")

if frecuencia >120 or saturacion <90:
    print("asignar color rojo")

elif temperatura >= 39:
    print("asignar color amarillo")

else:
    print("asignar color verde")