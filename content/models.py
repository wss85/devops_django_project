from django.db import models


class Feed(models.Model):
    content = models.TextField()  # 글 내용
    image = models.TextField()  # 피드 이미지 경로
    email = models.EmailField(default="")  # 글쓴이의 이메일


class Like(models.Model):
    feed_id = models.IntegerField(default=0)  # 좋아요가 속한 피드의 id
    email = models.EmailField(default="")  # 좋아요를 누른 사용자의 이메일
    is_like = models.BooleanField(default=True)  # 좋아요 여부


class Reply(models.Model):
    feed_id = models.IntegerField(default=0)  # 댓글이 속한 피드의 id
    email = models.EmailField(default="")  # 댓글 작성자의 이메일
    reply_content = models.TextField()  # 댓글 내용


class Bookmark(models.Model):
    feed_id = models.IntegerField(default=0)  # 북마크가 속한 피드의 id
    email = models.EmailField(default="")  # 북마크한 사용자의 이메일
    is_marked = models.BooleanField(default=True)  # 북마크 여부
