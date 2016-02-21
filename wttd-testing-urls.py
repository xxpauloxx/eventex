
import os 
from django.conf import settings
from django.core.urlresolvers import get_urlconf, set_urlconf, resolve, reverse
from django.conf.urls import url, include 

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'eventex.settings')
# print('Meu ROOT_URLCONFIG é', settings.ROOT_URLCONF)

def index(request):
	pass

def auth(request):
	pass 

def list_(request):
	pass 

def edit(request):
	pass 

def new(request):
	pass 

def delete(request):
	pass 


"""
class GroupConf:
	urlpatterns = [
		url(r'^groups/$', list_, name='list'),
		url(r'^groups/(\d+)/$', edit, name='edit'),
		url(r'^groups/new/$', new, name='new'),
		url(r'^groups/delete/$', delete, name='delete'),
	]
"""

"""class LENDConf:
	def __init__(self, name):
		self.urlpatterns = [
			url(r'^{}/$'.format(name), list_, name='list'),
			url(r'^{}/(\d+)/$'.format(name), edit, name='edit'),
			url(r'^{}/new/$'.format(name), new, name='new'),
			url(r'^{}/delete/$'.format(name), delete, name='delete'),
		]"""


class LENDConf:

	def __init__(self, model):
		self.model = model

		self.urlpatterns = [
			url(r'^$', list_, name='list'),
			url(r'^(\d+)/$', edit, name='edit'),
			url(r'^new/$', new, name='new'),
			url(r'^delete/$', delete, name='delete'),
		]


class MySiteUrlConfig:
	urlpatterns = [
		url(r'^$', index, name='index'),
		url(r'^login/$', auth, kwargs={'action': 'login'}, name='login'),
		url(r'^logout/$', auth, kwargs={'action': 'logout'}, name='logout'),
		# url(r'', include(GroupConf))
		url(r'^groups/', include(LENDConf('groups'), namespace='groups')),
		url(r'^users/', include(LENDConf('users'), namespace='users')),
	]


# print('get_urlconf', get_urlconf())
# print('set_urlconf', MySiteUrlConfig)
set_urlconf(MySiteUrlConfig)

# print('get_urlconf', get_urlconf())

print()
print('Resolve:')
print(resolve('/'))
print(resolve('/login/'))
print(resolve('/logout/'))

print(resolve('/groups/'))
print(resolve('/groups/1/'))
print(resolve('/groups/new/'))
print(resolve('/groups/delete/'))

print(resolve('/users/'))
print(resolve('/users/1/'))
print(resolve('/users/new/'))
print(resolve('/users/delete/'))

print()
print('Reverse:')
print(reverse('index'))
print(reverse('login'))
print(reverse('logout'))

print(reverse('groups:list'))
print(reverse('groups:edit', args=[1]))
print(reverse('groups:new'))
print(reverse('groups:delete'))

print(reverse('users:list'))
print(reverse('users:edit', args=[1]))
print(reverse('users:new'))
print(reverse('users:delete'))