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

#Lista
listaNumeros = [1,2,3,4,5];
listaStrings = ["e", "f", "c", "d"];
listaMista   = [1, "a", 3.14, True];
print(listaNumeros);
print(listaStrings);
print(listaMista);

frutas = ["maça", "banana", "morango"];

print(frutas[0])

frutas[1] = "laranja";
print("Tamanho 1: ", len(frutas))

frutas.append("Abacaxi");
print(frutas)

print("Tamanho 2: ",len(frutas))

listaNova = [1, ["a", "b"]];
print(listaNova[1][0]);

lista1 = [1,2,3];
lista2 = [4,5,6];

listaConcatenada = lista1 + lista2;
print(listaConcatenada);

listaRepetida = [0] * 4;
print(listaRepetida);

letras  = ["a", "b", "c", "d"];
sublista = letras[1:4];
print(sublista);

frutas = ["maça", "banana", "laranja"];
frutas.append("morango");
print(frutas);

frutas.insert(1, "abacaxi");
print(frutas);
print();
frutaRemovida = frutas.remove("banana");
frutaRemovida = frutas.pop(2);
print(frutas);
print(frutaRemovida);

frutas.sort();

print("Embaralhado: ", frutas);








