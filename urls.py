from django.conf.urls import url
from django.contrib import admin
from article import views
from django.conf.urls import include
urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name = 'archives'),
    
    url(r'^page(?P<id>\d+)/$', views.pages, name = 'pages'),    


]


