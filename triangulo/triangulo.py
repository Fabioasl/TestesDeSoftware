a = int(input("Digite o valor do lado A: "))
b = int(input("Digite o valor do lado B: "))
c = int(input("Digite o valor do lado C: "))

if (a + b > c) and (a + c > b) and (b + c > a):
    print("Os lados formam um triângulo.")
    if a == b == c:
        print("O triângulo é EQUILÁTERO.")
    elif a == b or a == c or b == c:
        print("O triângulo é ISÓSCELES.")
    else:
        print("O triângulo é ESCALENO.")
else:
    print("Os lados NÃO formam um triângulo.")
