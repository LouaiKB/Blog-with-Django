from django.urls import path
from .views import (
	PostListView, 
	PostDetailView,
	PostCreateView
)
from . import views


urlpatterns = [
    path('', PostListView.as_view(), name="Blog-home"),
    path('post/<int:pk>/', PostDetailView.as_view(), name="post-detail"), 
    #Pk refers to the primary key - the id of the post for example Post_1 ..
    path('post/new/', PostCreateView.as_view(), name="post-create" ), 
    path('about/', views.about, name="Blog-about")
]



# ORM : object relational mapper 