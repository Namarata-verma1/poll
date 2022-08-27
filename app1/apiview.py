from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .models import Poll,Customer_Class
@csrf_exempt
def questions_view(request):
    if request.method == 'GET':
        return HttpResponse("Not Implemented")
    elif request.method == 'POST':
        question_text = request.POST['question_text']
        Poll.objects.create(question_text=question_text)
        return HttpResponse("Question created", status=201)