from django.shortcuts import render, get_object_or_404
from .models import Example

# Create your views here.
def homepage(request):
    examples = Example.objects  # get Examples
    return render(request, "examples/home.html", {"examples": examples})


def detail(request, example_id):
    # print(example_id)
    example_detail = get_object_or_404(
        Example, pk=example_id
    )  # every model inside of the database has a primary key
    return render(request, "examples/detail.html", {"example": example_detail})
