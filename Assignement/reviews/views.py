
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import *
import json
from django.views.generic import View,CreateView,DetailView
from django.contrib import messages
from datetime import datetime

def homepage(request):
    
    title="Dashboard"
    f = open ('jsondata.json', "r",encoding='utf-8')
    data_file = json.loads(f.read())
    new_data_file = {}
    count=10000
    for i in data_file:
        correct_format = "%Y-%m-%d"

        if i['added']:
            date_string = i['added']
            date_format = "%B, %d %Y %H:%M:%S"
            date_object = datetime.strptime(date_string, date_format)
            correct_date_string = date_object.strftime(correct_format)
            i['added']  = correct_date_string
        
        if i['published']:
            date_string = i['published']
            date_format = "%B, %d %Y %H:%M:%S"
            date_object = datetime.strptime(date_string, date_format)
            correct_date_string = date_object.strftime(correct_format)
            i['published']  = correct_date_string

        if i['end_year']=='':
            i['end_year']=None
        if i['start_year']=="":
            i['start_year']=None
        if i['added']=='':
            i['added']=None
        if i['published']=='':
            i['published']=None
        if i['intensity']=='':
            i['intensity']=None
        if i['likelihood']=='':
            i['likelihood']=None
        if i['relevance']=='':
            i['relevance']=None
            
        if i['sector'] in new_data_file:
            new_data_file[i['sector']].append(i)
        else:
            if i['sector']== "":
                if i['topic'] in new_data_file:
                    new_data_file[i['topic']].append(i)
                else:
                    if i['topic']=="":
                        new_data_file['other']=i
                    else:
                        new_data_file[i['topic']]=[i]
            else:
                new_data_file[i['sector']]=[i]
        
        # DashBoardData.objects.create(data_id=count,end_year= i['end_year'], intensity= i['intensity'], sector= i['sector'],topic= i['topic'], insight= i['insight'],url= i['url'], region= i['region'], start_year= i['start_year'], impact= i['impact'],added= i['added'], published= i['published'], country= i['country'], relevance= i['relevance'], pestle= i['pestle'], source= i['source'], title= i['title'], likelihood= i['likelihood'])
        count+=1
    return render(request, 'title_page.html', locals())



def datapage(request,my_string):
    obj1 = DashBoardData.objects.filter(sector=my_string)
    obj2 = DashBoardData.objects.filter(topic=my_string)
    new_data_file = {}
    title = my_string
    if obj1:
        for i in obj1:
            if i.topic in new_data_file:
                if i.topic=="":
                    i.topic=my_string
                new_data_file[i.topic].append(i)
            else:
                if i.topic=="":
                    i.topic=my_string
                new_data_file[i.topic]=[i]
    
    elif obj2:
        for i in obj2:
            if i.topic in new_data_file:
                if i.topic=="":
                    i.topic=my_string
                new_data_file[i.topic].append(i)
            else:
                if i.topic=="":
                    i.topic=my_string
                new_data_file[i.topic]=[i]

    return render(request, 'newdata.html', locals())



def newdatapage(request,my_string,new_string):
    obj1 = DashBoardData.objects.filter(topic=new_string)
    new_data_file = {}
    title = my_string    
    
    return render(request, 'newstringdata.html', locals())