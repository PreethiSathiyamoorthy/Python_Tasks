from datetime import datetime as d, timedelta
def today_date():
    return d.now().date().strftime("%d %B %G, %A")
def Yesterday():
    return (d.now().date()-timedelta(1)).strftime("%d %B %G, %A")
def tommorow():
    return (d.now().date()+timedelta(1)).strftime("%d %B %G, %A")
