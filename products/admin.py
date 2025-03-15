from django.contrib import admin
from .models import Catagory , Product , File



@admin.register(Catagory)
class CatagoryAdmin(admin.ModelAdmin):
    list_display = ['parent','title','is_enable','created_time']
    list_filter = ['is_enable','parent']
    search_fields = ['title']


class FileInlineAdmin(admin.StackedInline):
    model = File
    fields =['title','file','is_enable','file_type']
    extra = 0


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['title','is_enable','created_time']
    list_filter = ['is_enable']
    search_fields = ['title']
    filter_horizontal = ['catagories']
    inlines = [FileInlineAdmin]
