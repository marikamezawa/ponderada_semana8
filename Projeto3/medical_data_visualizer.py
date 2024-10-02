import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1. Importar o arquivo medical_examination.csv
df = pd.read_csv('medical_examination.csv')

# 2. Criar a coluna overweight
df['overweight'] = (df['weight'] / (df['height'] / 100) ** 2 > 25).astype(int)

# 3. Normalizar as colunas cholesterol e gluc
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

def draw_cat_plot():
    # 5. Usar pd.melt para reformular os dados
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # 6. Agrupar os dados e contar as variáveis categóricas
    df_cat = df_cat.groupby(['cardio', 'variable', 'value']).size().reset_index(name='total')

    # 7. Usar sns.catplot() para criar o gráfico
    fig = sns.catplot(x='variable', y='total', hue='value', col='cardio', data=df_cat, kind='bar').fig

    # 8. Salvar a figura
    fig.savefig('catplot.png')
    return fig

def draw_heat_map():
    # 11. Limpar os dados
    df_heat = df[(df['ap_lo'] <= df['ap_hi']) &
                 (df['height'] >= df['height'].quantile(0.025)) &
                 (df['height'] <= df['height'].quantile(0.975)) &
                 (df['weight'] >= df['weight'].quantile(0.025)) &
                 (df['weight'] <= df['weight'].quantile(0.975))]

    # 12. Calcular a matriz de correlação
    corr = df_heat.corr()

    # 13. Gerar uma máscara para a parte superior da matriz de correlação
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # 14. Configurar a figura do matplotlib
    fig, ax = plt.subplots(figsize=(12, 8))

    # 15. Desenhar o heatmap com seaborn
    sns.heatmap(corr, annot=True, fmt=".1f", mask=mask, square=True, cbar_kws={'shrink': 0.5}, ax=ax)

    # 16. Salvar a figura
    fig.savefig('heatmap.png')
    return fig