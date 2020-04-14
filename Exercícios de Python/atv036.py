import playsound

n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))

#cores
cores = {'limpa':'\033[m',
         'branco':'\033[1;30m',
         'vermelho':'\033[1;31m',
         'verde':'\033[1;32m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m',
         'ciano':'\033[1;35m',
         'roxo':'\033[1;36m'}

#calculos
media = (n1 + n2)/2

#fala
print('Tirando {} e {}, a média do aluno é {}{}{}.'.format(n1, n2, cores['roxo'],media, cores['limpa']))

print()

#condição
if media < 5:
    print('O aluno está {}REPROVADO!{}'.format(cores['vermelho'], cores['limpa']))
    playsound.playsound('Seu Madruga - Reprovado!.mp3')

elif media >= 5 and media <= 6.99:
    print('O aluno está de {}RECUPERAÇÃO!{}'.format(cores['branco'], cores['limpa']))

else:
    print('O aluno está {}APROVADO!{}'.format(cores['ciano'], cores['limpa']))
