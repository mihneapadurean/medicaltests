from django.urls import path

from . import views

app_name='analysis'
urlpatterns=[
    path('',views.home,name='home'),
    path('add',views.add,name='add'),
    path('chat',views.chat,name='chat'),
    path('statistics',views.statistics,name='statistics'),
    path('myprofile',views.myprofile,name='myprofile'),
    path('notifications',views.notifications,name='notifications'),
    path('showall',views.show_all,name='show_all'),
]
