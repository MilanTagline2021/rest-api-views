from django.contrib import admin
from django.db import router
from django.urls import path, include
from func_crud import views
from class_crud import views as w
from generic_crud import views as g
from concreate_crud import views as c
from view_crud import views as v
from model_crud import views as m
from token_auth import auth as t
from jwt_auth import views as j
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

router = DefaultRouter()

# router.register('studentviewAPI', v.StudentViewSet, basename='studentviewAPI')
# router.register('studentModelViewAPI', m.StudentModelViewSet, basename='studentModelViewAPI')
router.register('studentJWTAPI', j.StudentJWTViewSet, basename='studentJWTAPI')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.student_list),
    path('stu/<int:pk>', views.student_detail),
    path('stud/', w.StudentList.as_view()),
    path('stud/<int:pk>', w.StudentDetail.as_view()),
    path('studentapi/', g.StudentListAPI.as_view()),
    path('studentapi/<int:pk>', g.StudentAPI.as_view()),
    path('student/', c.StudentsAPI.as_view()),
    path('student/<int:pk>', c.StudentsAPI_PK.as_view()),
    path('',include(router.urls)),
    path('gettoken/', t.CustomAuthToken.as_view()),
    path('obtain_token/', TokenObtainPairView.as_view(), name='obtain_token'),
    path('refresh_token/', TokenRefreshView.as_view(), name='refresh_token'),
    path('verify_token/', TokenVerifyView.as_view(), name='verify_token'),
]
