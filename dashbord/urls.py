from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='dashbord-home'),
    path('workspace/<str:work>',views.workspace,name='dashbord-workspace'),
    path('report/<str:report>',views.report,name='dashbord-report'),
    # path('history_of_playlist/',views.playlist,name='dashbord-playlist'),
    # path('history_of_playlist/',views.postView.as_view(),name='dashbord-playlist'),
    path('playlist/create/',views.create_playlist,name='dashbord-create'),
    path('playlist/create/select_report/',views.select_report,name='dashbord-create-report'),
    # path('steps_for_register/', views.register_steps, name='register'),
    # path('login', views.user_login, name='login'),
    # path('logout', views.user_logout, name='logout'),
    path('user-infos/', views.user_informations, name='userinfos'),
    path('change_pass/', views.pass_change, name='change_pass'),
]