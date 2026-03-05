print("=== CALCULADORA BÁSICA ===")

num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

print("1. Sumar")
print("2. Restar")

opcion = input("Seleccione una opción: ")

if opcion == "1":
    print("Resultado:", num1 + num2)
elif opcion == "2":
    print("Resultado:", num1 - num2)
else:
    print("Opción inválida")
