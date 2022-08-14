from django.shortcuts import render
from . import util

from markdown2 import markdown

# used to propose the best match with the search bar entry
from difflib import get_close_matches


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def wiki_page(request,name):

    ## interieur de ce if exécuté seulement dans le cas d'une saisie dans la barre de recherche
    ## "Get the value of a GET variable with name 'q', and if it doesn't exist, return 1"
    if request.GET.get('q'):
        name = request.GET.get('q')
        if (name not in util.list_entries()):
            name = get_close_matches(name, util.list_entries())
            print("here")
            print(type(name))
            return render(request, "encyclopedia/close_match.html", {
                "page_name":"Page not found", "closest_pages":name
            })
    


    if (util.get_entry(name)==None):
        return render(request, "encyclopedia/wiki_page.html", {
            "page_name":"Not Found", "entries":"<p> page not found </p>"
        })
    else:
        return render(request, "encyclopedia/wiki_page.html", {
        "page_name":name, "entries": markdown(util.get_entry(name))
    })

