from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'music'

urlpatterns=[
    #/music
    path('',views.IndexView.as_view(),name='index'),

    #/music/id
    path('<int:pk>',views.DetailView.as_view(),name='detail'),

    # /music/album/add
    path('album/add/', views.AlbumCreate.as_view(), name='albumAdd'),

    path('album/<int:pk>/delete/', views.AlbumDelete.as_view(), name='delete-album'),

    #/music/register
    path('register/', views.UserFormView.as_view(), name='register'),

    path('song/add/', views.SongCreate.as_view(), name='songAdd'),

    url(r'^logout/$', views.logout_view, name = 'logout'),

]

