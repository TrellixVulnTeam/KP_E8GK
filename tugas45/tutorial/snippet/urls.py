from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippet import views

urlpatterns = [
    path('snippet/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippet/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippet/<int:pk>/highlight/',
         views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
]

urlpatterns = format_suffix_patterns(urlpatterns)