import datetime
import json

from django.http import HttpResponse
from django.shortcuts import render

from .models import LastLocation


# Create your views here.
def index(request):
    return render(request, 'index.html')


def api(request):
    if request.method == "POST":
        r_username = request.POST.get('username', '')
        r_lat = request.POST.get('lat', '')
        r_lng = request.POST.get('lng', '')
        r_timestamp = request.POST.get('timestamp', '')

        if r_username == '':
            json_stuff = json.dumps({'success': 1, 'message': 'missing username'})
            return HttpResponse(json_stuff, content_type="application/json")

        if r_lat == '':
            json_stuff = json.dumps({'success': 1, 'message': 'missing lat'})
            return HttpResponse(json_stuff, content_type="application/json")

        if r_lng == '':
            json_stuff = json.dumps({'success': 1, 'message': 'missing lng'})
            return HttpResponse(json_stuff, content_type="application/json")

        if r_timestamp == '':
            json_stuff = json.dumps({'success': 1, 'message': 'missing timestamp'})
            return HttpResponse(json_stuff, content_type="application/json")

        try:
            r_lat = float(r_lat)
            r_lng = float(r_lng)
            r_timestamp = float(r_timestamp)

            ll = LastLocation.objects.all().filter(username=r_username)
            if len(ll) <= 0:
                ll = LastLocation(username=r_username, lat=r_lat, lng=r_lng, timestamp=r_timestamp)
                ll.save()
                json_stuff = json.dumps({'success': 0, 'message': '{}'.format("added")})
            else:
                ll = LastLocation.objects.get(username=r_username)
                ll.lat = r_lat
                ll.lng = r_lng
                ll.timestamp = r_timestamp
                ll.save()
                json_stuff = json.dumps({'success': 0, 'message': '{}'.format("modified")})

            return HttpResponse(json_stuff, content_type="application/json")

        except Exception as e:
            json_stuff = json.dumps({'success': 1, 'message': '{}'.format(e)})
            return HttpResponse(json_stuff, content_type="application/json")

    else:
        try:
            custom_list = list()
            ll = LastLocation.objects.all()

            for location in ll:
                custom_dict = dict()
                custom_dict['title'] = "<center>{}<br>{}</center>".format(location.username,
                                                                          datetime.datetime.fromtimestamp(
                                                                              location.timestamp
                                                                              ).strftime(
                                                                              '%Y-%m-%d %H:%M:%S'))
                custom_dict['lat'] = location.lat
                custom_dict['lng'] = location.lng
                custom_dict['username'] = location.username
                custom_dict['timestamp'] = datetime.datetime.fromtimestamp(location.timestamp
                                                                           ).strftime(
                    '%Y-%m-%d %H:%M:%S')
                custom_list.append(custom_dict)

            json_stuff = json.dumps(custom_list)
            return HttpResponse(json_stuff, content_type="application/json")
        except Exception as e:
            json_stuff = json.dumps({'success': 1, 'message': '{}'.format(e)})
            return HttpResponse(json_stuff, content_type="application/json")
