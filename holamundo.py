print("<3")
print("Hola mundo")

print(":(")


num1 = 5
num2 = 7
sum = num1 + num2
print (sum)

# Función para convertir Celsius a Fahrenheit
def celsius_a_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Pedir al usuario que ingrese los grados Celsius
celsius = float(input("Ingrese la temperatura en grados Celsius: "))

# Convertir la temperatura y mostrar el resultado
fahrenheit = celsius_a_fahrenheit(celsius)
print(f"{celsius} grados Celsius son {fahrenheit} grados Fahrenheit.")


print("nevits")

print("atisopom")

print("daniel lore")

print(".....")

# Función para verificar si un número es par o impar
def es_par_o_impar(numero):
    if numero % 2 == 0:
        return "par"
    else:
        return "impar"

# Pedir al usuario que ingrese un número
numero = int(input("Ingrese un número: "))

# Verificar y mostrar el resultado
resultado = es_par_o_impar(numero)
print(f"El número {numero} es {resultado}.")