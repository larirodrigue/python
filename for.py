'''num = int(input("Digite um número: "))
for contador in range(0, 11, 1):
    print(num, "x", contador,"=",(contador*num))'''

'''for num in range(100, 201, 2):
        print(num)'''

'''for num in range(200, 147, -3):
    print(num)'''

'''palavra = input("digite uma palavra: ")
x = 0
for letra in palavra:
    print(x, "-", letra)
    x = x + 1'''


'''compra_confirmada = True
dados_compra = "Compra ok"
for enviar in range(3):
    if compra_confirmada:
        print(dados_compra)
        print("Detalhes enviado por email")
        break
    else:
        print("Falha na compra")'''

'''x = int(input("digite um numero: "))
n = 1
while n <+10:
    print(f'{x} x {n} = {x*n}')
    n += 1
print(n)'''


'''gasto = int(input("Coloque o valor que você pode gastar: "))
while gasto >= 0:
    somaprod = int(input("Informe o valor do produto adquirido: "))
    print(f'{gasto} - {somaprod} = {gasto-somaprod}')
    gasto -= somaprod
print("Acabou")'''


'''tabuada = 1
numero = 1
while tabuada <= 10:
    print(f'{tabuada} x {numero} = {tabuada * numero}')
    numero += 1
    if numero == 11:
        numero = 1
        tabuada += 1
        print("\n")'''


'''verba, compra = 1000, 0
while compra <= verba:
    compra = compra + float(input("informe o preço do produto: "))
print("Despesa total = ", compra)'''


verba, compra = 999, 0
while compra <= verba:
    compra =  compra + float(input('informe o preço do produto: '))
print('Despesa total = ', compra)