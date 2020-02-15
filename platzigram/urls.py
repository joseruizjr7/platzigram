from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from platzigram import views as local_views
from posts import views as posts_views


urlpatterns = [
    path('admin/', admin.site.urls),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
