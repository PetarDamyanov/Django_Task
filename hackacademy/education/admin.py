from django.contrib import admin
from education.models import Course, Lecture, Tasks, Solutions


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'get_duration', 'start_date', 'end_date')

    def get_duration(self, obj):
        if obj.duration:
            return f'{obj.duration.days // 7} weeks'

        return 'N/A'

    get_duration.short_description = 'Duration'


@admin.register(Lecture)
class LectureAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'week', 'course', 'url')


@admin.register(Tasks)
class TaskAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'due_date', 'course', 'lecture')


@admin.register(Solutions)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('get_task', 'get_description', 'get_lecture', 'date', 'url')

    def get_description(self, obj):
        return obj.task.description

    def get_lecture(self, obj):
        return obj.task.lecture

    def get_task(self, obj):
        return obj.task.name

    get_description.short_description = 'description'

    get_lecture.short_description = 'lecture'

    get_task.short_description = 'name'
