from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='dashbord-home'),
    path('workspace/<str:work>',views.workspace,name='dashbord-workspace'),
    path('report/<str:report>',views.report,name='dashbord-report'),
    path('history_of_playlist/',views.playlist,name='dashbord-playlist'),
    # path('history_of_playlist/',views.postView.as_view(),name='dashbord-playlist'),
    path('playlist/create/',views.create_playlist,name='dashbord-create'),
]