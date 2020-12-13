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
    path('add/add_health_clinic',views.add_clinic,name='add_clinic'),
    path('add/add_medical_test',views.add_medical_test,name='add_medical_test'),
    path('add/add_result_type',views.add_result_type,name='add_result_type'),
    path('add/add_result',views.add_result,name='add_result'),
    #path('showall/<int:healthclinic_id>',views.show_mt,name='show_mt'),
    #path('showall/<int:health_clinic_id>/<int:medical_test_id>',views.show_res,name='show_res'),
]
