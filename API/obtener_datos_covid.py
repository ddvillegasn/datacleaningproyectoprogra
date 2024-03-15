import pandas as pd
from sodapy import Socrata
def obtener_datos_covid(limite, departamento):
    cliente = Socrata("www.datos.gov.co", None)
    resultados = cliente.get("gt2j-8ykr", limit=limite, departamento_nom=departamento)
    return pd.DataFrame.from_records(resultados)