from django.db import models
from django.core.urlresolvers import reverse

class GameQuerySet(models.QuerySet):
	def published(self):
		return self.filter(publish=True)

class Game(models.Model):
	title = models.CharField(max_length=200)
	description = models.TextField()
	slug = models.SlugField(max_length=200, unique=True)
	imageurl = models.URLField(max_length=200)
	downloadurl = models.URLField(max_length=200)
	ingameurl = models.URLField(max_length=200)

	objects = GameQuerySet.as_manager()

	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse("game_detail", kwargs={"slug": self.slug})

	class Meta:
		verbose_name = "Game"
		verbose_name_plural = "Games"
		ordering = ["-title"]
