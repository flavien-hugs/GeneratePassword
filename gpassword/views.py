import random
import string
from django.shortcuts import render
from django.views.generic import TemplateView


# HOME VIEWS
class HomeView(TemplateView):
    template_name = "base.html"


# view generate password
def generate(request):
    carac = list(
        string.digits + string.ascii_letters +
        string.ascii_lowercase +
        string.ascii_uppercase +
        string.punctuation
    )

    random_carac = [random.choice(carac) for _ in range(24)]
    password = ''.join(random_carac)
    template = 'base.html'
    context = {'password': password}
    return render(request, template, context)
