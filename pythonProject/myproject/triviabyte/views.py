from django.shortcuts import render
from .questions import questions_data
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse

def triviabyte_view(request):
    # Extracting unique categories from questions_data
    categories = set(question['category'] for question in questions_data)
    print("categories:", categories)  # Print out categories for debugging
    context = {'categories': categories}
    return render(request, 'index.html', context)

def music_view(request):
    return render(request, 'music.html')

def science_view(request):
    return render(request, 'science.html')

def quiz_view(request):
    return render(request, 'quiz.html')

def get_quiz(request):
    if request.method == 'POST':
        category = request.POST.get('category')
        if category:
            # Filter questions based on the selected category
            filtered_questions = [question for question in questions_data if question['category'] == category]
            context = {'category': category, 'questions': filtered_questions}
            return render(request, 'quiz.html', context)
    return render(request, 'index.html')


@csrf_exempt
def calculate_questions_score(request):
    if request.method == 'POST':
        try:
            selected_answers = request.POST.getlist('selected_answers[]')
            correct_answers = [question['correct_answer'] for question in questions_data]

            score = calculate_score(selected_answers, correct_answers)

            return JsonResponse({'score': score})

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)


def calculate_score(selected_answers, correct_answers):
    # Calculate the score based on selected and correct answers
    correct_count = sum(1 for selected, correct in zip(selected_answers, correct_answers) if selected == correct)
    total_questions = len(correct_answers)
    score = (correct_count / total_questions) * 100
    return score


@csrf_exempt
def submit_answers(request):
    if request.method == 'POST':
        try:
            selected_answers = request.POST.getlist('selected_answers[]')
            score = request.session.get('score', 0)

            # Increment score for each correct answer
            score += sum(1 for answer_id in selected_answers if answer_id in correct_answers)

            request.session['score'] = score

            feedback = {
                'score': score
            }

            return JsonResponse(feedback)

        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request'}, status=400)
