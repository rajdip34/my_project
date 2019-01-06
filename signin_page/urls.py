
from . import views
from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


urlpatterns = [

    url(r'^$', views.index,name ='index'),
    url(r'^register',views.register,name='register'),

]
urlpatterns += staticfiles_urlpatterns()