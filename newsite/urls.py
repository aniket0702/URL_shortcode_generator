
from django.conf.urls import url,include
from django.contrib import admin
from shortener.views import HomeView,URLRedirectView
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',HomeView.as_view()),
    url(r'^(?P<shortcode>[\w-]+)/$',URLRedirectView.as_view(),name = "shortcode"),
]
