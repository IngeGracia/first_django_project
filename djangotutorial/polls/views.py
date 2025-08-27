from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.db.models import F
from django.urls import reverse
from polls.models import Question, Choice
from django.views import generic


# # def index(request):
# #     return HttpResponse("Hello, world. You're at the polls index.")
# def index(request):
#     latest_question_list = Question.objects.order_by("-pub_date")[:5]
#     context = {"latest_question_list": latest_question_list}
#     return render(request, "index.html", context)


# def detail(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "detail.html", {"question": question})


# def results(request, question_id):
#     response = f"You are looking at the results of question {question_id}"
#     return HttpResponse(response)


# def vote(request, question_id):
#     # return HttpResponse(f"You are voting on question {question_id}")
#     question = get_object_or_404(Question, pk=question_id)
#     try:
#         selected_choice = question.choice_set.get(pk=request.POST["choice"])
#     except(KeyError, Choice.DoesNotExist):
#         # Regresar a la vista detail.html
#         return render(request, "detail.html", {
#             "question": question,
#             "error_message": "You didn't select a choice."
#         })
#     else:
#         selected_choice.votes = F("votes")+1
#         selected_choice.save()
#         # Always return a HttpResponseRedirect after successfully dealing with POST data.
#         # This prevents data from beign posted twice if a user hits the Back button.
#         return HttpResponseRedirect(reverse("results", args=(question.id,)))
    

# def results(request, question_id):
#     question = get_object_or_404(Question, pk=question_id)
#     return render(request, "results.html", {"question": question})

# Vistas Genéricas de Django.
class IndexView(generic.ListView):
    template_name = "index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        """Return the last five published questions"""
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "detail.html"


class ResultsView(generic.DetailView):
    model = Question
    template_name = "results.html"


def vote(request, question_id):
    # return HttpResponse(f"You are voting on question {question_id}")
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except(KeyError, Choice.DoesNotExist):
        # Regresar a la vista detail.html
        return render(request, "detail.html", {
            "question": question,
            "error_message": "You didn't select a choice."
        })
    else:
        selected_choice.votes = F("votes")+1
        selected_choice.save()
        # Always return a HttpResponseRedirect after successfully dealing with POST data.
        # This prevents data from beign posted twice if a user hits the Back button.
        return HttpResponseRedirect(reverse("results", args=(question.id,)))