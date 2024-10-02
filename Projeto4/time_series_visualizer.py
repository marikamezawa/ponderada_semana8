import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Importar os dados
df = pd.read_csv("fcc-forum-pageviews.csv", parse_dates=["date"], index_col="date")

# Limpar os dados: Remover os 2.5% superiores e inferiores
df = df[(df["value"] >= df["value"].quantile(0.025)) & (df["value"] <= df["value"].quantile(0.975))]

def draw_line_plot():
    # Criar a figura e os eixos
    fig, ax = plt.subplots(figsize=(15, 5))
    
    # Plotar os dados
    ax.plot(df.index, df["value"], color='r', linewidth=1)
    
    # Definir o título e os rótulos
    ax.set_title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    ax.set_xlabel("Date")
    ax.set_ylabel("Page Views")
    
    # Salvar a imagem e retornar a figura
    fig.savefig("line_plot.png")
    return fig

def draw_bar_plot():
    # Copiar e modificar os dados para o gráfico de barras mensal
    df_bar = df.copy()

    # Adicionar colunas 'year' (ano) e 'month' (mês)
    df_bar['year'] = df_bar.index.year
    df_bar['month'] = df_bar.index.month_name()

    # Criar um tipo categórico para os meses para garantir a ordem correta
    months_order = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 
                    'August', 'September', 'October', 'November', 'December']
    df_bar['month'] = pd.Categorical(df_bar['month'], categories=months_order, ordered=True)

    # Agrupar por ano e mês e calcular a média de visualizações de página
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()

    # Desenhar o gráfico de barras
    fig, ax = plt.subplots(figsize=(10, 6))
    df_bar.plot(kind='bar', ax=ax)

    # Definir rótulos e título
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')
    ax.legend(title='Months')

    # Salvar a imagem e retornar a figura
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Preparar os dados para os box plots
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box["year"] = df_box["date"].dt.year
    df_box["month"] = df_box["date"].dt.strftime("%b")
    df_box["month_num"] = df_box["date"].dt.month
    
    # Ordenar por month_num para garantir a ordem correta dos meses
    df_box = df_box.sort_values("month_num")

    # Criar subplots para os box plots
    fig, ax = plt.subplots(1, 2, figsize=(15, 7))

    # Box plot por ano (Tendência)
    sns.boxplot(x="year", y="value", data=df_box, ax=ax[0])
    ax[0].set_title("Year-wise Box Plot (Trend)")
    ax[0].set_xlabel("Year")
    ax[0].set_ylabel("Page Views")

    # Box plot por mês (Sazonalidade)
    sns.boxplot(x="month", y="value", data=df_box, ax=ax[1])
    ax[1].set_title("Month-wise Box Plot (Seasonality)")
    ax[1].set_xlabel("Month")
    ax[1].set_ylabel("Page Views")

    # Salvar a imagem e retornar a figura
    fig.savefig("box_plot.png")
    return fig