ver = 1
while ver != 0:
    numero = int(input())
    if numero != 0:
        soma_divisores = 0 
        for i in range(1,numero):
            if numero % i == 0:
                soma_divisores += i

        if soma_divisores == numero:
            print(f'{numero} é perfeito')
        else:
            print(f'{numero} não é perfeito')

    else: 
        ver = 0


 
