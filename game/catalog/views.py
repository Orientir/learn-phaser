from django.shortcuts import render
from django.template.response import TemplateResponse

# Create your views here.
def home(request):
    return TemplateResponse(request, "home.html", {})

def first_game(request):
    return TemplateResponse(request, "learn/first_game.html", {})

def space_shooter(request):
    return TemplateResponse(request, "learn/space_shooter.html", {})