from django.urls import path, include

from education.views import index, lectures, courses, tasks, solutions


app_name = 'education'

courses_patterns = [
    path('', courses.list, name='list'),
    path('<int:course_id>/', courses.detail, name='detail'),
    path('new/', courses.CourseCreateView.as_view(), name='create'),
]
lectures_patterns = [
    path('', lectures.list, name='list'),
    path('<int:lecture_id>/', lectures.detail, name='detail'),
    path('new/', lectures.LectureCreateView.as_view(), name='create'),
]

tasks_patterns = [
    path('', tasks.list, name='list'),
    path('<int:task_id>/', tasks.detail, name='detail'),
    path('new/', tasks.TaskCreateView.as_view(), name='create'),
]

solutions_patterns = [
    path('', solutions.list, name='list'),
    path('<int:solution_id>/', solutions.detail, name='detail'),
    path('new/', solutions.SolutionCreateView.as_view(), name='create'),
]

urlpatterns = [
    path('', index, name='index'),
    path('courses/', include((courses_patterns, 'courses'))),
    path('lectures/', include((lectures_patterns, 'lectures'))),
    path('tasks/', include((tasks_patterns, 'tasks'))),
    path('solutions/', include((solutions_patterns, 'solutions')))
]
