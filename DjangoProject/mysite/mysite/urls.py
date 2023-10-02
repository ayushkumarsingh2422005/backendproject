from django.contrib import admin
from django.urls import path
from . import views
handler404 = 'mysite.views.custom_404'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('removepunc', views.removepunc, name='removepunc'),
    path('capfirst', views.capfirst, name='capfirst'),
]
