#consulta API Banco Central - link: https://dadosabertos.bcb.gov.br/dataset?res_format=API
#video explicativo utilizado: https://www.youtube.com/watch?v=GGkUt4hy0T8

#perguntar quantos dos últimos registros quer trazer
QtdeRegistros = int(input('Quantos registros quer trazer? '))

#import da biblioteca utilizada para fazer consultas à APIs
import requests

#gravado o link da API em uma variável e obtido os dados com o .get e gravado em outra variavel com o tipo json
link = f'https://olinda.bcb.gov.br/olinda/servico/mecir_dinheiro_em_circulacao/versao/v1/odata/informacoes_diarias?$top={QtdeRegistros}&$orderby=Data%20desc&$format=json'
requisicao = requests.get(link)
inf = requisicao.json()

#importado biblioteca que formata melhor o _print_ do json
import pprint
# -pprint.pprint(inf)-

#import
import pandas as pd

tabela = pd.DataFrame(inf['value'])

#formatação das colunas
tabela['Quantidade'] = tabela['Quantidade'].map('{:,}'.format)
tabela['Valor'] = tabela['Valor'].map('R${:,.2f}'.format)

print(tabela)