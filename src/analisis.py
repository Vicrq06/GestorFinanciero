import pandas as pd

#Analisis (describe)
def analisis_basico(df:pd.Dataframe):
    return df.describe()

#Gastos mensuales (calculo)
def calc_gast_mens (df:pd.Dataframe):
    valor=df["valor"].sum()
    return valor

#Filtrar datos
def filtrar_tipo_gastos(df:pd.Dataframe, tipo:string):
    df_filtrado=df[df["tipo"]==tipo]
    return df_filtrado

#Tipo de datos
def data_types(df:df.Dataframe):
    return df.dtypes


#Filtrar por orden
def filtrar(df:df.Dataframe,orden=False):
    df_filtrado=df.sort_values(by="valor",ascending=orden)
    return df_filtrado

#Filtro por categoria 
def filtrar_categoria (df:df.Dataframe,tipo:string):
    df_filtrado=df[df["categoria"]==tipo]
    return df_filtrado


if __name__=="__main__":
    df1=pd.read_excel("data/raw/gastos.xlsx")
    print (filtrar_categoria(df1,"entretenimiento"))


