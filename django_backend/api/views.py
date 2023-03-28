from django.shortcuts import render ,redirect
from django.http import HttpResponse ,JsonResponse ,HttpResponseRedirect 
import urllib
import json, io

from modelCore.models import Drawdata


# Create your views here.
def index(request):
    if request.method == 'POST' and 'save' in request.POST:
        data_name = request.POST.get('dataName')
        json_data_str = request.POST.get('jsonData')
        json_data = json.loads(json_data_str)
        print(type(json_data))
        if Drawdata.objects.filter(jsondata=json_data,name=data_name).count() == 0:
            Drawdata.objects.create(jsondata=json_data,name=data_name)

    drawDatas = Drawdata.objects.all()
    datalength = drawDatas.count()
    return render(request, 'index.html',{'datas':drawDatas,'datalength':datalength})

def return_jsondata(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest' :

        jsonData = urllib.parse.parse_qs(request.body.decode('utf-8'))
        
        data = json.dumps(jsonData)

        return JsonResponse({'data':data})