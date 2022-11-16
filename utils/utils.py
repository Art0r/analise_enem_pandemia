import matplotlib.pyplot as plt
import pandas as pd
import os


def make_analisys_image(df: pd.DataFrame, output_path: str):
    fig, [[ax1, ax2], [ax3, ax4], [ax5, ax6], [ax7, ax8], [ax9, ax10], [ax11, ax12]] = plt.subplots(6, 2,
                                                                                                    figsize=(
                                                                                                        13, 22),
                                                                                                    constrained_layout=True
                                                                                                    )

    fig.suptitle(
        f"Número de pessoas x Nota da Redação - {df[['NU_ANO']].iloc[0][0]} - {df.shape[0]} candidatos", fontsize=16)

    df[['NU_NOTA_REDACAO']].hist(
        bins=100, ax=ax1, label="Total da Amostra", color="blue")
    ax1.set_title(
        "Descrição da amostra - {0} candidatos".format(df.shape[0]))
    ax1.set_ylabel('Número de pessoas')
    ax1.set_xlabel('Nota')

    df[['NU_NOTA_REDACAO']].plot.box(
        ax=ax2, label="Total da Amostra", grid=True)
    ax2.set_title(
        "Descrição da amostra - {0} candidatos".format(df.shape[0]))
    ax2.set_ylabel('Número de pessoas')
    ax2.set_xlabel('Nota')

    df.query("Q006 == 'E'")[['NU_NOTA_REDACAO']].hist(
        bins=100, ax=ax3, label="Classe E", color="blue")
    ax3.set_title(
        "Classe E - {0} candidatos".format(df.query(f"Q006 == 'E'").shape[0]))
    ax3.set_ylabel('Número de pessoas')
    ax3.set_xlabel('Nota')

    df.query("Q006 == 'E'")[['NU_NOTA_REDACAO']].plot.box(
        ax=ax4, label="Classe E", grid=True)
    ax4.set_title(
        "Classe E - {0} candidatos".format(df.query("Q006 == 'E'").shape[0]))
    ax4.set_ylabel('Número de pessoas')
    ax4.set_xlabel('Nota')

    df.query("Q006 == 'D'")[['NU_NOTA_REDACAO']].hist(
        bins=100, ax=ax5, label="Classe D", color='orange')
    ax5.set_title(
        "Classe D - {0} candidatos".format(df.query("Q006 == 'D'").shape[0]))
    ax5.set_ylabel('Número de pessoas')
    ax5.set_xlabel('Nota')

    df.query("Q006 == 'D'")[['NU_NOTA_REDACAO']].plot.box(
        ax=ax6, label="Classe D", grid=True)
    ax6.set_title(
        "Classe D - {0} candidatos".format(df.query("Q006 == 'D'").shape[0]))
    ax6.set_ylabel('Número de pessoas')
    ax6.set_xlabel('Nota')

    df.query("Q006 == 'C'")[['NU_NOTA_REDACAO']].hist(
        bins=100, ax=ax7, label="Classe C", color='green')
    ax7.set_title(
        "Classe C - {0} candidatos".format(df.query("Q006 == 'C'").shape[0]))
    ax7.set_ylabel('Número de pessoas')
    ax7.set_xlabel('Nota')

    df.query("Q006 == 'C'")[['NU_NOTA_REDACAO']].plot.box(
        ax=ax8, label="Classe C", grid=True)
    ax8.set_title(
        "Classe C - {0} candidatos".format(df.query("Q006 == 'C'").shape[0]))
    ax8.set_ylabel('Número de pessoas')
    ax8.set_xlabel('Nota')

    df.query("Q006 == 'B'")[['NU_NOTA_REDACAO']].hist(
        bins=100, ax=ax9, label="Classe B", color='red')
    ax9.set_title(
        "Classe B - {0} candidatos".format(df.query("Q006 == 'B'").shape[0]))
    ax9.set_ylabel('Número de pessoas')
    ax9.set_xlabel('Nota')

    df.query("Q006 == 'B'")[['NU_NOTA_REDACAO']].plot.box(
        ax=ax10, label="Classe B", grid=True)
    ax10.set_title(
        "Classe B - {0} candidatos".format(df.query("Q006 == 'B'").shape[0]))
    ax10.set_ylabel('Número de pessoas')
    ax10.set_xlabel('Nota')

    df.query("Q006 == 'A'")[['NU_NOTA_REDACAO']].hist(
        bins=100, ax=ax11, label="Classe A", color='purple')
    ax11.set_title(
        "Classe A - {0} candidatos".format(df.query("Q006 == 'A'").shape[0]))
    ax11.set_ylabel('Número de pessoas')
    ax11.set_xlabel('Nota')

    df.query("Q006 == 'A'")[['NU_NOTA_REDACAO']].plot.box(
        ax=ax12, label="Classe A", grid=True)
    ax12.set_title(
        "Classe A - {0} candidatos".format(df.query("Q006 == 'A'").shape[0]))
    ax12.set_ylabel('Número de pessoas')
    ax12.set_xlabel('Nota')

    fig.tight_layout(pad=5.0)

    fig.savefig(os.path.join(
        output_path, f"histogram_and_boxplot_classes_{df[['NU_ANO']].iloc[0][0]}.jpg"))
