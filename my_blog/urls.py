from django.conf.urls import include
from django.conf.urls import url
from django.contrib import admin
from article import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'my_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    
    url(r'^$', views.home, name = 'home'),
    url(r'^(?P<id>\d+)/$', views.detail, name='detail'),
    url(r'^archives/$', views.archives, name = 'archives'),
   
    url(r'^tag(?P<tag>\w+)/$', views.search_tag, name = 'search_tag'),
    url(r'^search/$',views.blog_search, name = 'search'),
    url(r'^admin/', admin.site.urls),
    url(r'^page(?P<id>\w+)/$', views.pages, name = 'pages'),  


]


