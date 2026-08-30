def calificaciones():
    calif = float(input("Ingrese la calificación numérica: "))
    if calif >= 90 and calif <= 100:
        print("La calificación es: A")
    elif calif >= 80 and calif < 89:
        print("La calificación es: B")
    elif calif >= 70 and calif < 79:
        print("La calificación es: C")
    elif calif >= 60 and calif < 69:
        print("La calificación es: D")
    else:
        print("La calificación es: F")

calificaciones()
