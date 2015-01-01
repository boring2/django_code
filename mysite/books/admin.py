from django.contrib import admin
from books.models import Book,Publisher,Author
# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
	list_display = ('first_name','last_name','email')
	search_fields = ('first_name','last_name')

class BookAdmin(admin.ModelAdmin):
	list_display = ('title', 'publiser', 'publication_date')
	list_filter = ('publication_date','publiser')
	date_hierarchy = 'publication_date'
	ordering = ('-publication_date',)
	fields = ('title', 'authors', 'publiser', 'publication_date', 'num_pages')
	filter_horizontal = ('authors',)
#	filter_vertical = ('authors',)
	raw_id_fields = ('publiser',)
admin.site.register(Book,BookAdmin)
admin.site.register(Publisher)
admin.site.register(Author,AuthorAdmin)
