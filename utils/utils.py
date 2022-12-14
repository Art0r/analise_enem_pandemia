from dask import dataframe as dd
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
import os


def plot_hist_classes_all(df: pd.DataFrame, output_path: str):
    fig, ax = plt.subplots(figsize=(10, 6))

    df.query("Q006 == 'E'")[['NU_MEDIA_GERAL']].hist(
        bins=50, ax=ax, label="Classe E")
    df.query("Q006 == 'D'")[['NU_MEDIA_GERAL']].hist(
        bins=50, ax=ax, label="Classe D")
    df.query("Q006 == 'C'")[['NU_MEDIA_GERAL']].hist(
        bins=50, ax=ax, label="Classe C")
    df.query("Q006 == 'B'")[['NU_MEDIA_GERAL']].hist(
        bins=50, ax=ax, label="Classe B")
    df.query("Q006 == 'A'")[['NU_MEDIA_GERAL']].hist(
        bins=50, ax=ax, label="Classe A")

    n_candidatos = df.shape[0]
    ax.set_title(
        f"Número de pessoas x Media Geral - {df[['NU_ANO']].iloc[0][0]} - {n_candidatos} candidatos")
    ax.set_ylabel('Número de pessoas')
    ax.set_xlabel('Nota')
    ax.legend()

    fig.savefig(os.path.join(
        output_path, f"all_classes_{df[['NU_ANO']].iloc[0][0]}.jpg"))


def plot_hist_classes(df: pd.DataFrame, output_path: str):
    fig, [[ax1, ax2], [ax3, ax4], [ax5, _]] = plt.subplots(3, 2,
                                                           figsize=(14, 11),
                                                           # constrained_layout=True
                                                           )
    fig.suptitle(
        f"Número de pessoas x Media Geral - {df[['NU_ANO']].iloc[0][0]} - {df.shape[0]} candidatos", fontsize=16)

    df.query(f"Q006 == 'E'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax1, label=f"Classe E", color='blue')
    ax1.set_title(
        "Classe E - {0} candidatos".format(df.query(f"Q006 == 'E'").shape[0]))
    ax1.set_ylabel('Número de pessoas')
    ax1.set_xlabel('Nota')

    df.query(f"Q006 == 'D'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax2, label=f"Classe D", color='orange')
    ax2.set_title(
        "Classe D - {0} candidatos".format(df.query(f"Q006 == 'D'").shape[0]))
    ax2.set_ylabel('Número de pessoas')
    ax2.set_xlabel('Nota')

    df.query(f"Q006 == 'C'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax3, label=f"Classe C", color='green')
    ax3.set_title(
        "Classe C - {0} candidatos".format(df.query(f"Q006 == 'C'").shape[0]))
    ax3.set_ylabel('Número de pessoas')
    ax3.set_xlabel('Nota')

    df.query(f"Q006 == 'B'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax4, label=f"Classe B", color='red')
    ax4.set_title(
        "Classe B - {0} candidatos".format(df.query(f"Q006 == 'B'").shape[0]))
    ax4.set_ylabel('Número de pessoas')
    ax4.set_xlabel('Nota')

    df.query(f"Q006 == 'A'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax5, label=f"Classe A", color='purple')
    ax5.set_title(
        "Classe A - {0} candidatos".format(df.query(f"Q006 == 'A'").shape[0]))
    ax5.set_ylabel('Número de pessoas')
    ax5.set_xlabel('Nota')

    fig.savefig(os.path.join(
        output_path, f"histogram_classes_{df[['NU_ANO']].iloc[0][0]}.jpg"))


def plot_hist_boxplot_classes(df: pd.DataFrame, output_path: str):
    fig, [[ax1, ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8], [ax9, ax10], [ax11, ax12]] = plt.subplots(6, 2,
                                                                                                    figsize=(
                                                                                                        13, 22),
                                                                                                    constrained_layout=True
                                                                                                    )

    fig.suptitle(
        f"Número de pessoas x Media Geral - {df[['NU_ANO']].iloc[0][0]} - {df.shape[0]} candidatos", fontsize=16)

    df[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax1, label="Total da Amostra", color="blue")
    ax1.set_title(
        "Descrição da amostra - {0} candidatos".format(df.shape[0]))
    ax1.set_ylabel('Número de pessoas')
    ax1.set_xlabel('Nota')

    df[['NU_MEDIA_GERAL']].plot.box(
        ax=ax2, label="Total da Amostra", grid=True)
    ax2.set_title(
        "Descrição da amostra - {0} candidatos".format(df.shape[0]))
    ax2.set_ylabel('Número de pessoas')
    ax2.set_xlabel('Nota')

    df.query("Q006 == 'E'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax3, label="Classe E", color="blue")
    ax3.set_title(
        "Classe E - {0} candidatos".format(df.query(f"Q006 == 'E'").shape[0]))
    ax3.set_ylabel('Número de pessoas')
    ax3.set_xlabel('Nota')

    df.query("Q006 == 'E'")[['NU_MEDIA_GERAL']].plot.box(
        ax=ax4, label="Classe E", grid=True)
    ax4.set_title(
        "Classe E - {0} candidatos".format(df.query("Q006 == 'E'").shape[0]))
    ax4.set_ylabel('Número de pessoas')
    ax4.set_xlabel('Nota')

    df.query("Q006 == 'D'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax5, label="Classe D", color='orange')
    ax5.set_title(
        "Classe D - {0} candidatos".format(df.query("Q006 == 'D'").shape[0]))
    ax5.set_ylabel('Número de pessoas')
    ax5.set_xlabel('Nota')

    df.query("Q006 == 'D'")[['NU_MEDIA_GERAL']].plot.box(
        ax=ax6, label="Classe D", grid=True)
    ax6.set_title(
        "Classe D - {0} candidatos".format(df.query("Q006 == 'D'").shape[0]))
    ax6.set_ylabel('Número de pessoas')
    ax6.set_xlabel('Nota')

    df.query("Q006 == 'C'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax7, label="Classe C", color='green')
    ax7.set_title(
        "Classe C - {0} candidatos".format(df.query("Q006 == 'C'").shape[0]))
    ax7.set_ylabel('Número de pessoas')
    ax7.set_xlabel('Nota')

    df.query("Q006 == 'C'")[['NU_MEDIA_GERAL']].plot.box(
        ax=ax8, label="Classe C", grid=True)
    ax8.set_title(
        "Classe C - {0} candidatos".format(df.query("Q006 == 'C'").shape[0]))
    ax8.set_ylabel('Número de pessoas')
    ax8.set_xlabel('Nota')

    df.query("Q006 == 'B'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax9, label="Classe B", color='red')
    ax9.set_title(
        "Classe B - {0} candidatos".format(df.query("Q006 == 'B'").shape[0]))
    ax9.set_ylabel('Número de pessoas')
    ax9.set_xlabel('Nota')

    df.query("Q006 == 'B'")[['NU_MEDIA_GERAL']].plot.box(
        ax=ax10, label="Classe B", grid=True)
    ax10.set_title(
        "Classe B - {0} candidatos".format(df.query("Q006 == 'B'").shape[0]))
    ax10.set_ylabel('Número de pessoas')
    ax10.set_xlabel('Nota')

    df.query("Q006 == 'A'")[['NU_MEDIA_GERAL']].hist(
        bins=100, ax=ax11, label="Classe A", color='purple')
    ax11.set_title(
        "Classe A - {0} candidatos".format(df.query("Q006 == 'A'").shape[0]))
    ax11.set_ylabel('Número de pessoas')
    ax11.set_xlabel('Nota')

    df.query("Q006 == 'A'")[['NU_MEDIA_GERAL']].plot.box(
        ax=ax12, label="Classe A", grid=True)
    ax12.set_title(
        "Classe A - {0} candidatos".format(df.query("Q006 == 'A'").shape[0]))
    ax12.set_ylabel('Número de pessoas')
    ax12.set_xlabel('Nota')

    fig.tight_layout(pad=5.0)

    fig.savefig(os.path.join(
        output_path, f"histogram_and_boxplot_classes_{df[['NU_ANO']].iloc[0][0]}.jpg"))


def plot_boxplot_descricao_amostras(df: list[pd.DataFrame], output_path: str):
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(10, 15))

    sns.boxplot(x='Q006', y='NU_MEDIA_GERAL', data=df[0],
                ax=ax1, order=['A', 'B', 'C', 'D', 'E']).set(xlabel='Classe Social', ylabel='Nota')
    ax1.set_title(
        "Descrição da amostra - {0}".format(df[0][['NU_ANO']].iloc[0][0]))
    ax1.set_ylabel('Nota')
    ax1.set_xlabel('Classe Social')
    ax1.yaxis.grid(True)

    sns.boxplot(x='Q006', y='NU_MEDIA_GERAL', data=df[1],
                ax=ax2, order=['A', 'B', 'C', 'D', 'E']).set(xlabel='Classe Social', ylabel='Nota')
    ax2.set_title(
        "Descrição da amostra - {0}".format(df[1][['NU_ANO']].iloc[0][0]))
    ax2.set_ylabel('Nota')
    ax2.set_xlabel('Classe Social')
    ax2.yaxis.grid(True)

    sns.boxplot(x='Q006', y='NU_MEDIA_GERAL', data=df[2],
                ax=ax3, order=['A', 'B', 'C', 'D', 'E']).set(xlabel='Classe Social', ylabel='Nota')
    ax3.set_title(
        "Descrição da amostra - {0}".format(df[2][['NU_ANO']].iloc[0][0]))
    ax3.set_ylabel('Nota')
    ax3.set_xlabel('Classe Social')
    ax3.yaxis.grid(True)

    fig.tight_layout(pad=5.0)
    fig.savefig(os.path.join(output_path, 'all_classes_by_year_boxplot.jpg'))


def setup():
    YEARS = ['2019', '2020', '2021']
    PATHS = {
        '2019': os.path.join(os.getcwd(), 'dados', 'microdados_enem_2019', 'DADOS', 'MICRODADOS_ENEM_2019.csv'),
        '2020': os.path.join(os.getcwd(), 'dados', 'microdados_enem_2020', 'DADOS', 'MICRODADOS_ENEM_2020.csv'),
        '2021': os.path.join(os.getcwd(), 'dados', 'microdados_enem_2021', 'DADOS', 'MICRODADOS_ENEM_2021.csv')
    }
    ENCODING = "latin1"
    SEP = ";"
    COLS = [
        'NU_INSCRICAO',
        'Q006',
        'NU_ANO',
        #         'TP_COR_RACA',
        #         'SG_UF_ESC',
        #         'TP_SEXO',
        #         'TP_FAIXA_ETARIA',
        #         'TP_ESCOLA',
        #         'IN_TREINEIRO',
        'NU_NOTA_CN',
        'NU_NOTA_MT',
        'NU_NOTA_LC',
        'NU_NOTA_CH',
        'NU_NOTA_REDACAO',
    ]

    df = {}
    for i in YEARS:
        df[i] = dd.read_csv(PATHS[i], encoding=ENCODING, sep=SEP, dtype={
                            'SG_UF_ESC': 'object'}, usecols=COLS)
        df[i] = df[i].compute()
        df[i].dropna(inplace=True)

        for j in 'DEFG':
            df[i].loc[df[i]['Q006'] == j, 'Q006'] = 'D'

        for j in 'ABC':
            df[i].loc[df[i]['Q006'] == j, 'Q006'] = 'E'

        for j in 'HIJKLM':
            df[i].loc[df[i]['Q006'] == j, 'Q006'] = 'C'

        for j in 'NOP':
            df[i].loc[df[i]['Q006'] == j, 'Q006'] = 'B'

        df[i].loc[df[i]['Q006'] == 'Q', 'Q006'] = 'A'

        df[i]['NU_MEDIA_GERAL'] = (df[i]['NU_NOTA_MT'] + df[i]['NU_NOTA_LC']
                                   + df[i]['NU_NOTA_CH'] + df[i]['NU_NOTA_CN']
                                   + df[i]['NU_NOTA_REDACAO'])/5

    return [df[i] for i in YEARS]
