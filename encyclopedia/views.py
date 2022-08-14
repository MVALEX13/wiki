from django.shortcuts import render
from . import util

from markdown2 import markdown


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def wiki_page(request,name):

    ## "Get the value of a GET variable with name 'q', and if it doesn't exist, return 1"
    if request.GET.get('q'):
        name = request.GET.get('q')

    if (util.get_entry(name)==None):
        return render(request, "encyclopedia/wiki_page.html", {
            "page_name":"Not Found", "entries":"<p> page not found </p>"
        })
    else:
        return render(request, "encyclopedia/wiki_page.html", {
        "page_name":name, "entries": markdown(util.get_entry(name))
    })
