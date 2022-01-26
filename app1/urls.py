from django.urls import path
from .import views

app_name = 'app1'

urlpatterns = [
    path('', views.topView.as_view(), name='top'),
    path('Reception1', views.Reception1View.as_view(), name='Reception1'),
    path('Reception2', views.Reception2View.as_view(), name='Reception2'),
    path('Reception3', views.Reception3View.as_view(), name='Reception3'),
]
