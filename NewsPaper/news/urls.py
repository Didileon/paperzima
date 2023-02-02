from django.contrib import admin
#from django.contrib.sitemaps.views import index
from django.urls import path
from .views import PostsList, PostDetail, PostSearch, SearchDetail, PostDelete, PostCreate, PostUpdate

urlpatterns = [
    path('', PostsList.as_view(), name='posts'),
    path('<int:pk>', PostDetail.as_view()),
    path('search/', PostSearch.as_view()),
    path('<int:pk>', SearchDetail.as_view()),
    path('create/', PostCreate.as_view(), name='post_create'),
    path('<int:pk>/update/', PostUpdate.as_view(), name='post_edit'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),

]
