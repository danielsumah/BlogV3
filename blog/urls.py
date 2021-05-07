from django.urls import path
from blog.views import blog_login_view, blog_logout_view, blog_register_view, BlogHomeView, BlogDetailView, BlogCommentView, BlogCreateView, BlogDeleteView, BlogUpdateView

app_name = 'blog'
urlpatterns = [

    path('<slug>/update_post/', BlogUpdateView.as_view(), name='blog_post_update_url'),
    path('<slug>/delete_post/', BlogDeleteView.as_view(), name='blog_post_delete_url'),
    path('create_post/', BlogCreateView.as_view(), name='blog_post_create_url'),
    path('accounts/logout/', blog_logout_view, name='blog_logout_url'),
    path('accounts/login/', blog_login_view, name='blog_login_url'),
    path('login/', blog_login_view, name='blog_login_url'),
    path('register/', blog_register_view, name='blog_register_url'),
    path('', BlogHomeView.as_view(), name='blog_home_url'),
    path('<slug>/comment/', BlogCommentView.as_view(), name='add_comment_url'),
    path('<slug>/', BlogDetailView.as_view(), name = 'post_detail_url'),
]