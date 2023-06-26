#Aula 4
frase = "Olá mundo!"

nome = input("Nome: ");
sobreNome = input("SobreNome: ");
print(nome);
print();

print(f"Seja bem-vindo, {nome} {sobreNome}!")
#pode ser feito também desse jeito: print("Bem-vindo{}".format(nome));

#Concatenando strings
print("Concatenando strings: ");
outraFrase = "Bem-vindo ";
fraseCompleta = frase + ' ' + outraFrase;
print(fraseCompleta);
print();

#Tamanho da string
tamanho = len(frase);
print("Tamanho: ", tamanho);
print();

#Divindo uma string em sub strings
print("Divindo a string ");
palavras = fraseCompleta.split();

#Substituindo partes das string
print(palavras);
novaFrase = frase.replace("mundo" , "Python");
print(novaFrase);
print();

#Convertendo para letras maiúsculas e minúsculas
print("Convertendo para letras maiúsculas e minúsculas:");
print("Maiúsculas: ", frase.upper());
print("Minúsculas: ", frase.lower());