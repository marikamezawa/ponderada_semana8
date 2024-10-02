import pandas as pd  # Importa a biblioteca pandas para manipulação de dados
import matplotlib.pyplot as plt  # Importa a biblioteca matplotlib para visualização de dados
from scipy.stats import linregress  # Importa a função linregress para realizar regressão linear

def draw_plot():
    # Carrega os dados do arquivo CSV
    df = pd.read_csv('epa-sea-level.csv')
    
    # Cria um gráfico de dispersão
    plt.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])
    
    # Calcula a linha de melhor ajuste para todo o conjunto de dados
    slope, intercept, r_value, p_value, std_err = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years = pd.Series([i for i in range(1880, 2051)])  # Gera uma série de anos de 1880 a 2050
    plt.plot(years, intercept + slope * years, label='Fit line: 1880-2050', color='blue')  # Plota a linha de ajuste

    # Calcula a linha de melhor ajuste para os dados de 2000 até o ano mais recente
    recent_df = df[df['Year'] >= 2000]  # Filtra os dados a partir de 2000
    slope_recent, intercept_recent, _, _, _ = linregress(recent_df['Year'], recent_df['CSIRO Adjusted Sea Level'])
    recent_years = pd.Series([i for i in range(2000, 2051)])  # Gera uma série de anos de 2000 a 2050
    plt.plot(recent_years, intercept_recent + slope_recent * recent_years, label='Fit line: 2000-2050', color='green')  # Plota a linha de ajuste recente

    # Adiciona rótulos e título ao gráfico
    plt.xlabel('Year')  # Rótulo do eixo x
    plt.ylabel('Sea Level (inches)')  # Rótulo do eixo y
    plt.title('Rise in Sea Level')  # Título do gráfico
    plt.legend()  # Adiciona a legenda
    
    # Salva o gráfico como uma imagem PNG
    plt.savefig('sea_level_plot.png')
    
    return plt.gca()  # Retorna o objeto do eixo atual

import sea_level_predictor  # Importa o módulo que contém a função de plotagem

# Chama a função para gerar o gráfico
sea_level_predictor.draw_plot()

import unittest  # Importa a biblioteca unittest para testes
import sea_level_predictor  # Importa novamente o módulo para testar
import matplotlib as mpl  # Importa a biblioteca matplotlib
import numpy as np  # Importa a biblioteca NumPy

# Caso de teste para o gráfico
class LinePlotTestCase(unittest.TestCase):
    def setUp(self):
        self.ax = sea_level_predictor.draw_plot()  # Configura o ambiente de teste chamando a função de plotagem

    def test_plot_title(self):
        actual = self.ax.get_title()  # Obtém o título atual do gráfico
        expected = "Rise in Sea Level"  # Define o título esperado
        self.assertEqual(actual, expected)  # Verifica se o título atual é igual ao esperado

    def test_plot_labels(self):
        actual = self.ax.get_xlabel()  # Obtém o rótulo do eixo x
        expected = "Year"  # Define o rótulo esperado para o eixo x
        self.assertEqual(actual, expected)  # Verifica se o rótulo atual é igual ao esperado
        actual = self.ax.get_ylabel()  # Obtém o rótulo do eixo y
        expected = "Sea Level (inches)"  # Define o rótulo esperado para o eixo y
        self.assertEqual(actual, expected)  # Verifica se o rótulo atual é igual ao esperado

    def test_plot_lines(self):
        # Você pode adicionar verificações para os dados das linhas ou do gráfico de dispersão, se necessário
        pass

# Executa os testes se o arquivo for executado como script
if __name__ == "_main_":
    unittest.main()