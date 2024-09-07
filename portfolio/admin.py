from django.contrib import admin
from .models import AboutSection, PortfolioItem, Post, Comment,Contact


class AboutSectionAdmin(admin.ModelAdmin):
    list_display = ('title',)
    search_fields = ('title',)

admin.site.register(AboutSection, AboutSectionAdmin)


@admin.register(PortfolioItem)
class PortfolioItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'client', 'completed_date')
    search_fields = ('title', 'client')
    list_filter = ('completed_date',)
    ordering = ('-completed_date',)
    readonly_fields = ('social_links',)
    fields = ('title', 'description', 'client', 'website', 'completed_date', 'image', 'detail_image', 'social_links')

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return self.readonly_fields + ('image', 'detail_image')
        return self.readonly_fields
    


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'updated_at', 'views')
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'subject', 'post', 'created_at')
    search_fields = ('name', 'email', 'subject', 'message')


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["first_name", "email"]





