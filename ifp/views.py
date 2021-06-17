from django.shortcuts import render
from django.template import engines
from django.template.loader import render_to_string
from django.shortcuts import render,HttpResponse

def index(request):
    return HttpResponse("""<h1> Second Deploy:Innovators For Purpose </h1>
                        <p> This page is /ifp, method is 'index' </p>
                        <p> This codebase is GIT branch 'bt-2nd-deploy' </p>
                        <p> This dyno is named 'bt-2nd-deploy.herokuapp.com' </p>
                        <br/><p> Hello, world! </p>""")

def about(request):
    result = """<h1> This is the 'About' page </h1>
             <br/><p> Hello, world! </p>
             <br/><p> For more information visit 
             <a href='https://innovatorsforpurpose.org/'>
             Innovators For Purpose</a> website.</p>"""
    return HttpResponse(result)

