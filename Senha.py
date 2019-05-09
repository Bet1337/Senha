import random#Bibilioteca python para escolher números aleatórios
print('''Regras:
        1. Você deve inserir 5 digitos com números de 0 a 9
        2. Se o dígito está contido na senha mas não está na mesma posição o programa irá apresentar o valor 0 (zero);
        3. Se o dígito não está na senha o programa vai apresentar o valor -1 (menos um);
        4. Se o dígito está contido na senha e está na mesma posição o programa irá apresentar o valor +1 (mais um);
        5. Você tera 10 chances para acertar a senha.

         Boa sorte!!!''')
print()

senha=""
n=0
#Estrutura de Repetição utilizada para o sorteio da senha
while n<5:
    sorteio= random.randint(0,9)
    senha= senha + str(sorteio)
    n+=1
####################################################
claudio=0
while claudio<10:#while principal que vai definir o número máximo de jogadas que o jogador pode fazer 
    user= str(input("Por favor insira um senha de 5 dígitos\ncontendo os números inteiro de 0 a 9:"))
    cont=""
    while len(user)>len(senha) or len(user)<len(senha):#Estrutura de repetição que serve para ver se o número inserido pelo usuário é válido
        user=str(input("Por favor insira um senha de 5 dígitos\ncontendo os números inteiro de 0 a 9:"))
    if senha==user:#Define quando o usuário ganha o jogo, quebrando o a estrutura de repetição
        print("Parabéns vc acaba de ganhar um suspiro!!")
        print("11111")
        break
    #Sequência de Decisão que verfica se o número pertence e está no local correto, se ele pertence mas esta no local errado ou se ele não pertence a senha
    else:
        if user[0][0]==senha[0][0]:
            cont+="1"
        elif user[0][0]==senha[1][0] or user[0][0]==senha[2][0] or user[0][0]==senha[3][0] or user[0][0]==senha[4][0]:
            cont+="0"
        else:
            cont+="-1"


        if user[1][0]==senha[1][0]:
            cont+="1"
        elif user[1][0]==senha[0][0] or user[1][0]==senha[2][0] or user[1][0]==senha[3][0] or user[1][0]==senha[4][0]:
            cont+="0"
        else:
            cont+="-1"

        if user[2][0]==senha[2][0]:
            cont+="1"
        elif user[2][0]==senha[1][0] or user[2][0]==senha[0][0] or user[2][0]==senha[3][0] or user[2][0]==senha[4][0]:
            cont+="0"
        else:
            cont+="-1"


        if user[3][0]==senha[3][0]:
            cont+="1"
        elif user[3][0]==senha[1][0] or user[3][0]==senha[2][0] or user[3][0]==senha[0][0] or user[3][0]==senha[4][0]:
            cont+="0"
        else:
            cont+="-1"


        if user[4][0]==senha[4][0]:
            cont+="1"
        elif user[4][0]==senha[1][0] or user[4][0]==senha[2][0] or user[4][0]==senha[3][0] or user[4][0]==senha[0][0]:
            cont+="0"
        else:
            cont+="-1"


        print(cont)#print o quão proximo ou longe o usuário está de acertar
        claudio+=1
        if claudio==10:
            print("Você perdeu tente outra vez!!")

