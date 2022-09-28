v1 = float(input('Digite um número: '))
v2 = float(input('Digite outro número: '))
print('Soma: {} + {} = {}'.format(v1, v2, v1+v2))
print('Subtração: {} - {} = {}'.format(v1, v2, v1-v2))
print('Multiplicação: {} * {} = {}'.format(v1, v2, v1*v2))
print('Divisão: {} / {} = {}'.format(v1, v2, v1/v2))
print('Potenciação: {} ** {} = {}'.format(v1, v2, v1**v2))
print('Resto da divisão: {} % {} = {}'.format(v1, v2, v1%v2))
media= (int(v1)+int(v2))/2
print('média:',media)  

a = int(input('Informe um número: '))
b = int(input('Informe outro número: '))
c = int(input('Informe outro número: '))
d = int(input('Informe outro número: '))
media = (a + b + c + d) / 4
print('Os números {} {} {} {} foram selecionados para fazer a média'.format(a, b, c, d))
print('A média é {}'.format(media))

a = 7.5 % 2
print(a)
a = int(input('Qual é o ano que você nasceu? '))
b = int(input('Qual é o ano atual? '))
idade = b - a
print('A sua idade é',b,"-",a,'é igual a',idade)

'''a = int(input('Informe um valor: '))
b = int(input('Informe outro valor: '))
soma = a + b
print('A soma entre',a,"+",b,'é igual a',soma)
#print('{} + {} = {}'.format(a, b, soma))
name = str(input('informe o seu nome: '))
cid = str(input('informe a cidade em que você mora: '))
print('O seu nome é {} e você mora em {}'.format(name, cid))'''

a = int(input('Qual é o ano que você nasceu? '))
b = int(input('Qual é o ano atual? '))
idade = b - a
print('A sua idade é',b,"-",a,'é igual a',idade)

'''a = int(input('Informe um valor: '))
b = int(input('Informe outro valor: '))
soma = a + b
print('A soma entre',a,"+",b,'é igual a',soma)
#print('{} + {} = {}'.format(a, b, soma))
name = str(input('informe o seu nome: '))
cid = str(input('informe a cidade em que você mora: '))
print('O seu nome é {} e você mora em {}'.format(name, cid))'''


a = float(input('Informe um número: '))
b = float(input('Informe outro número? '))
soma = a + b
mult = a * b
sub = a - b
divisao = a / b
resto = a % b
pot = a ** b
media = (a + b) / 2
print('A soma entre os números é {}'.format(soma))
print('A multiplicação entre os números é {}'.format(mult))
print('A subtração entre os números é {}'.format(sub))
print('A divisão entre os números é {}'.format(divisao))
print('O resto da divisão entre os números é {}'.format(resto))
print('A potênciação entre os número é {}'.format(pot))
print('A média entre os números é {}'.format(media))