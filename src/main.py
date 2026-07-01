import analisis
import pandas as pd

if __name__=="__main__":
    df=pd.read_excel("data/raw/gastos.xlsx")
    ingreso=int(input("Digite su ingreso"))
    gasto= analisis.calc_gast_mens(df)
    print ("El sobrante es de: ", ingreso-gasto)