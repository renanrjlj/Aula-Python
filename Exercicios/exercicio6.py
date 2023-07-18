num1 = int(input("Digite o número: "));
num2 = int(input("Digite o outro número: "));

soma = num1 + num2;
subtracao = num1 - num2;
divisao = num1 / num2;
multiplicacao = num1 * num2;

print("O resultado da soma é: ", soma);
print("O resultado da subtração é: ", subtracao);
print("O resultado da multiplicação é: ", multiplicacao);  
print("O resultado da divisão é: ", divisao);

#2

temperatura = float(input("Digite a temperatura atual: "));
if temperatura >= 100: print("A água está fervendo!");
if temperatura <= 99: print("A água não está fervendo!");

#3

num1 = int(input("Digite um número inteiro: "));

if num1 % 2 == 0:
  print("O número digitado é par. ");
else:
    print("O número digitado é impar. ");
    
#4

senha = input("Por favor digite a sua senha: ");

senhaCorreta = "123456";

if senha == senhaCorreta:
    print("A senha está correta!");
else:
    print("A senha está incorreta!");
    
#5

idade = int(input("Digite a sua idade: "));

if (idade >= 18) and (idade <= 30):
    print("A idade está dentro do padrão!");
else:
    print("A idade não está dentro do padrão!");
    
#6

print("Por favor, digite 3 números abaixo para verificar se um ou mais deles é verdadeiro.")
num1 = int(input("Primeiro número: "));
num2 = int(input("Segundo número: "));
num3 = int(input("Terceiro número: "));

if (num1 >0) or (num2 >0) or (num3>0):
  print("Um ou mais números são positivos!");
elif (num1 == 0) and (num2 == 0) and (num3 == 0):
   print("Todos os números são iguais a zero!");
else:
    print("Os números são negativos!");
    
#7

letra = input("Favor digitar uma letra: ");

if (letra == "a") or (letra == "e") or (letra == "i") or (letra == "o") or (letra == "u"):
    print("A letra é uma vogal!");

else:
    print("A letra não é vogal!");
    
#8

numero = int(input("Infome o primeiro número inteiro: "));

if numero == 0:
    print("O número é zero!");
elif numero > 0:
    print("O número é positivo!");
else:
    print("O número é negativo!");
    
#9

print("Por favor, digite 3 números para verificar se estão na ordem crescente.")
num1 = float(input("Primeiro número: "));
num2 = float(input("Segundo número: "));
num3 = float(input("Terceiro número: "));

if (num1 < num2 < num3):
    print("Os números estão em ordem crescente.");
else:
    print("Os números não estão em ordem crescente.");
    
#10

num1 = int(input("Digite um número: "));

if (num1 % 3 == 0) and (num1 % 5 == 0):
    print("O número é múltiplo de 3 e 5 ao mesmo tempo.");
else:
    print("O número não é múltiplo de 3 e 5 ao mesmo tempo.");