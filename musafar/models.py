from django.db import models


class Datas(models.Model):
    id = models.BigAutoField
    name = models.CharField(max_length=100)
    desc = models.CharField(max_length=250)
    img = models.ImageField(upload_to="img",default="")

    def __str__(self):
        return self.name
        
class Destination:
    id : int
    name : str
    img : str
    desc :  str

class Song(models.Model):
    title= models.TextField()
    artist= models.TextField()
    image= models.ImageField()
    audio_file = models.FileField(blank=True,null=True)
    paginate_by = 2

    def __str__(self):
        return self.title
