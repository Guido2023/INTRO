from django.urls import path
from .views import BlogListView, BlogCreateView, BlogDetailView, BlogUpdateView, BlogDeleteView

app_name = 'blog'

urlpatterns = [
    path('', BlogListView.as_view(), name='home'),
    path('create/', BlogCreateView.as_view(), name='create'),
    path('<int:id>/', BlogDetailView.as_view(), name='detail'),
    path('<int:id>/update/', BlogUpdateView.as_view(), name='update'),
    path('<int:id>/delete/', BlogDeleteView.as_view(), name='delete'),
]
