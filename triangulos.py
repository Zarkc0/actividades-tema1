def triangulos():
    print("Ingrese los lados del triángulo:")
    a = float(input("Lado a: "))
    b = float(input("Lado b: "))
    c = float(input("Lado c: "))
    if a == b == c:
        print("El triángulo es equilátero.")
    elif a == b or b == c or a == c:
        print("El triángulo es isósceles.")
    else:
        print("El triángulo es escaleno.")
triangulos()