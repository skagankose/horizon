from django.conf.urls import url
from . import views

urlpatterns = [

    url(r'^$', views.index, name='index'),
    url(r'^twitter/', views.twitter, name='twitter'),

    # add Twitter account via AJAX
    url(r'^userSearch/$', views.userSearch, name='userSearch'),

    # search Twitter account via AJAX
    url(r'^userSearchV2/$', views.userSearchV2, name='userSearchV2'),

    # search Twitter account via AJAX
    url(r'^addTogether/$', views.addTogether, name='addTogether'),

    # page for an account
    url(r'^account/(?P<userName>\w+)/$', views.account, name='account'),



]
