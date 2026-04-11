#ELE NÃO QUER SALVAR ESSA PORRA COM OS COMENTARIOS, ENTÃO VAI FICAR ASSIM MESMO
# beecrowd | 1020

idade_em_dias = int(input())
ano = idade_em_dias // 365
idade_em_dias = idade_em_dias % 365
mes = idade_em_dias // 30
idade_em_dias = idade_em_dias % 30
print(f"{ano} ano(s)")
print(f"{mes} mes(es)")
print(f"{idade_em_dias} dia(s)")