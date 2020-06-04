import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","hrwproject.settings")
django.setup()


#%% copy this to views.py but do not include the Output bit

# imports
from datetime import datetime
import math

from bokeh.plotting import figure, output_file, show, save
from bokeh.embed import components
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.tools import HoverTool
from hrwapp1.models import Record

# query data
records = Record.objects.all()

# extract data for plot
chart_data = [{"x": record.last_review, "y": record.price} for record in records]
x = list(map(lambda f: f["x"], chart_data))
y = list(map(lambda f: f["y"], chart_data))

# figure
p = figure(
    title="blabla",
    x_axis_type="datetime",
    plot_width=600,
    plot_height=480,
    tools="pan,wheel_zoom,box_zoom,reset",
)

# axis
p.xaxis.axis_label = ""
p.yaxis.axis_label = "Y-Axis"
p.xaxis.formatter = DatetimeTickFormatter(
    hours=["%d %B %Y"],
    days=["%d %B %Y"],
    months=["%d %B %Y"],
    years=["%d %B %Y"],
)
p.xaxis.major_label_orientation = -math.pi/6

# toolbar
p.toolbar_location = "above"
p.toolbar.logo = None

# elements
r0 = p.circle(x,y,size=1)

# legend
legend = Legend(items=[
    ("f(x)",[r0]),
#    ("2*sin(x)",[r2]),
#    ("3*sin(x)",[r3, r4]),
], location="center")

p.add_layout(legend,'right')
p.legend.click_policy="hide"

#%% Output
# display
# show(p)
save(obj=p,filename='bla2.html')