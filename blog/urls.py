from django.urls import path
from blog.views import blog_login_view, blog_register_view, BlogHomeView, BlogDetailView, BlogCommentView


app_name = 'blog'
urlpatterns = [
    path('<slug>/comment/', BlogCommentView.as_view(), name='add_comment_url'),
    path('<slug>/', BlogDetailView.as_view(), name = 'post_detail_url'),
    path('', BlogHomeView.as_view(), name='blog_home_url'),
    path('login/', blog_login_view, name='blog_login_url'),
    path('register/', blog_register_view, name='blog_register_url'),
]