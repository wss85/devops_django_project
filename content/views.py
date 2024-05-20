from uuid import uuid4
from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Feed, Reply, Like, Bookmark
from user.models import User
import os
from config.settings import MEDIA_ROOT
from django.views.decorators.csrf import csrf_exempt  # 403 Forbidden Error Sol
from django.utils.decorators import method_decorator  # 403 Forbidden Error Sol


class Index(APIView):
    def get(self, request):
        email = request.session.get("email", None)

        if email is None:
            return render(request, "user/login.html")

        user = User.objects.filter(email=email).first()

        if user is None:
            return render(request, "user/login.html")

        feed_object_list = Feed.objects.all().order_by(
            "-id"
        )  # select  * from content_feed;
        feed_list = []

        for feed in feed_object_list:
            user = User.objects.filter(email=feed.email).first()
            reply_object_list = Reply.objects.filter(feed_id=feed.id)
            reply_list = []
            for reply in reply_object_list:
                user = User.objects.filter(email=reply.email).first()
                reply_list.append(
                    dict(reply_content=reply.reply_content, nickname=user.nickname)
                )
            like_count = Like.objects.filter(feed_id=feed.id, is_like=True).count()
            is_liked = Like.objects.filter(
                feed_id=feed.id, email=email, is_like=True
            ).exists()
            is_marked = Bookmark.objects.filter(
                feed_id=feed.id, email=email, is_marked=True
            ).exists()
            feed_list.append(
                dict(
                    id=feed.id,
                    image=feed.image,
                    content=feed.content,
                    like_count=like_count,
                    profile_image=user.profile_image,
                    nickname=user.nickname,
                    reply_list=reply_list,
                    is_liked=is_liked,
                    is_marked=is_marked,
                )
            )

        return render(
            request, "instagram/index.html", context=dict(feeds=feed_list, user=user)
        )


@method_decorator(csrf_exempt, name="dispatch")  # 403 Forbidden Error Sol
class UploadFeed(APIView):
    def post(self, request):

        file = request.FILES["file"]

        uuid_name = uuid4().hex
        save_path = os.path.join(MEDIA_ROOT, uuid_name)

        with open(save_path, "wb+") as destination:
            for chunk in file.chunks():
                destination.write(chunk)

        content = request.data.get("content")
        image = uuid_name
        email = request.session.get("email")

        Feed.objects.create(
            content=content,
            image=image,
            email=email,
        )
        return Response(status=200)


@method_decorator(csrf_exempt, name="dispatch")  # 403 Forbidden Error Sol
class Profile(APIView):
    def get(self, request):
        email = request.session.get("email", None)
        if email is None:
            return HttpResponseRedirect("/user/login/")

        user = User.objects.filter(email=email).first()
        if user is None:
            return HttpResponseRedirect("/user/login/")

        feed_list = Feed.objects.filter(email=email).order_by("-id")
        like_list = list(
            Like.objects.filter(email=email, is_like=True).values_list(
                "feed_id", flat=True
            )
        )
        like_feed_list = Feed.objects.filter(id__in=like_list).order_by("-id")
        bookmark_list = list(
            Bookmark.objects.filter(email=email, is_marked=True).values_list(
                "feed_id", flat=True
            )
        )
        bookmark_feed_list = Feed.objects.filter(id__in=bookmark_list).order_by("-id")

        return render(
            request,
            "content/profile.html",
            context=dict(
                user=user,
                feed_list=feed_list,
                like_feed_list=like_feed_list,
                bookmark_feed_list=bookmark_feed_list,
            ),
        )


@method_decorator(csrf_exempt, name="dispatch")  # 403 Forbidden Error Sol
class UploadReply(APIView):
    def post(self, request):
        feed_id = request.data.get("feed_id", None)
        reply_content = request.data.get("reply_content", None)
        email = request.session.get("email", None)

        Reply.objects.create(feed_id=feed_id, reply_content=reply_content, email=email)

        return Response(status=200)


@method_decorator(csrf_exempt, name="dispatch")  # 403 Forbidden Error Sol
class ToggleLike(APIView):
    def post(self, request):
        feed_id = request.data.get("feed_id", None)
        email = request.session.get("email", None)

        like = Like.objects.filter(feed_id=feed_id, email=email).first()

        if like:
            is_like = like.is_like
            like.is_like = not is_like
            like.save()
        else:
            is_like = True
            Like.objects.create(feed_id=feed_id, is_like=is_like, email=email)

        # 좋아요 수 계산
        like_count = Like.objects.filter(feed_id=feed_id, is_like=True).count()
        return Response({"like_count": like_count, "is_like": not is_like}, status=200)


@method_decorator(csrf_exempt, name="dispatch")  # 403 Forbidden Error Sol
class ToggleBookmark(APIView):
    def post(self, request):
        feed_id = request.data.get("feed_id", None)
        email = request.session.get("email", None)

        bookmark = Bookmark.objects.filter(feed_id=feed_id, email=email).first()

        if bookmark:
            is_marked = not bookmark.is_marked
            bookmark.is_marked = is_marked
            bookmark.save()
        else:
            is_marked = True
            Bookmark.objects.create(feed_id=feed_id, is_marked=is_marked, email=email)

        return Response({"is_marked": is_marked}, status=200)
