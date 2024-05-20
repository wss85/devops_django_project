from django.urls import path
from .views import (
    UploadFeed,
    Profile,
    Index,
    UploadReply,
    ToggleLike,
    ToggleBookmark,
)  # 수정
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("upload", UploadFeed.as_view()),
    path("profile", Profile.as_view()),
    path("index", Index.as_view()),
    path("reply", UploadReply.as_view()),
    path("like", ToggleLike.as_view()),  # 추가
    path("bookmark", ToggleBookmark.as_view()),  # 추가
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
