from API import obtener_datos_covid as API
from UI import mostrar_datos as UI
from data_wrangling import wrangling

print("\nDataFrame filtrado por el departamento de Risaralda (1000 primeros datos)\n\n")

#se trabaja con los datos extraidos filtrados del departamento de Risaralda.
libreria_data_obtenida = API.obtener_datos_covid("1000", "RISARALDA")
UI.mostrar_data(libreria_data_obtenida)

#Se repite el primer paso del proceso de data wrangling
UI.imprimir_inf_and_sum_df(libreria_data_obtenida)

#imputacion
wrangling.imputar_datos(libreria_data_obtenida)

#conversión de tipos de datos para compatibilidad con funciones de visualización
wrangling.encasillar_datos(libreria_data_obtenida)

print("\nDataFrame después de ser pasado por un proceso de imputación y typecasting\n\n")
# Imprime dataframe con valores imputados
UI.mostrar_data(libreria_data_obtenida)

#Se repite el primer paso del data Wrangling
UI.imprimir_inf_and_sum_df(libreria_data_obtenida)

#Resultados mediante plots
UI.visualizar_graficas(libreria_data_obtenida)