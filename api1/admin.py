from django.contrib import admin

from api1.models import Employee,News1

# Register your models here.
class EmployeeAdmin(admin.ModelAdmin):
    list_display=['name','emp_id','phone_num','salary']


class NewsAdmin1(admin.ModelAdmin):
    list_display=['image','news']


admin.site.register(Employee,EmployeeAdmin)
admin.site.register(News1,NewsAdmin1)