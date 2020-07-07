
import json
import datetime
from collections import Counter
from bokeh.plotting import figure, show, output_file

def reading_json (): 
    with open("birthdayfile.json","r") as birthday: #birthdayfile.json is json file name
        birthday_file = json.load(birthday)
    getting_only_values = list(birthday_file.values())
    return (getting_only_values)

def month_counter ():

    montha = []
    
    for element in reading_json():
        montha.append(datetime.datetime.strptime(element, "%m/%d/%Y").strftime("%B"))
        
    return(Counter(montha))

def month_names ():
    month_names = []
    for i in range (1,13):
        month_names.append(datetime.datetime.strptime(str(i),"%m").strftime("%B"))
    return (month_names)


def bokeh_plot ():
    output_file("plota.html")
    x_categories = month_names()
    x = list(month_counter().keys())
    y = list(month_counter().values())

    p = figure(x_range=x_categories)
    p.vbar(x=x, top=y, width=1.25)

    show(p)
    
bokeh_plot()
