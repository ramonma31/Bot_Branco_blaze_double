from Get_API_blaze.results_gather import Status_double, Last_Results_Double
import os

RED   = "\033[1;31m"  
BLUE  = "\033[1;34m"
CYAN  = "\033[1;36m"
GREEN = "\033[0;32m"
RESET = "\033[0;0m"
BOLD    = "\033[;1m"
REVERSE = "\033[;7m"

destrava_estrategia = False
complete = True
rolling = False
waiting = False
sinal = ''


def validador_branco():
    qtd = 0
    for cor in cores:
        if cor == 'white':
            qtd += 1
    porcentagem = qtd * 100 / 300 if qtd > 0 else 0
    return porcentagem


def resultado_rodada():

    menssagem = f'Cor: {cores[299]} Numero: {numeros[299]} Horario: {horario[299].format("HH:mm")}'
    tamanho = len(menssagem)
    
    print(' ')
    print(f'{RED}# {"-" * tamanho} #{RESET}')
    print(f'  {BLUE}{menssagem}{RESET}')
    print(f'{RED}# {"-" * tamanho} #{RESET}')
    print(' ')


def estrategia():
    global destrava_estrategia,sinal
    if numeros[299] == 6:
        horario_branco = horario[299].add(minutes=6).format('HH:mm')
        print(f'Horario para sair o branco {horario_branco}')
        destrava_estrategia = False
        sinal = horario_branco



def detecta_branco():
    global destrava_estrategia
    if cores[-1] == 'white' and validador_branco() > 7.9:
        destrava_estrategia = True
        print('Saiu um branco seu besta')


while True:
    # --TODAS AS 300 RODADAS DE CORES ANTERIORES-- #
    cores = Last_Results_Double(cor=True)

# --TODAS AS 300 RODADAS DE NUMEROS ANTERIORES-- #
    numeros = Last_Results_Double(numero=True)

# --TODAS AS 300 RODADAS DE HORARIO ANTERIORES-- #
    horario = Last_Results_Double(horario=True)

    if Status_double() == 'complete' and complete:
        os.system('cls')
        
        resultado_rodada()
        print(sinal if sinal else 'Não temos sinal')

        complete = False
        waiting = True

        detecta_branco()

        if destrava_estrategia:

            estrategia()

    elif Status_double() == 'waiting' and waiting:

        waiting = False
        rolling = True

    elif Status_double() == 'rolling' and rolling:

        rolling = False
        complete = True
