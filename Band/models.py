from django.db import models

# Create your models here.
class Member(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)

class Album(models.Model):
    title = models.CharField(max_length=100)
    release_date = models.DateField()
    cover_image = models.ImageField(upload_to='album_covers/')
    members = models.ManyToManyField(Member)

class Song(models.Model):
    title = models.CharField(max_length=100)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file = models.FileField(upload_to='songs/')