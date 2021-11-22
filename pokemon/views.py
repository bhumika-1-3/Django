import json
import requests
from django.shortcuts import render
from django.http import HttpResponse
from requests.models import Request

# Create your views here.
array = []
url = 'https://pokeapi.co/api/v2/type/'
call = requests.get(url)
data = json.loads(call.text)
# allTypes=requests.get(url+"1")
# data2 = json.loads(allTypes.text)
# array.append(data2['pokemon'])
# print(array)
for i in data['results']:
    allTypes = requests.get(i['url'])
    data2 = json.loads(allTypes.text)
    array.append(data2['pokemon'])

dataTypes = {
    'data': data['results'],
    'types':array,
}

def pokemon_types(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello world</h1>")
    return render(request, 'home.html', dataTypes)
