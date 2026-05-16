# Solicita ao usuário que digite uma string (texto)
# O valor digitado será armazenado na variável "string"
string = input("Digite uma string: ")

# Solicita ao usuário que digite um número inteiro
# O input sempre retorna texto, então usamos int()
# para converter o valor digitado em número inteiro
numero = int(input("Digite um número inteiro: "))

# Exibe a string repetida a quantidade de vezes informada
# (string + " ") adiciona um espaço após cada repetição
# O operador * repete a string várias vezes
print((string + " ") * numero)
