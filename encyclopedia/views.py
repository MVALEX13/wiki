from django.shortcuts import render
from . import util

from markdown2 import markdown

import encyclopedia


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })



def wiki_page(request,name):
    if (util.get_entry(name)==None):
        return render(request, "encyclopedia/wiki_page.html", {
            "page_name":"Not Found", "entries":"<p> page not found </p>"
        })
    else:
        return render(request, "encyclopedia/wiki_page.html", {
        "page_name":name, "entries": markdown(util.get_entry(name))
    })
