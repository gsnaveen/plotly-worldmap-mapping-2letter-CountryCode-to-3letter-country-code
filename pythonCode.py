from IPython.core.display import display, HTML
from IPython.display import display
display(HTML("<style>.container { width:100% !important; }</style>"))
import plotly.plotly as py
import plotly.graph_objs as go 
import pandas as pd
from plotly.offline import download_plotlyjs,init_notebook_mode,plot,iplot
init_notebook_mode(connected=True)
dfcountry = pd.read_csv('countryMap.txt',sep='\t')
dfData = pd.read_csv('sampledata.txt',sep='\t')
df = dfData.merge(dfcountry,how='inner',left_on=['Country'],right_on=['2let'])
df.head()

data = dict(
        type = 'choropleth',
        locations = df['3let'],
        z = df['SlowSpeed'],
        text = df['Countrylet'],
        colorbar = {'title' : 'Response Time'},
      )

layout = dict(
    title = 'User Activity',
    geo = dict(
        showframe = False,
        projection = {'type':'Mercator'}
    )
)

choromap = go.Figure(data = [data],layout = layout)
iplot(choromap)
