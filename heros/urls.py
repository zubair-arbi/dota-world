from django.conf.urls import url

from heros import views


urlpatterns = [
    url(r'^$', views.heros, name='view_heros'),
]
