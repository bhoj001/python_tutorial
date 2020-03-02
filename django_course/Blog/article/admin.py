from django.contrib import admin
from .models import Post,AskQuestion
# Register your models here.

# admin.site.register(Post)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title',  'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    
admin.site.register(Post, PostAdmin)



class AskQuestionAdmin(admin.ModelAdmin):
    list_display = ('title','created_on')
    search_fields = ('title',)

admin.site.register(AskQuestion, AskQuestionAdmin)