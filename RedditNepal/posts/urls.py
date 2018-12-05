from django.urls import path,include
from . import views

app_name = 'posts'

urlpatterns = [
    path('',views.PostList.as_view(),name='all'),
    path('new/',views.CreatePost.as_view(),name='create'),
    path('by/<str:username>)/',views.UserPosts.as_view(),name='for_user'),
    path('by/(str:username)/(pk:int)/',views.PostDetail.as_view(),name = 'single'),
    path('delete/(pk:int)/',views.DeletePost.as_view(),name = 'delete'),

    #for previous versions
    # path('by/(?P<username>[-\w])/',views.UserPosts.as_view(),name='for_user'),
    # path('by/(?P<username>[-\w])/(?P<pk>\d+)/',views.PostDetail.as_view(),name = 'single'),
    # path('delete/(?P<pk>\d+)/',views.DeletePost.as_view(),name = 'delete'),
]
