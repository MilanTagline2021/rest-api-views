from django.contrib import admin
from django.urls import path
from func_crud import views
from class_crud import views as w
urlpatterns = [
    path('admin/', admin.site.urls),
    path('stu/', views.student_list),
    path('stu/<int:pk>', views.student_detail),
    path('stud/', w.StudentList.as_view()),
    path('stud/<int:pk>', w.StudentDetail.as_view()),
]
