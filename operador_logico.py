entrada = input("[E]ntrar [S]air: ")
senha_digitada = input('Senha: ')

senha_permitida = '123456'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrar')

elif not senha_digitada:
    print('Não digitou a senha')

else:
    print('Sair')

print('3' in senha_permitida) #a ordem importa vai dar false se for 31 por exemplo
print('9' in senha_permitida)
