from django.contrib import admin
from .models import  Comment
from .models import GoldenChance
from .models import Post
from .models import Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Post,PostAdmin)
admin.site.register(GoldenChance)
admin.site.register(Comment)
admin.site.register(Contact)




# Register your models here.
