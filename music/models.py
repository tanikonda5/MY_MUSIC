from django.db import models
from django.urls import reverse

# Create your models here.
class Album(models.Model):
    title = models.CharField(max_length=50)
    singer = models.CharField(max_length=40)
    year = models.CharField(max_length=4)
    Nos = models.IntegerField(null=True)
    album_logo = models.CharField(max_length=300)
    #album_logo = models.FileField()

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.title + ' - ' + self.singer


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=40)
    song_title = models.CharField(max_length=300)
    is_fav=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('music:detail', kwargs={'pk':self.pk})

    def __str__(self):
        return self.song_title
