from django.contrib import admin
from django.urls import path
# from platzigram import views as local_views
# from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
]
