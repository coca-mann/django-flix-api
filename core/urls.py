from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('apps.genres.urls')),
    path('api/v1/', include('apps.actors.urls')),
    path('api/v1/', include('apps.movies.urls')),
    path('api/v1/', include('apps.reviews.urls')),
]