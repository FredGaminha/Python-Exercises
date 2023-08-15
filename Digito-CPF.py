#Calcule os dois últimos dígitos de seu CPF
#CPF Completo - 281.869.230-04

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

    cpfBody = cpf[:10]

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

#cpf = input("Digite um CPF (9 Dígitos) > ")
cpf = "95436481740"
firstRestSum = firstDigit(cpf)

secondRestSum = secondDigit(cpf, firstRestSum)

#print(f'CPF Selecionado --- {cpf}{str(firstRestSum)}{str(secondRestSum)}')
