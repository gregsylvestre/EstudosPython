#consulta API Banco Central - link: https://dadosabertos.bcb.gov.br/dataset?res_format=API
#video explicativo utilizado: https://www.youtube.com/watch?v=GGkUt4hy0T8

#import da biblioteca utilizada para fazer consultas à APIs
import requests
import pandas as pd

#registro inicial para o loop
TabelaFinal = pd.DataFrame()
ProxInd = 0

#gravado o link da API em uma variável e obtido os dados com o .get e gravado em outra variavel com o tipo json
while True:
    link = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top=10000&$skip={ProxInd}&$orderby=Data%20desc&$format=json'
    requisicao = requests.get(link)
    inf = requisicao.json()
    tabela = pd.DataFrame(inf['value'])
    if len(inf['value']) < 1:
        break
    TabelaFinal = pd.concat([TabelaFinal, tabela])
    ProxInd += 10000

#formatação das colunas
TabelaFinal['Quantidade'] = TabelaFinal['Quantidade'].map('{:,}'.format)
TabelaFinal['Valor'] = TabelaFinal['Valor'].map('R${:,.2f}'.format)

print(TabelaFinal)