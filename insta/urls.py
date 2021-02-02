from django.urls import path
from .views import PostListView,PostDetailView,PostCreateView,PostUpdateView,PostDeleteView,UserList
from .views import home,about
urlpatterns = [
    path('',PostListView.as_view(),name='blog-home'),
    path('about/',about,name='about-home'),
    path('post/<int:pk>/',PostDetailView.as_view(),name='post-detail-view'),
    path('post/<int:pk>/update/',PostUpdateView.as_view(),name='post-update-view'),
    path('post/<int:pk>/delete/',PostDeleteView.as_view(),name='post-delete-view'),
    path('post/new/',PostCreateView.as_view(),name='post-create-view'),
    path('user/<str:username>', UserList.as_view(), name='user-lists'),

]
