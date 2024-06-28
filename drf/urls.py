from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import BlogViewSet

blog_list = BlogViewSet.as_view({
	'get': 'list',
    'post': 'create'
})

blog_detail = BlogViewSet.as_view({
	'get': 'retrieve',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
	path('blog/', blog_list),
    path('blog/<int:pk>/', blog_detail),
]