def tarifa():
    edad = int(input("Ingrese su edad: "))
    if edad < 12:
        print("La tarifa es: $50")
    elif edad >= 12 and edad <= 17:
        print("La tarifa es: $80")
    elif edad >= 18:
         print("La tarifa es: $120")
tarifa()
