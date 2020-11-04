from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse(
            "Hello, world. 9877c662 is the polls index."
        )



