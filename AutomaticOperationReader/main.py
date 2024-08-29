op = str(input('Type your operation: \n'))

# Apenas para fins de checagem
sinais = ['+', '-', '/', '*', '**', '√', '(', ')', '#']
numeros = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Vai Separar todos os caracteres em espaços '8 + 8 * 9'
op1 = ' '.join(op)

# Vai pegar esses caracteres e botá-los em uma lista
op2 = op1.split()
op2.append('#') 

print(op2)

i2 = 0
e2 = i2
s1 = 1
concat = []

# Junta os números > 9

while i2 != len(op2) - 1:

  if i2 == 'x':
    i2 += 1
    continue

  elif op2[i2] in sinais:

    i2 += 1

  elif op2[i2 + 1] in sinais and op2[i2 - 1] in sinais:

    i2 += 1

  elif op2[i2 + 1] in numeros:

    while op2[i2] in numeros:
      concat.append(op2[i2])
      del op2[i2]

    op2.insert(i2, 'x')

    concat2 = ''.join(map(str, concat))

    op2.insert(op2.index('x'), concat2)
    del op2[op2.index('x')]

    concat = []

# Transforma tudo em número e ignora os sinais

i = 0

while i <= len(op2) - 1:

  if op2[i] in sinais:
    i += 1
    continue

  op2.insert(i, int(op2[i]))
  del op2[i + 1]
  i += 1
  print(op2)

del op2[op2.index('#')]

# Brackets Checker


def ParenteChecker():

  if '(' and ')' in op2:
    print('\n\033[33mInitiating parenthesis calculator...\033[m\n')
    
    while True:

      ParenteIndex1 = int(op2.index('('))
      ParenteIndex2 = int(op2.index(')'))

      global opP
      opP = op2[ParenteIndex1:ParenteIndex2]

      del op2[(ParenteIndex1 + 1):ParenteIndex2]

      ParenteIndex11 = int(opP.index('('))
      del opP[ParenteIndex11]

      OpCheckerP = 0

      while len(opP) != 1:

        if '*' in opP or '/' in opP:

          while '*' in opP or '/' in opP:

            if opP[OpCheckerP] not in sinais:
              OpCheckerP += 1
              continue

            if opP[OpCheckerP] == '*':
              OpCheckerP = 0
              MultiCheckerP()

            if opP[OpCheckerP] == '/':
              OpCheckerP = 0
              DivCheckerP()

            OpCheckerP += 1

        if '+' in opP or '-' in opP:

          while '+' in opP or '-' in opP:

            if opP[OpCheckerP] not in sinais:
              OpCheckerP += 1
              continue

            if opP[OpCheckerP] == '+':
              OpCheckerP = 0
              SumCheckerP()

            if opP[OpCheckerP] == '-':
              OpCheckerP = 0
              SubCheckerP()

            OpCheckerP += 1

      resultP = int(opP[0])

      ParenteIndex12 = int(op2.index('('))
      op2.insert(ParenteIndex12, resultP)

      ParenteIndex12 = int(op2.index('('))
      del op2[ParenteIndex12]

      ParenteIndex22 = int(op2.index(')'))
      del op2[ParenteIndex22]

      print('\n\033[33mExiting parenthesis calculator...\033[m\n')

      print(op2)
      
      
      break


# Multiplication Checker


def MultiChecker():

  if '*' in op2:

    MultiCount = int(op2.index('*'))

    resultMulti = (op2[MultiCount - 1]) * (op2[MultiCount + 1])
    del op2[MultiCount + 1]
    del op2[MultiCount - 1]

    op2.insert(MultiCount, resultMulti)

    MultiCount = int(op2.index('*'))

    del op2[MultiCount]

    print(op2)


#  Multiplication Checker on Brackets


def MultiCheckerP():

  if '*' in opP:

    MultiCountP = int(opP.index('*'))

    resultMultiP = (opP[MultiCountP - 1]) * (opP[MultiCountP + 1])
    del opP[MultiCountP + 1]
    del opP[MultiCountP - 1]

    opP.insert(MultiCountP, resultMultiP)

    MultiCountP = int(opP.index('*'))

    del opP[MultiCountP]

    print(opP)


# Division Checker


def DivChecker():

  if '/' in op2:

    DivCount = int(op2.index('/'))

    resultDiv = (op2[DivCount - 1]) / (op2[DivCount + 1])
    del op2[DivCount + 1]
    del op2[DivCount - 1]

    op2.insert(DivCount, resultDiv)

    DivCount = int(op2.index('/'))

    del op2[DivCount]

    print(op2)


# Division Checker on Brackets


def DivCheckerP():

  if '/' in opP:

    DivCountP = int(opP.index('/'))

    resultDivP = (opP[DivCountP - 1]) / (opP[DivCountP + 1])
    del opP[DivCountP + 1]
    del opP[DivCountP - 1]

    opP.insert(DivCountP, resultDivP)

    DivCountP = int(opP.index('/'))

    del opP[DivCountP]

    print(opP)


# Sum Checker


def SumChecker():

  if '+' in op2:

    SumCount = int(op2.index('+'))

    resultSum = (op2[SumCount - 1]) + (op2[SumCount + 1])
    del op2[SumCount + 1]
    del op2[SumCount - 1]

    op2.insert(SumCount, resultSum)

    SumCount = int(op2.index('+'))

    del op2[SumCount]

    print(op2)


# Sum Checker on Brackets


def SumCheckerP():

  if '+' in opP:

    SumCountP = int(opP.index('+'))

    resultSumP = (opP[SumCountP - 1]) + (opP[SumCountP + 1])
    del opP[SumCountP + 1]
    del opP[SumCountP - 1]

    opP.insert(SumCountP, resultSumP)

    SumCountP = int(opP.index('+'))

    del opP[SumCountP]

    print(opP)


# Sub Checker


def SubChecker():

  if '-' in op2:

    SubCount = int(op2.index('-'))

    resultSub = (op2[SubCount - 1]) - (op2[SubCount + 1])
    del op2[SubCount + 1]
    del op2[SubCount - 1]

    op2.insert(SubCount, resultSub)

    SubCount = int(op2.index('-'))

    del op2[SubCount]

    print(op2)


# Sub Checker on brackets


def SubCheckerP():

  if '-' in opP:

    SubCountP = int(opP.index('-'))

    resultSubP = (opP[SubCountP - 1]) - (opP[SubCountP + 1])
    del opP[SubCountP + 1]
    del opP[SubCountP - 1]

    opP.insert(SubCountP, resultSubP)

    SubCountP = int(opP.index('-'))

    del opP[SubCountP]

    print(opP)


# Ordem das operações

ParenteChecker()

# Identifica se existe * ou / no lista, se identificar, vai resolve-los primeiro

# Após essa verificação, checamos se + ou - estão na lista, caso existam, vão
# ser resolvidos. Caso não, cabou a conta.

OpChecker = 0

while len(op2) != 1:

  if '*' in op2 or '/' in op2:

    while '*' in op2 or '/' in op2:

      if op2[OpChecker] not in sinais:
        OpChecker += 1
        continue

      if op2[OpChecker] == '*':
        OpChecker = 0
        MultiChecker()

      if op2[OpChecker] == '/':
        OpChecker = 0
        DivChecker()

      OpChecker += 1

  if '+' in op2 or '-' in op2:

    while '+' in op2 or '-' in op2:

      if op2[OpChecker] not in sinais:
        OpChecker += 1
        continue

      if op2[OpChecker] == '+':
        OpChecker = 0
        SumChecker()

      if op2[OpChecker] == '-':
        OpChecker = 0
        SubChecker()

      OpChecker += 1

# Prints final result

print(f'\nThe result of \033[33m{op}\033[m is \033[4;36m{op2[0]}\033[m!')

# Espero que tenham gostado! Esse é um dos meu primeiros programas,
# então pode estar CHEIO de erros, mas eu aprendi muito com esse projeto
# e ansioso para os próximos.

# Feito por Nicolas Sousa - ThanatosPXL
