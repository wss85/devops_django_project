from django.contrib import admin
from django.urls import path, include
from content.views import Index
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("admin/", admin.site.urls),
    path("index/", Index.as_view()),
    path("content/", include("content.urls")),
    path("user/", include("user.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
