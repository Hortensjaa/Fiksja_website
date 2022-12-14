from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', include('core.urls')),
    path('admin/', admin.site.urls),
    path('polls/', include('polls.urls')),
    path('records/', include('records.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
