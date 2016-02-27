
from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk, Course


class ContactInline(admin.TabularInline):
	model = Contact
	extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
	inlines = [ContactInline]
	prepopulated_fields = {'slug': ('name', )}
	list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

	def website_link(self, obj):
		return '<a href="{0}">{0}</a>'.format(obj.website)

	website_link.allow_tags=True
	website_link.short_description = 'Website'

	def photo_img(self, obj):
		return '<img width="32px" src={}>'.format(obj.photo)

	photo_img.allow_tags=True
	photo_img.short_description='Foto'

	def email(self, obj):
		# return Contact.objects.filter(kind=Contact.EMAIL, speaker=obj).first()
		# return Contact.phones.filter(speaker=obj).first()
		# return obj.contact_set(manager='emails').first()
		return obj.contact_set.emails().first()

	email.short_description = 'e-mail'


	def phone(self, obj):
		# return Contact.objects.filter(kind=Contact.PHONE, speaker=obj).first()
		# return Contact.phones.filter(speaker=obj).first()
		# return obj.contact_set(manager='phones').first()
		return obj.contact_set.phones().first()

	phone.short_description = 'telefone'


class TalkModelAdmin(admin.ModelAdmin):
	def get_queryset(self, request):
		qs = super().get_queryset(request)
		return qs.filter(course=None)


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course)