#Exemplo de programa que aborda o tipo de dadno numero em Python

#Operações matemáticas
num1 = 10;
num2 = 5;

soma = num1 + num2;
subtracao = num1 - num2;
mutiplicacao = num1 * num2;
divisao = num1 / num2;
resto = num1 % num2;
potencia = num1 ** num2;

print("Operações básicas de matemática: ");
print("soma: ", soma);
print("subtração: ", subtracao);
print("mutiplicação: ", mutiplicacao);
print("divisão: ", divisao);    
print("resto: ", resto);
print("potência: ", potencia);

#Arredondamento de número
numeroFloat = 3.14;
numeroArredondado = round(numeroFloat);
print("Arredondamento: ", numeroArredondado);

#Funções matemáticas da biblioteca math
import math;
num = 4.7;
print("Funções matemáticas: ");
print("Valor absoluto: ", abs(-4.7));
print("Arredondamento para cima", math.ceil(num));
print("Arredondamento para baixo", math.floor(num)); 

#Geração números aleatórios
import random;
print("Números aleatórios: ");
print("Números aleatórios de 1 a 10:", random.randint(1, 10));
print("Número float aleatório entre 0 e 1", random.random());

#Formatação de números
numeroFormatado = 1234.56789;
print("Formatação de números: ");
print(f"Números com 2 casas decimais {numeroFormatado:.2f}");
print("Número formatado co m2 casas decimais {:.2f}".format(numeroFormatado));










