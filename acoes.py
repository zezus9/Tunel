class acoes():

    def __init__(self,codPapel,empresa,fechamento):
        self.codPapel = codPapel
        self.empresa = empresa
        self.fechamento = fechamento

vet_acoes = []

arq_cotacoes = open('cotacoes\COTAHIST_D02032023.txt','r')
lns = arq_cotacoes.readlines()

for ln in lns:
    ativo = ln[12:24]
    empresa = ln[27:39]
    fechamento = ln[108:121].lstrip('0')
    
    if ln[24:27] == '010':
        vet_acoes.append(acoes(ativo,empresa,fechamento))

for acao in vet_acoes:
    print(acao.codPapel)