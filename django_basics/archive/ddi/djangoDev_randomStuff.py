import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','p1mon.settings')
django.setup()


from datetime import datetime, timedelta, date, time
from serial.models import SerialLive
from serial.charts import ChartLiveLine
from django.db.models import Sum

import numpy as np

chart_gauge_n_intervals_big = 10
chart_gauge_n_stripes_per_big = 5
chart_interval_big = round(8/chart_gauge_n_intervals_big,1)
chart_scales = list(set([int(i) for i in np.arange(0,8+chart_interval_big,chart_interval_big)]))
chart_interval = (chart_scales[1]-chart_scales[0])/chart_gauge_n_stripes_per_big


# records today
date_filter = date.today()
date_filter = datetime.strptime('2019-06-12','%Y-%m-%d')
records_today = SerialLive.objects.filter(timestamp__date=date_filter)
record_today_earliest = records_today.earliest('timestamp')
record_today_latest = records_today.latest('timestamp')

# usage today
verbr_kwh_181_min = record_today_earliest.verbr_kwh_181
verbr_kwh_181_max = record_today_latest.verbr_kwh_181
verbr_kwh_181_today = verbr_kwh_181_max-verbr_kwh_181_min
verbr_kwh_182_min = record_today_earliest.verbr_kwh_182
verbr_kwh_182_max = record_today_latest.verbr_kwh_182
verbr_kwh_182_today = verbr_kwh_182_max-verbr_kwh_182_min
verbr_kwh_x_today = verbr_kwh_181_today+verbr_kwh_182_today

gelvr_kwh_281_min = record_today_earliest.gelvr_kwh_281
gelvr_kwh_281_max = record_today_latest.gelvr_kwh_281
gelvr_kwh_281_today = gelvr_kwh_281_max-gelvr_kwh_281_min
gelvr_kwh_282_min = record_today_earliest.gelvr_kwh_282
gelvr_kwh_282_max = record_today_latest.gelvr_kwh_282
gelvr_kwh_282_today = gelvr_kwh_282_max-gelvr_kwh_282_min
gelvr_kwh_x_today = gelvr_kwh_281_today+gelvr_kwh_282_today

verbr_gas_2421_min = record_today_earliest.verbr_gas_2421
verbr_gas_2421_max = record_today_latest.verbr_gas_2421
verbr_gas_2421_today = verbr_gas_2421_max-verbr_gas_2421_min

Dataplot = SerialLive
record_live = Dataplot.objects.latest('timestamp')

# chart line elec
time_threshold = record_live.timestamp - timedelta(minutes=10)
records = SerialLive.objects.exclude(timestamp__lt=time_threshold)
date_max_records = records.latest('timestamp')


chart_data = [{'x': record.timestamp, 'y': record.act_verbr_kw_170} for record in records]
chart_label = 'laatste 10 minuten'
chart_ylabel = 'kWh'
chart_unit = 'minute'

chart_line_elec = ChartLiveLine(
    chart_data=chart_data,
    chart_label=chart_label,
    chart_ylabel=chart_ylabel,
    chart_unit=chart_unit,
)


# chart
chart_live_elec = ChartLiveGauge(
        chart_data=chart_data,
    )
bla = chart_live_elec.as_html()

from geboco.tables import SettingTable,NoteTable
from geboco.models import Setting, Note
tableNotes = NoteTable(Note.objects.filter(analv__startswith="V1"))
print(', '.join(map(str, tableNotes.rows[0])))

from django.conf import settings
from django.contrib.auth.models import User

all_users = User.objects.all()
user = all_users[0]
groups = user.groups.all()
#groups = request.user.groups.all()


from geboco.models import GebocoFile


filesAll = GebocoFile.objects.all()
fileTables = GebocoFile.objects.filter(analysis__startswith="V1")
file = GebocoFile.objects.get(id=1)


bla = "bla"
bla[1]







settings.DATABASES
bla = settings.DATABASES

bla.keys()

bla=settings.INSTALLED_APPS[6]
dir(bla)

dir(settings)

from django.apps import apps
listModels = apps.get_models()
uniqueApplabels = set([model._meta.app_label for model in listModels])

type(uniqueApplabels)

'geboco_bla' in uniqueApplabels
    
bla = list(map(str.split(sep="."),listModels))

dir(settings.DATABASE_ROUTERS)

from django.conf import settings
routersActive = settings.DATABASE_ROUTERS
appsWithRouter = list(map(lambda x: str.split(x,sep=".")[0],routersActive))

list(map())
#items = [1, 2, 3, 4, 5]
#squared = list(map(lambda x: x**2, items))

myset = set(listModels)
print(myset)