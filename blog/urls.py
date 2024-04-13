from django.urls import path
from .views import PostListView,PostUpdateView, PostDeleteView,PostCreateView,AddLikesPost,AddLikesComment,AddLikesReply,AddCategoryView    
from . import views
from .views import load_more_posts

urlpatterns = [
    # path('categories/<slug:category_slug>/', views.category, name='category'),
    path('add-category/', AddCategoryView.as_view(), name='add-category'),
    path('category/<str:cats>/', views.CategoryView, name='view-category'),
    path('tags/<slug:tag_slug>/', views.tags, name='tags') , # Example URL pattern
    path('', PostListView.as_view(), name='post-list'),
    path('search/', views.search_view, name='post-search'),
    path('load_more_posts/', load_more_posts, name='load-more-posts'),
    path('post-detail/<uuid:pk>/', views.PostDetailView.as_view(), name='post-detail'),
    path('newpost', PostCreateView.as_view(), name='post-create'),
    path('update/<uuid:pk>/', PostUpdateView.as_view(), name='post-update'),
    # path('like/<uuid:pk>/', AddLike, name='post-likes'),
    path('add-like/<uuid:pk>/', AddLikesPost, name='add-post-likes'),
    path('add-like-comment/<uuid:pk>/', AddLikesComment.as_view(), name='add-comment-likes'),
    path('add-like-reply/<uuid:pk>/', AddLikesReply.as_view(), name='add-reply-likes'),
    # path('comment-like/<uuid:pk>/', AddCommentLike, name='comment-likes'),
    # path('post/<uuid:pk>/comment/create/', CommentCreateView.as_view(), name='comment-create'),
    # path('reply-like/<uuid:pk>/', AddReplyLike, name='reply-likes'),
    # path('comment/<int:pk>/update/', CommentUpdateView.as_view(), name='comment-update'),
    path('<uuid:pk>/delete/', PostDeleteView.as_view(), name='post-delete')
]


