import dataanalise as da
import plotly.express as px

data = da.analisar2()

data.drop(columns='municipio', inplace=True)
print(data.corr())


fig = px.imshow(data.corr())

fig.show()