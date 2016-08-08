"""skinneyit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$',  views.online_wel, name = 'online_wel'),
    url(r'^info/$',  views.store_post_create, name = 'store_post_create'),
    url(r'^br_2/$',  views.br_post_create, name = 'br_post_create'),
    url(r'^mc_3/$',  views.mc_post_create, name = 'mc_post_create'),
    url(r'^ml_4/$',  views.ml_post_create, name = 'ml_post_create'),
    url(r'^nm_5/$',  views.nm_post_create, name = 'nm_post_create'),
    url(r'^sc_6/$',  views.sc_post_create, name = 'sc_post_create'),
    url(r'^wfnp_7/$',  views.wfnp_post_create, name = 'wfnp_post_create'),
    url(r'^addi_8/$',  views.addtional_fields, name = 'addtional_fields'),
    url(r'^list/$',  views.online_list, name = 'online_list'),
    url(r'^detail/(?P<pk>[0-9]+)/$',  views.online_detail, name = 'online_detail'),
    url(r'^cancel_del/$',  views.online_del, name = 'online_del'),
	
    url(r'^login/$', views.user_login, name = 'user_login'),
    url(r'^logout/$', views.user_logout, name = 'user_logout'),
    url(r'^check/$', views.customer_check, name = 'customer_check'),
    url(r'^customer/(?P<pk>[0-9]+)/$', views.customer_detail, name = 'customer_detail'),
    #url(r'^customer_list/$', views.customer_list, name = 'customer_list'),
]
