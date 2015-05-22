from django.conf.urls import patterns, include, url
from web import views

urlpatterns = patterns('',
	url(r'^$', views.home, name='home'),
	url(r'^login/$', views.loginApp, name='login'),
	url(r'^logout/$', views.logoutApp, name='logout'),
	url(r'^createUser/$', views.createUser, name='signin'),
	url(r'^user/$', views.user, name='user'),
	url(r'^postTicket/$', views.postTicket, name='postTicket'),
	url(r'^postComment/$', views.postComment, name='postComment'),
	url(r'^deleteComment/$', views.deleteComment, name='deleteComment'),
	url(r'^deleteTicket/$', views.deleteTicket, name='deleteTicket'),
	url(r'^changeLang/$', views.changeLanguage, name='changeLang'),
	url(r'^updateTicket/$', views.updateTicket, name='updateTicket'),
	url(r'^searchTicket/$', views.searchTicket, name='searchTicket'),
)