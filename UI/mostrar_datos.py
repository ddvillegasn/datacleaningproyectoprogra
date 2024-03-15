from tabulate import tabulate
from data_wrangling import wrangling
import matplotlib.pyplot as plt

def mostrar_data(results_df):

    print(tabulate(results_df, tablefmt="grid", headers=results_df.keys()))

def imprimir_inf_and_sum_df (df):

    print("\nInf general del dataframe:\n")
    print(wrangling.inf_total_df(df))

    print("\nColumnas valores faltantes: \n" )
    print(wrangling.data_no_encontrada(df))

    print("\nSumario del dataframe:\n")
    sumario = wrangling.sumario_df(df)
    print(tabulate(sumario, tablefmt="grid", headers=sumario.columns.values.tolist()))
    print("\n")

def visualizar_graficas (df):
    plt.hist(df["ciudad_municipio_nom"], color="red", bins=40)
    plt.xlabel("Municipio")
    plt.ylabel("Frecuencia")
    plt.title("Histograma: Distribución de datos en municipios")
    plt.xticks(rotation=90)  # Rotar los nombres de los municipios en el eje x
    plt.show()


    conteo_valores = df["estado"].value_counts()
    plt.barh(conteo_valores.index, conteo_valores.values, color=["blue", "red", "yellow"])
    plt.xlabel("Cantidad")
    plt.ylabel("Estado")
    plt.title("Diagrama de barras: Estado de los individuos")
    plt.show()

    df[["edad", "fecha_inicio_sintomas"]].plot.scatter(x="fecha_inicio_sintomas", y="edad", color="magenta")
    plt.xlabel("Fecha de inicio de síntomas")
    plt.ylabel("Edad del paciente")
    plt.title("Gráfico de dispersión: Fecha de inicio de síntomas vs. Edad")
    plt.show()

