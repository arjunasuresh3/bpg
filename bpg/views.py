# Create your views here.
from django.shortcuts import render_to_response
from bpg.models import Area

def index(request):
    area_list = Area.objects.all()
    return render_to_response('area_templates/index.html', {'area_list': area_list})

def detail(request, poll_id):
    return HttpResponse("You're looking at poll %s." % poll_id)
