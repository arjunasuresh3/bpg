from django.shortcuts import render_to_response
from bpg.models import Area
from django.http import Http404

def index(request):
    area_list = Area.objects.all()
    return render_to_response('area_templates/index.html', {'area_list': area_list})

def detail(request, area_id):
    try:
        a = Area.objects.get(pk=area_id)
        area_list = Area.objects.all()        
    except Area.DoesNotExist:
        raise Http404
    return render_to_response('area_templates/detail.html', {'pgs': a, 'area_list': area_list})
