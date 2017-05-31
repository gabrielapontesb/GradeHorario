from random import randint
import xlwt

def main():
    lstHorarios = criarHorarios()
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

    grade = criarGrade(lstHorarios, lstAlocacoes, matriz)
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


def criarGrade(lstHorarios, lstAlocacoes, matriz):

    dicProfessorDia = {}

    for alocacao in lstAlocacoes:
        id_prof = alocacao[0]
        qtd_aulas = alocacao[2]
        turmas = alocacao[3]

        for turma in turmas:
            print("--------------------------------------------------")
            print(str(qtd_aulas) + " ALOCACOES PARA O PROF " + str(id_prof) + " NA TURMA " + str(turma))
            chave = (id_prof, turma)

            # Dicionario que relaciona o prof ao dia que ele esta alocado
            if chave not in dicProfessorDia.keys():
                dicProfessorDia[chave] = []

            i = 0
            while i < qtd_aulas:

                dia = randint(1, 5)  # sorteando o dia
                print("dia: " + str(dia))
                alocar(id_prof, qtd_aulas, turma, matriz, dicProfessorDia, lstHorarios, chave, dia)
                i += 1

    return matriz


def alocar(id_prof, qtd_aulas, turma, matriz, dicProfessorDia, lstHorarios, chave, dia):

        if dia not in dicProfessorDia[chave]: #se o professor nao der aula naquele dia
            dicProfessorDia[chave].append(dia)

            horario = sortearHorario(dia) #sorteando o horario

            if matriz[horario][turma-1] == -1: #se o horario daquele dia estiver vago, aloca
                matriz[horario][turma-1] = id_prof
                print("alocado no horario:" + str(horario))
                print()

            else: #se nao estiver, procura o proximo horario
                print("conflito com o professor: " + str(matriz[horario][turma-1]) + " no horario " + str(horario))
                procurarProximoHorario(horario, turma, id_prof, matriz, dicProfessorDia, lstHorarios, chave)


        else: #se o professor ja der aula, procurar proximo dia
            print("conflito de dia")

            if dia == 5:
                proximo_dia = procurarProximoDia(dicProfessorDia, chave, 0)
            else:
                proximo_dia = procurarProximoDia(dicProfessorDia, chave, dia)

            print("proximo dia: " + str(proximo_dia))
            alocar(id_prof, qtd_aulas, turma, matriz, dicProfessorDia, lstHorarios, chave, proximo_dia)

        print()



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

    proximo = dia + 1

    while (proximo <= 5):
        if proximo not in dicProfessorDia[chave]:
            return proximo

        else:
            proximo += 1

            if proximo > 5:
                proximo = 1


#cada vez que ele encontrar um proximo, tem que ver se o prof ja nao possui aula naquele dia
def procurarProximoHorario(horario, turma, id_prof, matriz, dicProfessorDia, lstHorarios, chave):

    if horario == 24:
        proximo = 0
    else:
        proximo = horario + 1

    while (proximo <= 24):
        if matriz[proximo][turma-1] == -1:

            print("proximo horario vago: " + str(proximo))
            #se tiver vazio o proximo, verificar se o cara ja nao da aula naquele dia
            possui = verificaProfPossuiAulaNoDia(dicProfessorDia, lstHorarios, proximo, chave)

            if possui == False:
                print("o prof nao possui aula nesse dia")
                matriz[proximo][turma-1] = id_prof
                print("alocado no horario: " + str(proximo))
                break

            else:

                dia_corresp = CorrespondeDiaHorario(horario, lstHorarios)
                print("o prof possui aula nesse dia: " + str(dia_corresp))
                prox_dia = procurarProximoDia(dicProfessorDia, chave, dia_corresp)
                proximo = lstHorarios[prox_dia-1][0] #primeiro horario do outro dia

                print("proximo dia: " + str(prox_dia) + " horario: " + str(proximo))

        else:
            proximo += 1



def CorrespondeDiaHorario(horario, lstHorarios):
    for i in range(len(lstHorarios)):
        if horario in lstHorarios[i]:
            return i

def verificaProfPossuiAulaNoDia(dicProfessorDia, lstHorarios, horario, chave):

    # dado um horario, ver a qual dia ele pertence e verificar se o professor ja da aula nesse dia
    possui = False

    dia = CorrespondeDiaHorario(horario, lstHorarios)
    if dia+1 in dicProfessorDia[chave]:
        possui = True

    return possui


def imprimeMatriz(matriz):

    for i in range(25):
        for j in range(11):
            print(matriz[i][j], end=" ")
        print()


def criarExcel(matriz):
    workbook = xlwt.Workbook()
    worksheet = workbook.add_sheet(u'GradeHorario')

    for i in range(25):
        for j in range(11):
            worksheet.write(i,j, matriz[i][j])

    workbook.save("GradeHorario-geminada.xls")

main()