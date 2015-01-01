from django.contrib import admin
from polls.models import Poll,Choice
# Register your models here.

#class ChoiceInline(admin.StackedInline):
#	model = Choice
#	extra = 3
class ChoiceInline(admin.TabularInline):
	model = Choice
	extra = 3

class PollAdmin(admin.ModelAdmin):
	#fields = ('question','pub_date')
	fieldsets = [('Question',{'fields':['question']}),('Date information',{'fields':['pub_date'],'classes':['collapse']})]
	list_display = ('question','pub_date','was_published_recently')
	inlines = [ChoiceInline]
	list_filter = ['pub_date']
	search_fields = ['question']
	date_hierarchy = 'pub_date'


admin.site.register(Poll,PollAdmin)
admin.site.register(Choice)