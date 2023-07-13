from django.contrib import admin
from . models import Song,Datas,desc,Profile

admin.site.register(Datas)
admin.site.register(Song)
admin.site.register(desc)
admin.site.register(Profile)