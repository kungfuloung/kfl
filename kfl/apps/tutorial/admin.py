from django.contrib import admin


from Tutorial.models import VideoTutorial, TutorialCategory



class VideoTutorialAdmin(admin.ModelAdmin):
	list_display = ('category', 
					'season',
					'episode',)
admin.site.register(VideoTutorial, VideoTutorialAdmin)


class TutorialCategoryAdmin(admin.ModelAdmin):
	list_display = ('name',)
admin.site.register(TutorialCategory, TutorialCategoryAdmin)	

# Register your models here.
