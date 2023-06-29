listaFrutas = ["maca", "banana", "laranja", "abacaxi" "melancia"];
print(listaFrutas);

listaFrutas.append("uva");
print(listaFrutas);

frutaRemovida = listaFrutas.remove("uva");
print(listaFrutas);

print(listaFrutas[1]);
fruta_selecionada = (listaFrutas[1]);
print(fruta_selecionada);

#Tuplas
tuplaCores = ("vermelho","azul","verde","amarelo","roxo");
print(tuplaCores);

print(tuplaCores[2]);
cor_selecionada = (tuplaCores[2]);
print(cor_selecionada);

#aqui eu chutei o comando utilizando como exemplo a lista de frutas, mas eu sei que tuplas são imutáveis, por isso não dá para adicionar.
#E eu não sei fazer para rodar o arquivo todo mesmo dando erro a partir daqui.
#tuplaCores.append("laranja");
#print(tuplaCores);

#Dicionario
dicionarioAluno = {
  'nome': 'José', 
  'idade' : 21,
  'cidade': "RJ"
};
print(dicionarioAluno);

idade_aluno = dicionarioAluno["idade"];
print(idade_aluno);

dicionarioAluno["gênero"] = "Masculino";
print(dicionarioAluno);

dicionarioAluno.pop("cidade");
print(dicionarioAluno);
