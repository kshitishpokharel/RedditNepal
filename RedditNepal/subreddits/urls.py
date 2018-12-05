from django.urls import path,include
from . import views

app_name = 'subreddits'

urlpatterns=[
    path('',views.ListSubReddit.as_view(),name="all"),
    path('new/',views.CreateSubReddit.as_view(), name="create"),
    path('posts/in/<str:slug>/',views.SingleSubReddit.as_view(),name="single"),
    path('join/<str:slug>/',views.JoinSubReddit.as_view(),name="join"),
    path('leave/<str:slug>/',views.LeaveSubReddit.as_view(),name="leave"),

    # for previous versions
    # path('posts/in/(?P<slug>[-\w]+)/',views.SingleSubReddit.as_view(),name='single'),
    # path('join/(?P<slug>[-\w]+)/',views.JoinSubReddit.as_view(),name='join'),
    # path('leave/(?P<slug>[-\w]+)/',views.LeaveSubReddit.as_view(),name='leave'),
]
