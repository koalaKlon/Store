from django.urls import path
from . import views

#app_name = 'clothing'

urlpatterns = [
    path('', views.index, name='home'),
    path('basket', views.product, name='product'),
    path('register', views.register_request, name='register'),
    path('login', views.login_request, name='login'),
    path('logout', views.logout_request, name='logout'),

    path(r'^$', views.product_list, name='product_list'),
    path(r'^(?P<category_slug>[-\w]+)/$', views.product_list, name='product_list_by_category'),
    path(r'^(?P<id>\d+)/(?P<slug>[-\w]+)/$', views.product_detail, name='product_detail'),
]
