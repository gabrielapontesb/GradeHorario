from random import randint
import xlwt

def main():
    lstHorarios = criarHorarios()
    lstTurmas = criarTurmas()
    lstAlocacoes = criarAlocacoes()

    matriz = [[-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1],
               [-1, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1]]

    grade = criarGrade(lstHorarios, lstTurmas, lstAlocacoes, matriz)
    imprimeMatriz(grade)
    criarExcel(grade)

    return 0


def criarHorarios():
    return [
        (0, 1, 2, 3, 4),
        (5, 6, 7, 8, 9),
        (10, 11, 12, 13, 14),
        (15, 16, 17, 18, 19),
        (20, 21, 22, 23, 24),
    ]


def criarTurmas():
    lst = []
    for i in range(11):
        lst.append(i)
    return lst


def criarAlocacoes():

    return [
        # [Professor, id, qtdAulas, [Turmas]]
        ("Mat1", 0, 4, [1, 2, 3, 4, 5, 9]),                             # Mat1 -> 4x em 1-5 e 9
        ("Mat2", 1, 4, [6, 7, 8, 10, 11]),                              # Mat2  -> 4x em 6-8 e 10-11
        ("Port1", 2, 4, [6, 7, 8, 9, 10, 11]),                          # Port1 -> 4x em 6-11
        ("Port2", 3, 4, [1, 2, 3, 4, 5]),                               # Port2 -> 4x em 1-5
        ("Geo1", 4, 2, [2, 3, 4, 6, 7, 8, 9]),                          # Geo1  -> 2x em 2-4 e 6-9 e 3x em 10-11
        ("Geo1", 4, 3, [10, 11]),
        ("Geo2", 5, 2, [1, 5]),                                         # Geo2  -> 2x em 1,5 e 1x em 10-11
        ("Geo2", 5, 1, [10, 11]),
        ("Fis", 6, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),             # Fis   -> 2x em 1-11
        ("Bio", 7, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),             # Qui   -> 2x em 1-11
        ("Qui", 8, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),             # Bio   -> 2x em 1-11
        ("Ing", 9 , 1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                    # Ing   -> 1x em 1-9 e 2x em 1-11
        ("Ing", 9, 2, [10, 11]),
        ("Hist", 10, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                   # Hist  -> 2x em 1-9 e 3x em 10-11
        ("Hist", 10, 3, [10, 11]),
        ("Art", 11, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                    # Art   -> 2x em 1-9
        ("Soc", 12, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),            # Soc   -> 1x em 1-11
        ("Edf", 13, 2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                    # Edf   -> 2x em 1-9
        ("Filo", 14, 1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])            # Filo  -> 1x em 1-11
    ]


def criarGrade(lstHorarios, lstTurmas, lstAlocacoes, matriz):

    dicProfessorDia = {}

    for alocacao in lstAlocacoes:
        id_prof = alocacao[0]
        qtd_aulas = alocacao[2]
        turmas = alocacao[3]
        for turma in turmas:
            alocar(id_prof, qtd_aulas, turma, matriz, dicProfessorDia)

    return matriz


def sortearHorario(dia):
    if dia == 1:
        return randint(0,4)
    elif dia == 2:
        return randint(5,9)
    elif dia == 3:
        return randint(10,14)
    elif dia == 4:
        return randint(15,19)
    else:
        return randint(20,24)


def procurarProximoDia(dicProfessorDia, chave, dia):

    while dia < 5:
        dia += 1
        if dia not in dicProfessorDia[chave]:
            return dia

    if dia == 5:
        dia = 0
        while dia < 5:
            dia += 1
            if dia not in dicProfessorDia[chave]:
                return dia


def alocar(id_prof, qtd_aulas, turma, matriz, dicProfessorDia):

    print(str(qtd_aulas) + " alocacoes para o prof " + str(id_prof) + " na turma " + str(turma))
    chave = (id_prof, turma)

    #Dicionario que relaciona o prof ao dia que ele esta alocado
    if chave not in dicProfessorDia.keys():
        dicProfessorDia[chave] = []

    i = 0
    while i < qtd_aulas:

        dia = randint(1,5)  #sorteando o dia
        print("dia: " + str(dia))
        if dia not in dicProfessorDia[chave]: #se o professor nao der aula naquele dia
            dicProfessorDia[chave].append(dia)
            horario = sortearHorario(dia) #pode sortear o horario
            if matriz[horario][turma-1] == -1:
                matriz[horario][turma-1] = id_prof
                print("alocado no horario:" + str(horario))
                print()

            # senão, procura o proximo horario
            else:
                print("CONFLITO COM O PROFESSOR: " + str(matriz[horario][turma-1]))
                horario = achaProximoHorario(horario, turma, id_prof, matriz)
                print("alocado no horario: " + str(horario))
                print()


        else: #se der aula, achar o proximo
            dia = procurarProximoDia(dicProfessorDia, chave, dia)
            #print("CONFLITO! próximo: " + str(dia))
            #print("alocado")
            dicProfessorDia[chave].append(dia)
            horario = sortearHorario(dia)  # pode sortear o horario
            if matriz[horario][turma-1] == -1:
                matriz[horario][turma-1] = id_prof
                print("alocado no horario:" + str(horario))
                print()

            # senão, procura o proximo horario
            else:
                print("CONFLITO COM O PROFESSOR: " + str(matriz[horario][turma-1]))
                achaProximoHorario(horario, turma, id_prof, matriz)
                print()

        print()
        i += 1

    #i = 0

    # while i < qtd_aulas:
    #     horario = randint(0, 24)
    #
    #     print("horario " + str(horario) + " e turma " + str(turma))
    #
    #     # se tiver vazio, aloca
    #     ##### VERIFICAR AULAS GEMINADAS
    #     if matriz[horario][turma-1] == -1:
    #         matriz[horario][turma-1] = id_prof
    #         print("alocado")
    #         print()
    #
    #     # senão, procura o proximo horario
    #     else:
    #         print("CONFLITO COM O PROFESSOR: " + str(matriz[horario][turma-1]))
    #         achaProximoHorario(horario, turma, id_prof, matriz)
    #         print("alocado")
    #         print()
    #
    #     i += 1


def achaProximoHorario(horario, turma, id_prof, matriz):

    proximo = horario + 1
    print("ACHANDO O PROXIMO HORARIO: " + str(proximo))

    while (proximo < 24):
        if matriz[proximo][turma-1] == -1:
            matriz[proximo][turma-1] = id_prof
            print("alocado no horario: " + str(horario))
            break
        else:
            proximo = proximo + 1

    if (proximo >= 24):
        proximo = 0
        while (proximo != 24):
            if matriz[proximo][turma-1] == -1:
                matriz[proximo][turma-1] = id_prof
                print("alocado no horario: " + str(horario))
                break
            else:
                proximo = proximo + 1

    return 0


def imprimeMatriz(matriz):

    for i in range(25):
        for j in range(11):
            print(matriz[i][j], end=" ")
        print()


def criarExcel(matriz):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(u'GradeHorario')
    # for i in range(11):
    #     for j in range(25):
    #         worksheet.write(i,j, matriz[i][j])

    for i in range(25):
        for j in range(11):
            worksheet.write(i,j, matriz[i][j])

    workbook.save("GradeHorario.xls")

main()