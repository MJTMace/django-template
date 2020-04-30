from django.shortcuts import render
from .models import Example

# Create your views here.
def homepage(request):
    examples = Example.objects  # get Examples
    return render(request, "examples/home.html", {"examples": examples})
