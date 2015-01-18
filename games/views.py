from django.views import generic
from django.shortcuts import render
from . import models

class GameIndex(generic.ListView):
	queryset = models.Game.objects.order_by('title')
	template_name = "home.html"

class GameDetail(generic.DetailView):
	model = models.Game
	template_name = "post.html"

def search(request):
    query = request.GET.get('q')
    if query:
        # There was a query entered.
        results = models.Game.objects.filter(title__contains=query)
    else:
        # If no query was entered, simply return all objects
        results = models.Game.objects.order_by('title')
        
    
    if results:
        return render(request, "search.html", {"results": results})
    else:
        return render(request, "nogame.html", {"query": query})

    