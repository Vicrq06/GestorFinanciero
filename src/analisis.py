import pandas as pd

#Analisis (describe)
def analisis_basico(df:pd.Dataframe):
    return df.describe()

#Gastos mensuales (calculo)
def calc_gast_mens (df:pd.Dataframe):
    valor=df["valor"].sum()
    return valor

#Filtrar datos
def filtrar_gastos(df:pd.Dataframe, tipo:string):
    df_filtrado=df[df[tipo]]
    return df_filtrado

df1=pd.read_excel("data/raw/gastos.xlsx")

print (df1.dtypes)
print (analisis_basico(df1))
print (calc_gast_mens(df1))



