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