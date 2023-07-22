from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import Question

def index(request):
    questions = Question.objects.order_by('-pub_date')
    twenty_four_hours_ago = timezone.now() - timezone.timedelta(hours=24)
    recent_questions = questions.filter(pub_date__gte=twenty_four_hours_ago)
    context = {
        'recent_questions': recent_questions
    }
    return render (request, 'index.html', context)
    #return HttpResponse("Hello, world. You're at the polls index!")