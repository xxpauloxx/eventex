from django.contrib import admin
from eventex.core.models import Speaker, Contact, Talk, Course


class ContactInLine(admin.TabularInline):
    model = Contact
    extra = 1


class SpeakerModelAdmin(admin.ModelAdmin):
    inlines = [ContactInLine]
    prepopulated_fields = {'slug': ('name',)}
    list_display = ['name', 'photo_img', 'website_link', 'email', 'phone']

    def website_link(self, obj):
        return '<a href="{0}" target="_blank">{0}</a>'.format(obj.website)

    website_link.allow_tags = True
    website_link.short_description = 'website'

    def photo_img(self, obj):
        return '<img width="32px" src="{}">'.format(obj.photo)

    photo_img.allow_tags = True
    photo_img.short_description = 'foto'

    def email(self, obj):
        return obj.contact_set.emails().first()

    email.short_description = 'e-mail'

    def phone(self, obj):
        return obj.contact_set.phones().first()

    phone.short_description = 'telefone'


class ActivityModelAdmin(admin.ModelAdmin):
    list_display = ['title', 'start', 'get_speakers']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.select_related()

    def get_speakers(self, obj):
        return ', '.join([speaker.name for speaker in obj.speakers.all()])

    get_speakers.short_description = 'palestrante(s)'


class TalkModelAdmin(ActivityModelAdmin):
    list_display = ['title', 'start', 'get_speakers']

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.filter(course=None)


admin.site.register(Speaker, SpeakerModelAdmin)
admin.site.register(Talk, TalkModelAdmin)
admin.site.register(Course, ActivityModelAdmin)