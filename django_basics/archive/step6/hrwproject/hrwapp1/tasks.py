import time

def task_order_fruit(fruit_type,num_fruit,type_task):
    time.sleep(int(num_fruit))   # e.g. 2 apples take 2 secs
    return '%s: %s_%s' % (type_task,fruit_type, num_fruit)