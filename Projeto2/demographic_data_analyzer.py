import pandas as pd 

def calculate_demographic_data(print_data=True):
    # Ler dados do arquivo
    df = pd.read_csv('adult.data.csv', header=None, names=[
        'age', 'workclass', 'fnlwgt', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country', 'salary'
    ])

    # Converter 'hours_per_week' para numérico, substituindo valores inválidos por NaN
    df['hours_per_week'] = pd.to_numeric(df['hours_per_week'], errors='coerce')

    # Verificar e remover valores ausentes ou inválidos na coluna 'age'
    df['age'] = pd.to_numeric(df['age'], errors='coerce')  # Converter a coluna 'age' para numérica, substituindo valores inválidos por NaN
    df = df.dropna(subset=['age'])  # Remover linhas onde 'age' é NaN

    # Quantidade de pessoas de cada raça no dataset
    race_count = df['race'].value_counts()

    # Média de idade dos homens
    average_age_men = round(df[df['sex'] == 'Male']['age'].mean(), 1)

    # Porcentagem de pessoas com Bacharelado
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # Pessoas com e sem educação superior (Bacharelado, Mestrado ou Doutorado)
    higher_education = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    lower_education = ~higher_education

    # Porcentagem de pessoas com educação superior que ganham mais de 50K
    higher_education_rich = round((df[higher_education & (df['salary'] == '>50K')].shape[0] / df[higher_education].shape[0]) * 100, 1)

    # Porcentagem de pessoas sem educação superior que ganham mais de 50K
    lower_education_rich = round((df[lower_education & (df['salary'] == '>50K')].shape[0] / df[lower_education].shape[0]) * 100, 1)

    # Número mínimo de horas que uma pessoa trabalha por semana
    min_work_hours = df['hours_per_week'].min()

    # Porcentagem de pessoas que trabalham o número mínimo de horas por semana e ganham mais de 50K
    num_min_workers = df[df['hours_per_week'] == min_work_hours]
    rich_percentage = round((num_min_workers[num_min_workers['salary'] == '>50K'].shape[0] / num_min_workers.shape[0]) * 100, 1)

    # País com a maior porcentagem de pessoas que ganham >50K e essa porcentagem
    country_earnings = df[df['salary'] == '>50K']['native_country'].value_counts() / df['native_country'].value_counts() * 100
    highest_earning_country = country_earnings.idxmax()
    highest_earning_country_percentage = round(country_earnings.max(), 1)

    # Ocupação mais popular entre aqueles que ganham >50K na Índia
    top_IN_occupation = df[(df['native_country'] == 'India') & (df['salary'] == '>50K')]['occupation'].value_counts().idxmax()

    # NÃO MODIFIQUE A LINHA ABAIXO
    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
