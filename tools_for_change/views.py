from django.shortcuts import render
from django.template import engines
from django.template.loader import render_to_string
from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("<h1> Tools For Curiousity </h1>"
                        "<p> Hello, world! </p>")

def about(request):
    return HttpResponse("<h2> Tools For Curiousity </h2>"
                        "<p> Hello, world! </p>"
                        "<br/>"
                        "<p> Tools For Curiousity is a project "
                        "to create a cellphone-playable video game."
                        "The game will include puzzles, levels, "
                        "and a 'Save' feature.")
