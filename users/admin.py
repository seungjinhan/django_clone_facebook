from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.utils.translation import gettext as _
from . import models


class FriendInline(admin.StackedInline):
    model = models.Friends
    max_num = 1
    min_num = 1
    can_delete = False


class UserAdmin(BaseUserAdmin):

    inlines = (FriendInline,)

    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        (_('Personal Info'), {'fields': (
            'username',
            'avatar',
            'about_me',
            'hobbies',
        )}),
        (
            _('Permissions'),
            {
                'fields': (
                    'is_active',
                    'is_staff',
                    'is_superuser',
                )
            }
        ),
        (_('Important dates'), {'fields': ('last_login',)}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')
        }),
    )

    filter_horizontal = (
        'hobbies',
    )

    search_fields = ('username', 'email')

    ordering = ['id']

    list_display = ['email']

    list_filter = ('is_active',
                   'is_staff',
                   'is_superuser',
                   'hobbies',)


@admin.register(models.Friends)
class FriendsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': (
                'me',
                'friend',
                'is_block',
            ),
        }),
    )

    list_display = (
        'me',
        'count_friends',
        'count_friend_me',
        'is_block',
    )

    filter_horizontal = (
        'friend',
    )

    def count_friends(self, obj):
        return obj.friend.count()
    count_friends.short_description = "친구추가 개수"


admin.site.register(models.User, UserAdmin)
admin.site.register(models.Hobby)
