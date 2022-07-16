dia = int(input('Dia do seu nascimento: '))
mes = input('Mês do seu nascimento: ')

if (mes == 'março' and dia >= 21) or mes == 'abril' and dia <= 20:
    print('Áries')
if (mes == 'abril' and dia >= 21) or mes == 'maio' and dia <= 20:
    print('Touro')
if (mes == 'maio' and dia >= 21) or mes == 'junho' and dia <= 20:
    print('Gêmeos')
if (mes == 'junho' and dia >= 21) or mes == 'julho' and dia <= 22:
    print('Câncer')
if (mes == 'julho' and dia >= 23) or mes == 'agosto' and dia <= 22:
    print('Leão')
if (mes == 'agosto' and dia >= 23) or mes == 'setembro' and dia <= 22:
    print('Virgem')
if (mes == 'setembro' and dia >= 23) or mes == 'outubro' and dia <= 22:
    print('Libra')
if (mes == 'outubro' and dia >= 23) or mes == 'novembro' and dia <= 21:
    print('Escorpião')
if (mes == 'novembro' and dia >= 22) or mes == 'dezembro' and dia <= 21:
    print('Sagitário')
if (mes == 'dezembro' and dia >= 22) or mes == 'janeiro' and dia <= 20:
    print('Capricórnio')
if (mes == 'janeiro' and dia >= 21) or mes == 'fevereiro' and dia <= 18:
    print('Aquário')
if (mes == 'fevereiro' and dia >= 19) or mes == 'março' and dia <= 20:
    print('Peixes')
