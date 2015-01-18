from django.contrib import admin
from . import models
from django_markdown.admin import MarkdownModelAdmin

class GameAdmin(MarkdownModelAdmin):
	prepopulated_fields = {'slug': ('title',)}

admin.site.register(models.Game, GameAdmin)