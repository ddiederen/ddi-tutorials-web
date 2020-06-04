# set up django environment
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE","hrwproject.settings")
django.setup()

# specific imports
import pandas as pd
import sqlite3
from hrwapp1.models import Record

# get legacy data
conn = sqlite3.connect('hrwapp1/legacy.db')
query = conn.execute("SELECT * From AB_NYC_2019")
cols = [column[0] for column in query.description]
pdDataLegacy= pd.DataFrame.from_records(data = query.fetchall(), columns = cols)
conn.close()


# put in geom field for leaflet map
pdDataLegacy["geom"] = '{"type":"Point","coordinates":[' + pdDataLegacy.longitude.map(str)+','+pdDataLegacy.latitude.map(str)+']}'
pdDataLegacy["geom"][0]

# adjust date time stuff
for col in pdDataLegacy.columns:
    print(col)
    pdDataLegacy.loc[pdDataLegacy[col]=="", col] = None

# subset for development
pdDataLegacy = pdDataLegacy[:100]

# commit to django
pdDataLegacy.dtypes
Record.objects.bulk_create(
    Record(**vals) for vals in pdDataLegacy.to_dict('records')
)
