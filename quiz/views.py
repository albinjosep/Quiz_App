from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Question, UserSubmission, QuizSession
import random
import json

def start_quiz(request):
    session = QuizSession.objects.create()  # Create a new quiz session
    return JsonResponse({"message": "Quiz session started.", "session_id": session.id})

@csrf_exempt
def start_session(request):
    UserSubmission.objects.all().delete()  # Clear previous submissions
    return JsonResponse({"message": "New session started."})

def get_random_question(request):
    questions = Question.objects.all()
    if not questions:
        return JsonResponse({"error": "No questions available."}, status=404)
    question = random.choice(questions)
    return JsonResponse({
        "id": question.id,
        "text": question.text,
        "options": {
            "a": question.option_a,
            "b": question.option_b,
            "c": question.option_c,
            "d": question.option_d,
        }
    })

@csrf_exempt
def submit_answer(request):
    if request.method == "POST":
        data = json.loads(request.body)  # Using JSON for POST data
        question_id = data.get("question_id")
        selected_option = data.get("selected_option")
        try:
            question = Question.objects.get(id=question_id)
            is_correct = question.correct_option == selected_option
            UserSubmission.objects.create(
                question=question,
                selected_option=selected_option,
                is_correct=is_correct
            )
            return JsonResponse({"is_correct": is_correct})
        except Question.DoesNotExist:
            return JsonResponse({"error": "Question not found."}, status=404)

def results(request):
    submissions = UserSubmission.objects.all()
    total = submissions.count()
    correct = submissions.filter(is_correct=True).count()
    incorrect = total - correct
    return JsonResponse({
        "total": total,
        "correct": correct,
        "incorrect": incorrect,
        "details": [
            {
                "question": sub.question.text,
                "selected_option": sub.selected_option,
                "is_correct": sub.is_correct
            }
            for sub in submissions
        ]
    })
