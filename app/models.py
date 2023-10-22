from django.db import models

class Video(models.Model):
    caption = models.CharField(max_length=100, default='some video')
    video = models.FileField(upload_to="video/%y", default='default_video.mp4')
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.caption

    def increment_likes(self):
        self.like += 1
        self.save()

class Comment(models.Model):
    video = models.ForeignKey(Video, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()

    def __str__(self):
        return self.text

