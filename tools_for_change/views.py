from django.shortcuts import render
from django.template import engines
from django.template.loader import render_to_string
from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("""<h1> Second Deploy: Tools For Curiousity </h1>
                        <p> This page is tfc, method is 'index' </p>
                        <p> This codebase is GIT branch 'bt-2nd-deploy' </p>
                        <p> This dyno is named 'bt-2nd-deploy.herokuapp.com' </p>
                        <br/><p> Hello, world! </p>""")

def aframe(request):
        return render(request, "aframe.html", {})


def about(request):
    return HttpResponse("""<h2> Second Deploy: Tools For Curiousity </h2>
                        <p> Hello, world! </p>
                        <br/>
                        <p> Tools For Curiousity is a project 
                        to create a cellphone-playable video game.
                        The game will include puzzles, levels, 
                        and a 'Save' feature.""")
