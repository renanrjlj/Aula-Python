num1 = 1
while num1 <=10:
    print(num1);
    num1 += 1;
    
#

for i in range (1,11):
    print(i);

print(" ");

#

soma = 0
num1 = 1;
while num1 <=100:
    soma += num1;
    num1 += 1;

print(soma);

#

soma = 0
for i in range(1,101):
    soma += i;
print(soma);

#

num1 = 1;
while (num1 <= 20):
    if num1 % 2 == 0:
        print(num1);
    num1 += 1;
    
#

for i in range(2,21, 2):
        print(i);

print(" ");

#inverter string não consegui

palavra = input("Escreva uma palavra: ");

palavraInvertida = "";

for letra in palavra:
    palavraInvertida = letra + palavraInvertida;
if palavra == palavraInvertida:
    print("A palavra é um palíndromo.");
else:
    print("A palavra não é um palíndromo.");
    
#ara

num1 = 1;

while num1 ** 2 <= 1000:
      num1 += 1;

print("O menor número inteiro cujo o quadrado é maior que 1000 é:", num1);

print(" ");

#

lista = ["a", "b", "c", "d", "e"];

for indice in range(len(lista)-1, -1, -1):
    print(lista[indice]);