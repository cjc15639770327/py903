from django.conf.urls import url
from . import views

app_name="polls"
urlpatterns=[
    url(r'^$',views.IndexView.as_view(),name="index"),
    url(r'^detail/(\d+)/$',views.DetailView.as_view(),name="detail"),
    url(r'^result/(\d+)/$',views.ResultView.as_view(),name="result")
]