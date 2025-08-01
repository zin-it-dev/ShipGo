from django.urls import path, include
from rest_framework_nested import routers

from .resources import UserViewSet, CategoryViewSet, CourseViewSet, LessonViewSet, TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'categories', CategoryViewSet, basename='category')
router.register(r'courses', CourseViewSet, basename='course')

courses_router = routers.NestedSimpleRouter(router, r'courses', lookup='course')
courses_router.register(r'lessons', LessonViewSet, basename='course-lessons')


urlpatterns = [
    path(r'', include(router.urls)),
    path(r'', include(courses_router.urls)),
    
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]