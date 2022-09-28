x = int(input("Digite o valor de um lado do triangulo: "))
y = int(input("Digite o valor de um lado do triangulo: "))
z = int(input("Digite o valor de um lado do triangulo: "))
maior = 0;
intermediario = 0;
menor = 0;

if ((x > y) and (x > z)):
    maior = x;
    if (y > z):
        intermediario = y;
        menor = z;
    elif (z > y):
        intermediario = z;
        menor = y;
    elif (z == y):
        intermediario = z;
        menor = z;


elif ((y > x) and (y > z)):
    maior = y;
    if ((x > z)):
        intermediario = x;
        menor = z;
    elif (z > x):
        intermediario = z;
        menor = x;
    elif (z == x):
        intermediario = x;
        menor = x;

elif ((z > x) and (z > y)):
    maior = z;
    if (x > y):
        intermediario = x;
        menor = y;
    elif (y > x):
        intermediario = y;
        menor = x;
    elif (y == x):
        intermediario = y;
        menor = y;

elif ((z < x) and (z < y)):
    menor = z;
    if (y == x):
        intermediario = y;
        menor = y;

elif ((y < x) and (y < z)):
    menor = y;
    if (x == z):
        intermediario = x;
        menor = x;

if ((x < y) and (x < z)):
    menor = x;
    if (z == y):
        intermediario = z;
        menor = z;

if (maior > (intermediario + menor)):
    print("Não pode ser um triangulo")
elif ((maior == intermediario != menor) or (maior == menor != intermediario) or (intermediario == menor != maior)):
    print("Isóceles (possui 2 lados iguais)")
elif ((maior == intermediario == menor)):
    print("Equilátero (possui todos os lados iguais)")
elif ((maior != intermediario != menor)):
    print("Escaleno (não possui nenhum lado igual)")