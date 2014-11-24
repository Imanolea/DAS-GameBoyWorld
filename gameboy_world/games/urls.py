from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns(
    '',
    url(r'^$', views.GameIndex.as_view(), name="index"),
    url(r'^(?P<slug>\S+)$', views.GameDetail.as_view(), name="game_detail"),
)