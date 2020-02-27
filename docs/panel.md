# Panel

[Panel](https://panel.holoviz.org) is plotting-library-agnostic — it supports nearly all visualization libraries. 

## Getting Started

### Install Panel
```
$ conda install -c pyviz panel
```

### Make a practice dashboard in Jupyter Notebook

The following instructions are based on [this](https://panel.holoviz.org/gallery/simple/altair_choropleth.html#simple-gallery-altair-choropleth) example from the official HoloViz site.

#### In Terminal install altair
```
conda install -c conda-forge altair_data_server
```

#### In Terminal install vega_datasets
```
conda install -c conda-forge vega_datasets vega
```

#### In your Jupyter Notebook, add the following to a code cell
It's a best-practice to put your import statements into their own code block in Jupyter Notebook.
```
import altair as alt
from vega_datasets import data
import panel as pn

pn.extension('vega')
```

#### Add the following to a new code cell
```
altair_logo = 'https://altair-viz.github.io/_static/altair-logo-light.png'
states = alt.topo_feature(data.us_10m.url, 'states')
states['url'] = 'https://raw.githubusercontent.com/vega/vega/master/docs/data/us-10m.json'
source = 'https://raw.githubusercontent.com/vega/vega/master/docs/data/population_engineers_hurricanes.csv'
variable_list = ['population', 'engineers', 'hurricanes']

variable = pn.widgets.Select(options=variable_list, name='Variable')

@pn.depends(variable.param.value)
def get_map(variable):
    return alt.Chart(states).mark_geoshape().encode(
        alt.Color(variable, type='quantitative')
    ).transform_lookup(
        lookup='id',
        from_=alt.LookupData(source, 'id', [variable])
    ).properties(
        width=500,
        height=300
    ).project(
        type='albersUsa'
    ).repeat(
        row=[variable]
    )

pn.Row(
    pn.Column('# Altair Choropleth Maps', pn.panel(altair_logo, height=150), variable),
    get_map
).servable()
```

### Start the Jupyter Notebook server
```
jupyter notebook
```
See your notebooks at http://localhost:8888.

## Resources
- https://github.com/holoviz/panel
- https://panel.holoviz.org/gallery/simple/altair_choropleth.html#simple-gallery-altair-choropleth
