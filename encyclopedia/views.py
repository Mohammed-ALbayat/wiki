from django  import forms
from django.http import HttpResponse
from django.shortcuts import render
from markdown2 import Markdown
from . import util
from django.urls import reverse

class searchEntryForm(forms.Form):
    entryTitle = forms.CharField(label='', widget=forms.TextInput(attrs={'placeholder': 'Search Encyclopedia'}))

def convert_md_to_html(title):
    content = util.get_entry(title)
    markDowner = Markdown()
    if content == None:
        return None
    else: 
        return markDowner.convert(content)

##routes

def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries(),
        "searchBar": searchEntryForm()
    })

def entry(request, title):
        
    markDowner = Markdown()
    if convert_md_to_html(title) == None:
        htmlPage = markDowner.convert("#Error: No match title")
    else:
        htmlPage = convert_md_to_html(title)
    return render(request, "encyclopedia/entry.html", {
        "name" : title,
        "content" : htmlPage,
        "searchBar": searchEntryForm()
    })

def searchEntry(request):
    if request.method == "GET":
            entryTitle = request.GET["entryTitle"]
            entryPage = util.get_entry(entryTitle)
            if entryPage == None:
                listEntries = util.list_entries()
                entries = []
                entryTitle = entryTitle.upper()
                for entry in listEntries:
                    entry1 = entry.upper()
                    if entry1.find(entryTitle) != -1:
                        entries.append(entry)
                return render(request, "encyclopedia/searchEntry.html", {
                    "entries": entries,
                    "searchBar": searchEntryForm(),
                    "title": entryTitle
                    })
            else:
                htmlPage = convert_md_to_html(entryTitle)
                return render(request, "encyclopedia/entry.html", {
                    "name" : entryTitle,
                    "content" : htmlPage,
                    "searchBar": searchEntryForm()
                })

    