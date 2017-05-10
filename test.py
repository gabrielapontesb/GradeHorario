lst = [
(4, [1, 2, 3, 4, 5, 9]),
(4, [6, 7, 8, 10, 11]),                              # Mat2  -> 4x em 6-8 e 10-11
(4, [6, 7, 8, 9, 10, 11]),                          # Port1 -> 4x em 6-11
(4, [1, 2, 3, 4, 5]),                               # Port2 -> 4x em 1-5
(2, [2, 3, 4, 6, 7, 8, 9]),                          # Geo1  -> 2x em 2-4 e 6-9 e 3x em 10-11
(3, [10, 11]),
(2, [1, 5]),                                # Geo2  -> 2x em 1,5 e 1x em 10-11
(1, [10, 11]),
(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),             # Fis   -> 2x em 1-11
(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),             # Qui   -> 2x em 1-11
(2, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),             # Bio   -> 2x em 1-11
(1, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                    # Ing   -> 1x em 1-9 e 2x em 1-11
(2, [10, 11]),
(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                   # Hist  -> 2x em 1-9 e 3x em 10-11
(3, [10, 11]),
(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                    # Art   -> 2x em 1-9
(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]),            # Soc   -> 1x em 1-11
(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]),                    # Edf   -> 2x em 1-9
(1, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])]              # Filo  -> 1x em 1-9

soma = 0
for aloc in lst:
    qtd = aloc[0]
    turmas = aloc[1]
    soma += qtd*len(turmas)

print(soma)

# import pip
# package_name='xlwt'
# pip.main(['install', package_name])

# import xlwt
# workbook = xlwt.Workbook()
# worksheet = workbook.add_sheet(u'Teste')
# worksheet.write(0, 0, u'Escrevi')
# workbook.save("Teste.xls")


