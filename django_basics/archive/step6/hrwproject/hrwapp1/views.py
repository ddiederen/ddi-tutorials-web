# Import
from django.shortcuts import render

# Create your views here.
def hrwapp1_index(request):
    context = {}
    return render(request, 'hrwapp1/hrwapp1_index.html', context=context)# -*- coding: utf-8 -*-

def hrwapp1_result(request,input1):
    context = {}
    context['input1'] = input1
    return render(request, 'hrwapp1/hrwapp1_result.html', context=context)# -*- coding: utf-8 -*-


from django_q.models import Task
from django_q.tasks import async_task, result
import hrwapp1.tasks as tasks
from django.http import JsonResponse

def hrwapp1_taskrequest(request):
    # init
    result_sync1 = "no sync1 result yet"
    result_sync2 = "no sync2 result yet"
    async_task_id = 'no_id'

    # get items from request
    dict_items = {}
    if request.method == 'POST':
        for key, value in request.POST.items():
            if key != 'csrfmiddlewaretoken':
                dict_items[key] = value


        # handle request
        if dict_items['type_task']=='sync':
            # first sync
            cmd = 'tasks.task_order_fruit(**dict_items)'
            result_sync1 = eval(cmd)

        if dict_items['type_task']=='async':
            task_id = async_task(
                'hrwapp1.tasks.task_order_fruit',
                **dict_items,
            )
            async_task_id = task_id
            result_sync2 = str(task_id) + ' added to the queue'


    # render
    context = {}
    context['result_sync1'] = result_sync1
    context['result_sync2'] = result_sync2
    context['async_task_id'] = async_task_id
    return render(request, 'hrwapp1/hrwapp1_taskrequest.html', context=context)# -*- coding: utf-8 -*-

def hrwapp1_taskresult(request,task_id):
    # this is the async result view, which is going to be polled by the client with javascript

    # try to get the result
    try:
        bla = Task.objects.get(id=task_id)
        result_async = bla.result
    except:
        result_async = 'No async result just yet..'
    print(result)

    # send async
    context = {}
    context['result_async'] = result_async
    return JsonResponse(context)


# figure imports
from django.shortcuts import  render_to_response
from bokeh.plotting import figure, output_file, show, save
from bokeh.embed import components
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.models import ColumnDataSource, Legend
from bokeh.models.tools import HoverTool
import math
from hrwapp1.models import Record

# figure view
def hrwapp1_figure(request,input1):
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
    p.xaxis.major_label_orientation = -math.pi / 6

    # toolbar
    p.toolbar_location = "above"
    p.toolbar.logo = None

    if input1 == 'scatter':
        # elements
        r0 = p.circle(x, y, size=1)
    elif input1 == 'line':
        # elements
        r0 = p.line(x, y, line_width=1)

    # legend
    legend = Legend(items=[
        ("f(x)", [r0]),
        #    ("2*sin(x)",[r2]),
        #    ("3*sin(x)",[r3, r4]),
    ], location="center")

    p.add_layout(legend, 'right')
    p.legend.click_policy = "hide"

    # store components
    script, div = components(p)

    # render
    context = {}
    context['input1'] = input1          # input1 is variable (str) that comes directly from the url (see urls.py)
    context['script'] = script          # this is the javascript component of the Bokeh plot
    context['div'] = div                # this is the HTML component of the Bokeh plot
    return render_to_response('hrwapp1/hrwapp1_figure.html', context=context)# -*- coding: utf-8 -*-