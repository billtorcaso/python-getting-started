from django.shortcuts import render
from django.template import engines
from django.template.loader import render_to_string
from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("<h1> Innovators For Progress </h1>"
                        "<p> Hello, world! </p>")

