from django.views import generic
from . import models

class GameIndex(generic.ListView):
	queryset = models.Game.objects.order_by('title')
	template_name = "home.html"
	paginate_by = 1

class GameDetail(generic.DetailView):
	model = models.Game
	template_name = "post.html"