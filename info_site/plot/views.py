from django.shortcuts import render
# from django.template.response import TemplateResponse

import os
# import table model and connection
from sheet_parser.app import google_sheets, conn

def index(request):
    dates = []
    prices_usd = []
    
    query = google_sheets.select().order_by(google_sheets.c.delivery_time)
    r = conn.execute(query).fetchall()

    for row in r:
        prices_usd.append(row[2])
        dates.append(row[3].strftime("%d.%m.%Y"))
    # print(dates, prices_usd)
    return render(request, 'plot/index.html', {
        'dates': dates,
        'prices': prices_usd,
    })