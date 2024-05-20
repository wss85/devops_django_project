from django.contrib import admin
from .models import Feed, Like, Reply, Bookmark


@admin.register(Feed)
class FeedAdmin(admin.ModelAdmin):
    pass


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    pass


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    pass


@admin.register(Bookmark)
class BookmarkAdmin(admin.ModelAdmin):
    pass
