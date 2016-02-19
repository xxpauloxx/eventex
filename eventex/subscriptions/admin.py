from django.contrib import admin
from django.utils.timezone import now
from eventex.subscriptions.models import Subscription


class SubscriptionModelAdmin(admin.ModelAdmin):
	date_hierarchy = 'created_at'
	list_display = ('name', 'email', 'phone', 'cpf', 'created_at', 'subscribed_today', 'paid')
	search_fields = ('name', 'email', 'phone', 'cpf', 'created_at')
	list_filter = ('created_at', 'paid')

	def subscribed_today(self, obj):
		return obj.created_at == now().date()

	subscribed_today.short_description = 'inscrito hoje?'
	subscribed_today.boolean = True


admin.site.register(Subscription, SubscriptionModelAdmin)
admin.site.site_header = 'Eventex'

