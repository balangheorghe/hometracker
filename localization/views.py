from django.shortcuts import render
from django.http import HttpResponse
import json

# Create your views here.
def index(request):
    return render(request, 'index.html')

def api(request):
    if request.method == "POST":
        custom_list = [
        {'success': "1", 'message': 'custom error'},
        ]
        json_stuff = json.dumps(custom_list)
        return HttpResponse(json_stuff, content_type ="application/json")
    else:
        custom_list = [
        {'title': "GBA", 'lat': 47.1713741, 'lng': 27.5720664},
        ]
        json_stuff = json.dumps(custom_list)
        return HttpResponse(json_stuff, content_type ="application/json")
