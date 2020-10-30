from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from calculator.models import Question

class IndexView(View):

    def get(self, request, *args, **kwargs):
        ctx = {}
        ctx['questions'] = Question.objects.all()
        return render(request, 'calculator/index.html',ctx)
