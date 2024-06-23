from django.shortcuts import render
from markdown2 import Markdown
from . import util

def convert_md_to_html(title):
    content = util.get_entry(title)
    markDowner = Markdown()
    if content == None:
        return None
    else: 
        return markDowner.convert(content)

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    markDowner = Markdown()
    if convert_md_to_html(title) == None:
        htmlPage = markDowner.convert("#Error: No match title")
    else:
        htmlPage = convert_md_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "name" : title,
        "content" : htmlPage
    })

