#!/usr/bin/env python
# coding: utf-8

# In[29]:


import pandas as pd

tabela = pd.read_csv("advertising.csv")

import seaborn as sns
import matplotlib.pyplot as plt 

sns.heatmap(tabela.corr(), annot=True, cmap="Wistia")
sns.pairplot(tabela)
plt.show()

from sklearn.model_selection import train_test_split

y=tabela["Vendas"]

x=tabela.drop("Vendas", axis=1)

x_treino, x_teste, y_treino, y_teste = train_test_split(x, y, test_size=0.3, random_state=1)

from sklearn.linear_model import LinearRegression

from sklearn.ensemble import RandomForestRegressor
#criar as inteligencias artificiais
modelo_regressaolinear = LinearRegression()
modelo_arvoredecisao = RandomForestRegressor()
#treina as inteligencias artificiais
modelo_regressaolinear.fit(x_treino, y_treino)
modelo_arvoredecisao.fit(x_treino, y_treino)

RandomForestRegressor()

from sklearn import metrics 
#criar as previsões
previsao_regressaolinear = modelo_regressaolinear.predict(x_teste)
previsao_arvoredecisao = modelo_arvoredecisao.predict(x_teste)
#comparar os modelos
print(metrics.r2_score(y_teste, previsao_regressaolinear))
print(metrics.r2_score(y_teste, previsao_regressaolinear))
#visualização gráfica das previsões
tabela_auxiliar = pd.DataFrame()
tabela_auxiliar["y_teste"] = y_teste
tabela_auxiliar["Previsoes ArvoreDecisao"] = previsao_arvoredecisao
tabela_auxiliar["Previsoes Regressao Linear"] = previsao_regressaolinear

plt.figure(figsize=(15, 5))

sns.lineplot(data=tabela_auxiliar)
plt.show()

sns.barplot(x=x_treino.columns, y=modelo_arvoredecisao.feature_importances_)
plt.show()


# In[ ]:





# In[ ]:




