from django.urls import path, include
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework.routers import DefaultRouter

from .views import PostsViewSet, CommentsViewSet, GroupViewSet, FollowViewSet

api_router = DefaultRouter()
api_router.register(r'posts', PostsViewSet, basename='posts')
api_router.register(r'posts/(?P<post_id>\d+)/comments',
                    CommentsViewSet, basename='comments')
api_router.register(r'group', GroupViewSet, basename='group')
api_router.register(r'follow', FollowViewSet, basename='follow')

urlpatterns = [
    path('v1/', include(api_router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
]
