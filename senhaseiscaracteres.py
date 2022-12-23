#Exercício 1. Escreva um programa que pede ao usuário uma senha de 6 caracteres. O programa deverá imprimir uma mensagem relativa ao número de caracteres da senha.

#Interação com o usuário
senha = input("Digite sua senha: ")

#Leitura de quantos caracteres tem a senha
numCarac = len(senha)

#Programa que lê a senha
if numCarac <  6:
    print("\nSenha inválida, com menos de 6 caracteres. Digite novamente.")
elif numCarac > 6: 
    print("\nSenha inválida, com mais de 6 caracteres. Digite novamente.")
else:
    print("\nSenha registrada com sucesso!")