import random
import string

tamanho = int(input("Digite o tamanho da Senha que você deseja: ")) #tamanho da senha Damm

#objeto que ira receber as estruturas das enhas que serão geradas
chars = string.ascii_letters + string.digits + '!@#$%&*()-=+§~^'

rnd = random.SystemRandom() #os.urandom,ela gera numeros aleatorios apartir de fontes fornecidas pelo S.O

# rnd.choice = gera uma lista de caracteres randomicos
#chars = ele ira passar um caracter de cada vez e digito também
print(''.join((rnd.choice(chars) for i in range(tamanho))))
