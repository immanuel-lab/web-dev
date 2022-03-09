from django.contrib import admin
from.models import Editor
from app1.models import Destination, Form

# Register your models here.
class DestinationAdmin(admin.ModelAdmin):
    list_display=['name','image','price','description','offer']


class FormAdmin(admin.ModelAdmin):
    list_display=['name','email_id','gender','intrest','region','feedback']

admin.site.register(Destination,DestinationAdmin)
admin.site.register(Form,FormAdmin)
admin.site.register(Editor)
