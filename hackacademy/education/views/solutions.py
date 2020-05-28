from django.shortcuts import render, get_object_or_404
from django.views.generic import CreateView
from django.urls import reverse_lazy

from education.models import Solutions


def list(request):
    return render(request, 'solutions/list.html', {'solutions': Solutions.objects.all()})


def detail(request, solutions_id):
    solutions = get_object_or_404(Solutions, id=solutions_id)
    return render(request, 'solutions/detail.html', {'solution': solutions})


class SolutionCreateView(CreateView):
    model = Solutions
    fields = ['task', 'date', 'url']
    template_name = 'solutions/create.html'

    def get_success_url(self, **kwargs):
        return reverse_lazy('education:solutions:detail', kwargs={'solution_id': self.object.id})
