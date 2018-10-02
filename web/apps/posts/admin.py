from django.contrib import admin
from .models import Post

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display = ["title", "timestamp", "updated"]
    list_display_links = ["updated"]
    list_filter = ["updated", "timestamp"]
    search_fields = ["content"]
    list_editable = ["title"]

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
