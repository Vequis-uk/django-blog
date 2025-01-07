from . import views
from django.urls import path, include

urlpatterns = [
    path("", views.PostList.as_view(), name='home'),
    path('summernote/', include('django_summernote.urls')),
]