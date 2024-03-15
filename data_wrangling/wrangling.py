import pandas as pd

def inf_total_df (df):
    return df.info()

def sumario_df(df):
    return df.describe()

def data_no_encontrada(df):
    #retorna columnas con datos faltantes
    return df.columns[df.isnull().any()].tolist()

def encasillar_datos(df):
    df["fecha_inicio_sintomas"] = pd.to_datetime(df["fecha_inicio_sintomas"])
    df["edad"] = pd.to_numeric(df["edad"])


def imputar_datos(df):

    #si no sale pais de origen se supone que es colombia
    df["pais_viajo_1_nom"] = df["pais_viajo_1_nom"].fillna("COLOMBIA")

    #si no tiene recuperación,falleció
    df["tipo_recuperacion"] = df["tipo_recuperacion"].fillna("Fallecido")

    #Si no tienen dato de su estado, serán eliminados del dataframe
    df.dropna(subset=["estado"])