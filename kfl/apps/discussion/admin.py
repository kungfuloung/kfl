from django.contrib import admin

from discussion.models import ThreadCategory, ThreadContent, Thread, Reply



class ThreadContentAdmin(admin.ModelAdmin):
    list_display = ('title',
                    'of_thread',)               
    # list_display = ('user',)

admin.site.register(ThreadContent, ThreadContentAdmin)



class ThreadCategoryAdmin(admin.ModelAdmin):
    list_display = ('pid',
                    'title_CN',)
                
    # list_display = ('user',)

admin.site.register(ThreadCategory, ThreadCategoryAdmin)



class ThreadAdmin(admin.ModelAdmin):
    list_display = ('id',)
                
    # list_display = ('user',)

admin.site.register(Thread, ThreadAdmin)


class ReplyAdmin(admin.ModelAdmin):
    list_display = ('posted_by',
                    'following_thread',
                    'following_reply',)
                
    # list_display = ('user',)

admin.site.register(Reply, ReplyAdmin)
