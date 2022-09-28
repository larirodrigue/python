'''a = float(input('Informe a altura do triângulo: '))
b = float(input('Informe a base: '))
area = (b * a) / 2
print('A área é ',area)'''

'''for num in range(200, 147, -3):
    print(num)'''

'''palavra = input("digite uma palavra: ")
x = 0
for letra in palavra:
    print(x, "-", letra)
    x = x + 1'''

'''é para ir em 1 em 1 lado esquedo
 n+n se colocar 4 é pra começar no 4
 para ir em 2 em 2'''
'''def soma(n):
    num = 1
    for i in range(1, n + n, 2):
        num = num + 1

        print(num, '/', i)



n = int(input('Informe um número: '))
print(soma(n))'''

'''a = str(input('Digite uma letra: '))
if a == 'a' or a == 'e' or a == 'i' or a == 'o' or a == 'u':
    print('Você digitou uma vogal')
else:
    print('Você digitou uma consoante')'''

'''
v = int(input('Informe a quantidade de hora trabalhada: '))
h = v * 5
var = h <= 220
sin = h * 0.97
if h <= 900:
    print('isento')
elif h <= 1500:
    sin = 1500 * 0.05
    a = 1500 - fgts
    print('Seu salário é ',a)
elif h <=2500:
    sin = 1500 * 0.10
    a = 1500 - fgts
    print('Seu salário é ',a)
else:
    sin = 1500 * 0.20
    a = 1500 - fgts
    print('Seu salário é ',a)
'''
'''def dia_semana(dia):
    match dia:
        case 1:
            return 'Domingo'
        case 2:
            return 'Segunda'
        case 3:
            return 'Terça'
        case 4:
            return 'Quarta'
        case 5:
            return 'Quinta'
        case 6:
            return 'Sexta'
        case 7:
            return 'Sabado'
        case _:
            return "valor {} inválido".format(dia)

dia = int(input('Qual é o dia da semana: '))
print(dia_semana(dia))'''


'''
x = int(input('Informe um número: '))
y = int(input('Informe um outro número: '))
z = int(input('Informe mais um número:  '))



if (x > (y + z) or (y > (x + z) or (z > (y + x)))):
    print("Não pode ser um triangulo")
elif ((x == y != z) or (x == z != y) or (y == z != x)):
    print("Isóceles (possui 2 lados iguais)")
elif ((x == y == z)):
    print("Equilátero (possui todos os lados iguais)")
elif ((x != y != z)):
    print("Escaleno (não possui nenhum lado igual)")'''






