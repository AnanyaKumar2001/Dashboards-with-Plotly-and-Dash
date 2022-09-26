import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

random_x = np.random.randn(1000)
random_y = np.random.rand(1000)

data = [go.Scatter(x = random_x, y = random_y, mode = 'markers',)]

layout = go.Layout(
                    title = 'Random Data Scatterplot',
                    xaxis = dict(title = 'Normal distribution'),
                    yaxis = dict(title = 'Uniform distribution'),
                    hovermode ='closest'
                  )

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='scatter4.html')
