import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

def plot_histograms(df):
    df.hist(bins=20, figsize=(15, 10), color='blue', edgecolor='black')
    plt.suptitle('Histogramele datelor')
    plt.savefig('../date/grafice/histograme.png')
    plt.close()

def plot_countplot(df):
    sns.countplot(data = df, x = 'tip placa', order = df['tip placa'].value_counts().index)
    plt.title('Numar placi tectonice in functie de tip')
    plt.xlabel('Tip placa')
    plt.ylabel('Numar placi')
    plt.savefig('../date/grafice/countplot.png')
    plt.close()

def plot_coordinates(df):
    sns.scatterplot(data = df, x = 'longitudine', y = 'latitudine', hue = 'magnitudine')
    plt.title('Coordonatele cutremurelor si intensitatea lor')
    plt.xlabel('Longitudine')
    plt.ylabel('Latitudine')
    plt.legend(title='Magnitudine', loc = 'upper right')
    plt.savefig('../date/grafice/coordonate.png')
    plt.close()

def plot_zile_replici_intensitate(df):
    sns.scatterplot(data = df, x = 'zi', y = 'replici', hue = 'magnitudine')
    plt.title('Intensitatea replicilor in functie de zi')
    plt.xlabel('Zi')
    plt.ylabel('Numar replici')
    plt.legend(title='Magnitudine', loc = 'upper right')
    plt.savefig('../date/grafice/zi_replici.png')
    plt.close()

def plot_ult_magnitudine_placa(df):
    sns.boxplot(x = 'tip placa', y = 'magnitudine ultimul', data = df)
    plt.title('Ultima magnitudine in functie de tipul placii tectonice')
    plt.xlabel('Tip placa')
    plt.ylabel('Ultima magnitudine')
    plt.savefig('../date/grafice/ult_magnitudine_placa.png')
    plt.close()

def violin_plot(df):
    sns.violinplot(x = 'tip placa', y = 'magnitudine', data = df)
    plt.title('Distributia magnitudinii in functie de tipul placii tectonice')
    plt.xlabel('Tip placa')
    plt.ylabel('Magnitudine')
    plt.savefig('../date/grafice/violin_plot.png')
    plt.close()

def plot_corr(df):
    corr = df.select_dtypes(include=[np.number]).corr()
    sns.heatmap(corr, annot = True, cmap = 'coolwarm', fmt = '.2f')
    plt.title('Matricea de corelatie')
    plt.savefig('../date/grafice/matrice_corelatie.png')
    plt.close()

def grafice(df):
    plot_histograms(df)
    plot_countplot(df)
    plot_coordinates(df)
    plot_zile_replici_intensitate(df)
    plot_ult_magnitudine_placa(df)
    violin_plot(df)
    plot_corr(df)