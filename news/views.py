from django.shortcuts import render
from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.core.context_processors import csrf

# from django.utils import simplejson as json
from tailor import fetch
import os

# Create your views here.

# def servejson(request):
# 	return HttpResponse(json.dump('[]','Business','Sports','Capital','World','National','Entertainment','Top','Oped','Fiction']),content_type='application/json')


def servejson(request, category="Top"):
    categories = category.split("-")
    fetch(30, categories)
    return HttpResponseRedirect("file://" + os.getcwd() + "/Fetch/fetch.json")
