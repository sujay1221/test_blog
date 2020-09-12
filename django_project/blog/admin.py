from django.contrib import admin
from blog.models import blog

# Register your models here.
class blogAdmin(admin.ModelAdmin):
    list_display = ['title','date_posted']


admin.site.register(blog,blogAdmin)
