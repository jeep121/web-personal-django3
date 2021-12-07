from django.shortcuts import render, HttpResponse

html_base = """"<h1>Mi Web Personal</h1><h2> Portada </h2>
<ul> 
    <li> <a href="/"> Portada </a> </li>
    <li> <a href="/about/"> Acerca de... </a> </li>
    <li> <a href="/portafolio/"> Portafolio </a> </li>
    <li> <a href="/contact/"> Contactame </a> </li>
</ul>
"""

# Create your views here.
def home(request):
    return render(request, "core/home.html")

def about(request):
    return render(request, "core/about.html")



def contact(request):
    return render(request, "core/contact.html")

