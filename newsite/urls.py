
from django.conf.urls import url,include
from django.contrib import admin
from shortener.views import HomeView,KirrCBView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()), 
    url(r'^b/(?P<shortcode>[\w-]+)/$',KirrCBView.as_view()),
]
