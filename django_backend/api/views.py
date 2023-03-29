from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
import urllib
import json

from modelCore.models import Drawdata


# Create your views here.
def index(request):

    if request.method == 'POST' and 'save' in request.POST:
        data_name = request.POST.get('dataName')
        json_data = request.POST.get('jsonData')
        if json_data != None:
            if Drawdata.objects.filter(jsondata=json_data, name=data_name).count() == 0:
                print('save!!!!')
                Drawdata.objects.create(jsondata=json_data, name=data_name)

        drawDatas = Drawdata.objects.all()
        id_list = list(drawDatas.values_list('id', flat=True))
        id_list_str = json.dumps(id_list)
        return render(request, 'index.html', {'datas': drawDatas, 'id_list_str': id_list_str})

    drawDatas = Drawdata.objects.all()
    id_list = list(drawDatas.values_list('id', flat=True))
    id_list_str = json.dumps(id_list)

    return render(request, 'index.html', {'datas': drawDatas, 'id_list_str': id_list_str})


def return_jsondata(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        jsonData = urllib.parse.parse_qs(request.body.decode('utf-8'))
        data = jsonData['geojsonStr'][0]
        return JsonResponse({'data': data})


def delete_data(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        data = urllib.parse.parse_qs(request.body.decode('utf-8'))
        id = data['id'][0]
        print(id)
        if Drawdata.objects.filter(id=id).count() > 0:
            print(Drawdata.objects.filter(id=id))
            Drawdata.objects.filter(id=id).delete()
            print('delete drawdata object id equal ', id)
        print(Drawdata.objects.filter(id=id))
        return JsonResponse({"id": id})
