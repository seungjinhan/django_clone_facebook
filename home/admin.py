from django.contrib import admin
from django.utils.html import mark_safe
from .models import Photo, Post


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):

    list_display = (
        '__str__', 'get_thumbnail'
    )

    def get_thumbnail(self, obj):
        return mark_safe(f'<img src="{obj.file.url}" width=50 >')

    get_thumbnail.short_description = "Thumbnail"


class PhotoInline(admin.StackedInline):
    model = Photo


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    inlines = (PhotoInline,)

    fieldsets = (
        (None, {
            "fields": (
                "content",
                "user",
                "open",

            ),
        }),
    )

    list_display = (
        "id",
        "content",
        "user",
        "open",
        "created",
        "updated",
    )

    ordering = (
        "-created",
    )

    list_filter = (
        "open",
    )

    search_fields = ('content', 'user__username', 'user__email')
