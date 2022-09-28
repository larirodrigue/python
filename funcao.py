'''def somar(a,b):
    resultado = a + b
    print('O resultado da soma é: ',resultado)


x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
somar(x, y)

def dividir(a, b=2):
    resultado = a / b
    print("O resultado da divisão é: ", resultado)



x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
dividir(x, y)


x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
somar(x)
dividir(x, y)


def somar(a, b):
    return a + b


def dividir(a, b=2):
    resultado = a / b
    print("O resultado da divisão é: ", resultado)


x = float(input("Digite um número: "))
y = float(input("Digite um número: "))
w = somar(x, y)
print("O valor de w é: ", {w})
print(somar(x, y))
#dividir(x, y)
'''''


'''def conta(a):
    return a

def gor(a):
    return a * 0.1

x = float(input('Digite o valor da conta: ' ))

conta(x)
gor(x)

print('O valor total da conta é ',conta(x),'e a gorjeta é ',gor(x))
'''


'''
def e(b):
    a = b * b
    return a
    
    
a = 10
e(a)
e(a)
print(e(a))
'''

'''

def num(a,b,c):
    return a,b,c


x = a + a

str(input('In'))

'''


'''
def valor(a,b,c):
    return a+b+c


x = int(input('Informe um valor: '))
y = int(input('Informe um valor: '))
z = int(input('Informe um valor: '))
valor(x,y,z)
print('A soma é',valor(x,y,z))
'''

'''
def soma(n):
  num = 1
  for i in range(3,n+1 ,2):
    num = num + 1
    print(num, '/', i)


n = int(input('Informe um número: '))
print(soma(n))
'''
'''
variacao = range(10,51,2)
soma = 0
for i in variacao:
  soma += i
  print(str(i)+"+")
print("soma resultado: "+str(soma))
print("resultado divido por 21: "+str(soma/21))
'''

num = int(input("Digite um numero inteiro: "));

for i in range(1, num + 1, 1):
    print(str(i) * i);






