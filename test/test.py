import pandas as pd 
import matplotlib.pyplot as plt


df=pd.read_excel("data/raw/gastos.xlsx")
print (df)

plt.figure(figsize(10,5))
plt.show()
