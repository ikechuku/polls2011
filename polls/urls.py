from django.conf.urls import url
from django.contrib import admin
from . import views as myview
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    url(r'^$', myview.home, name="home"),
    url(r'^polling-result/$', myview.puResult, name="puresult"),
    url(r'^polling-get/$', myview.puGet, name="puget"),
    url(r'^parties/$', myview.party, name="parties"),
    url(r'^manage/$', myview.addpollingresult, name="manages"),
]
urlpatterns+=staticfiles_urlpatterns()
# urlpatterns+=static(settings)