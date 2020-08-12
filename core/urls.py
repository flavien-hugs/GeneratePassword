from django.conf import settings
from django.urls import path, include
from django.conf.urls.static import static

from gpassword.views import HomeView

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('p', include(
        'gpassword.urls', namespace='gpwd')),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT)
