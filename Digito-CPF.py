"""
Cálculo dos dois dígitos do CPF
-----
O programa irá calcular os dois últimos dígitos do CPF com base no CPF de 9 dígitos informado pelo usuário.
O CPF gerado ficará de acordo com o formato esperado pelo governo
"""

import os
import time

def firstDigit(cpf):
    firstMultiplier = 10
    firstSum = 0

    cpfBody = cpf[:9]
    
    for i in cpfBody:
        multResult = int(i) * firstMultiplier
        print(f'{int(i)} x {firstMultiplier} = {multResult}')
        firstMultiplier -= 1
        firstSum += multResult
    
    print(f'A soma dos nove dígitos do CPF é {firstSum}')

    sumMult = firstSum * 10

    print(f'O fator de 10 sobre a soma dos nove dígitos do CPF é {sumMult}')

    firstRestSum = sumMult % 11

    if (firstRestSum <= 9):
        print(f'O resto da divisão por 11 sob o fator de 10 é {firstRestSum}')
    else:
        print(f'O resto da divisão por 11 sob o fator de 10 é 0')
        firstRestSum = 0

    return firstRestSum

def secondDigit(cpf, firstRestSum):
    secondMultiplier = 11
    secondSum = 0

    cpfBody = cpf[:9] + str(firstRestSum)

    for i in cpfBody:
        multResult = int(i) * secondMultiplier
        print(f'{int(i)} x {secondMultiplier} = {multResult}')
        secondMultiplier -= 1
        secondSum += multResult

    print(f'A soma dos nove dígitos do CPF é {secondSum}')

    sumMult = secondSum * 10

    print(f'O fator de 10 sobre a soma dos dez dígitos do CPF é {sumMult}')

    secondRestSum = sumMult % 11

    if (secondRestSum <= 9):
        print(f'O resto da divisão por 11 sob o fator de 10 é {secondRestSum}')
    else:
        print(f'O resto da divisão por 11 sob o fator de 10 é 0')
        secondRestSum = 0

    return secondRestSum

while True:

    print("Digite um CPF de nove dígitos e o programa gerará os últimos dois dígitos")
    cpf = input("Digite um CPF (9 Dígitos) > ")

    if len(cpf) == 9:
        firstRestSum = firstDigit(cpf)
        secondRestSum = secondDigit(cpf, firstRestSum)
        print(f'CPF Completo --- {cpf}{str(firstRestSum)}{str(secondRestSum)}')
        time.sleep(2)

    elif len(cpf) < 9:
        print("CPF não possui os dígitos necessários: 9 dígitos")
        time.sleep(2)
        os.system("cls")
