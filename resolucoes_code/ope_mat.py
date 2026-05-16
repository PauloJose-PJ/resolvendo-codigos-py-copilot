# ============================================
# CALCULADORA SIMPLES EM PYTHON
# ============================================

# O programa solicita dois números ao usuário
# e depois pergunta qual operação matemática
# deve ser realizada entre eles.

# input() recebe um valor digitado pelo usuário.
# int() converte o texto digitado para número inteiro.
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

# Aqui o usuário escolhe qual operação deseja fazer.
# O valor digitado será armazenado na variável "operacao".
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# Estrutura condicional:
# Verifica qual operação foi escolhida.

# Se a operação for soma
if operacao == "+":
    # Soma os dois números e exibe o resultado
    print(num1 + num2)

# Se a operação for subtração
elif operacao == "-":
    # abs() transforma o resultado em valor positivo.
    # Exemplo:
    # abs(-10) = 10
    print(abs(num1 - num2))

# Se a operação for multiplicação
elif operacao == "*":
    # Multiplica os números
    print(num1 * num2)

# Se a operação for divisão
elif operacao == "/":
    # Divide o primeiro número pelo segundo
    print(num1 / num2)

# Caso o usuário digite uma operação inválida
else:
    # Exibe mensagem de erro
    print("Operação invalida")