vel = float(input('Qual é a sua velocidade atual do carro?'))
mut = float(vel-80)*7
if vel>80:
    print("\033[1;31mMUTADO!\033[m \033[33mVocê excedeu o limite de velocidade que é de 80Km/h.\nVocê foi mutado em R${:.2f}\033[m".format(mut))
print('\033[1;36mTenha um bom dia. Dirija com cuidado!')
