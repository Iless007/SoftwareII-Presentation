print("<3")
print("Hola mundo")
print("Hola xd")
print(":(")


num1 = 5
num2 = 7
sum = num1 + num2
print (sum)
print("nevits")

print("atisopom")

print("daniel lore")

print(".....")

def contar_palabras(texto):
    palabras = texto.split()
    return len(palabras)

def main():
    texto = input("Ingrese un texto: ")
    cantidad_palabras = contar_palabras(texto)
    print(f"La cantidad de palabras en el texto es: {cantidad_palabras}")

main()