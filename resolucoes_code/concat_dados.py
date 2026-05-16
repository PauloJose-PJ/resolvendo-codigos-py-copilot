# Vamos pedir duas informações diferentes ao usuário
# O input() serve para capturar dados digitados no teclado

info1 = input("Digite a primeira informação: ")

# Aqui armazenamos a segunda informação digitada pelo usuário
info2 = input("Digite a segunda informação: ")


# Concatenação significa juntar textos
# O operador + é usado para unir as strings
# " " adiciona um espaço entre as palavras para não ficarem grudadas

info_concatenada = info1 + " " + info2


# Exibe o resultado final na tela
# print() é usado para mostrar informações ao usuário

print("As informações concatenadas são:", info_concatenada)