from django.contrib import admin



# Register your models here.
from app.models import *
class WebpageCustomView(admin.ModelAdmin):
    list_display=['topic_name','name','url']
    list_editable=['name']
    list_display_links=['topic_name','url']
    #list_per_page=2
    search_fields=['name']
    list_filter=['name','topic_name']
admin.site.register(Topic)
admin.site.register(Webpage,WebpageCustomView)
admin.site.register(AccessRecords)

