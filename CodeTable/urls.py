from django.conf.urls import url

from . import views

app_name = 'CodeTable'
urlpatterns = [
	# ex: /
	url(r'^$', views.index, name='index'),
	# ex: /ajSkHb
	url(r'^(?P<code_id>[-\w]+)$', views.savedCodeView, name='saved-code'),
	# ex: /compile/
	url(r'^compile/$', views.compileCode, name='compile'),
	# ex: /run/
	url(r'^run/$', views.runCode, name='run'),
]

