'''from django.conf.urls import patterns, include, url'''
from django.conf.urls import *
from django.contrib import admin
from mana import views


# """
#     cmdb 就是工程里面的app,把视图放在app里面，从里面导入更合适
# """
# '''urlpatterns = patterns('',
#     # Examples:
#     # url(r'^$', 'mysite.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#
#     url(r'^admin/', include(admin.site.urls)),
# )'''
#
# urlpatterns = [
#     url(r'^admin/', include(admin.site.urls)),
#     url(r'^home', views.home),
#
#     url(r'^login', views.login),
#     url(r'^detail-(\d+).html', views.detail), # 此处会将(\d+)匹配到的id传给detail函数
#     url(r'^orm/', include('app01.urls'))
#     # ... your url patterns
# ]

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^enter', views.enter),
    url(r'^register', views.register),
    url(r'^handle', views.handle),
    url(r'^host_del-(\d+)', views.host_del),
    url(r'^host_detail-(\d+)', views.host_detail),
    url(r'^edit-(\d+)', views.edit),
    # url(r'^detail-(\d+).html', views.detail), # 此处会将(\d+)匹配到的id传给detail函数
    # ... your url patterns
]