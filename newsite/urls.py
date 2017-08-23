
from django.conf.urls import url,include
from django.contrib import admin
from shortener.views import kirr_redirect_view,KirrCBView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^a/(?P<shortcode>[\w-]+)/$',kirr_redirect_view),
    url(r'^b/(?P<shortcode>[\w-]+)/$',KirrCBView.as_view()),
]
