from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from education.models import Tasks


def list(request):
    return render(request, 'tasks/list.html', {'tasks': Tasks.objects.all()})


def detail(request, task_id):
    task = get_object_or_404(Tasks, id=task_id)
    return render(request, 'tasks/detail.html', {'task': task})


class TaskCreateView(CreateView):
    model = Tasks
    fields = ['name', 'description', 'due_date', 'course', 'lecture']
    template_name = 'tasks/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:tasks:detail', kwargs={'task_id': self.object.id})
