from django.shortcuts import get_object_or_404, render

# from .models import Question EXAMPLE


# ...
def index(request):
    # question = get_object_or_404(Question, pk=question_id) EXAMPLE
    context = {

    }
    return render(request, "puckpuzzle/index.html", {"context": context})
