from django.contrib import admin

from bookmark.models import Bookmark

# Register your models here.
# Bookmark zmffotmrk Admin사이트에서 
class BookmarkAdmin(admin.ModelAdmin):
    list_display = ('title','url')
    
from bookmark.models import Bookmark

