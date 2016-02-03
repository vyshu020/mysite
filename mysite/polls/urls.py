from django.conf.urls import url

from . import views

app_name = 'polls'

urlpatterns = [
    url(r'^about_us', views.about_us,),
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk><question_id>[0-9]+)/$',views.DetailView.as_view(), name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$',views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),

]