from django.contrib import admin

from apps.utils import created, updated, publish, unpublish

from .models import FeaturedImage


class FeaturedImageAdmin (admin.ModelAdmin):
    list_display = ('image', 'link', 'title', 'caption', 'published', 'sortorder', created, updated)
    list_filter = ('published','created','updated')
    search_fields = ('link', 'title', 'caption', 'image')
    list_editable = ('link', 'title', 'caption', 'published', 'sortorder',)
    list_per_page = 50
    save_as = True
    actions = [publish, unpublish]



# register admin objs

admin.site.register (FeaturedImage, FeaturedImageAdmin)

