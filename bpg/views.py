from django.shortcuts import render_to_response
from bpg.models import Area
from django.http import Http404, HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    area_list = Area.objects.all()
    return render_to_response('area_templates/index.html', {'area_list': area_list})

def detail(request, area_id):
    try:
        a = Area.objects.get(pk=area_id)
        area_list = Area.objects.all()[:5]        
    except Area.DoesNotExist:
        raise Http404
    return render_to_response('area_templates/detail.html', {'pgs': a, 'area_list': area_list})


    # q = request.GET['q']
    # areas_list = Area.objects.filter(area_name__istartswith=q).order_by("area_name")[:10]
    # json = serialize("json", areas_list)

    # return HttpResponse(json, mimetype="application/x-javascript")

@csrf_exempt
def areas_search(request):
    if request.is_ajax():
        raw_data = Area.objects.all()[:5]
        final_raw_data = []
        for i in range(len(raw_data)):
            inner_raw_data = {}
            inner_raw_data['id'] = raw_data[i].id
            inner_raw_data['area_name'] = raw_data[i].area_name
            final_raw_data.append(inner_raw_data)
            
        data = json.dumps(final_raw_data)
        return HttpResponse(data,mimetype="application/json")
    # If you want to prevent non XHR calls
    else:
        return HttpResponse(status=400)
