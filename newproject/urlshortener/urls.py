from django.urls import path, include

from . import views


urlpatterns = [
	path('api/', include('urlshortener.api.urls')),
	path('<str:short>/', views.redirect_url),
	path('', views.home)
]
