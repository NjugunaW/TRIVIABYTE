from django.shortcuts import render
from .questions import questions_data
from django.http import JsonResponse

# View function for rendering the index page with unique categories
def triviabyte_view(request):
    # Extracts unique categories from questions_data
    categories = set(question['category'] for question in questions_data)
    print("categories:", categories)
    # Creates a context dictionary containing the uniques categories extracted
    # Also renders the HTML page
    context = {'categories': categories}
    return render(request, 'index.html', context)

# View function for rendering the music.html template
def music_view(request):
    return render(request, 'music.html')

# View function for rendering the science.html template
def science_view(request):
    return render(request, 'science.html')

# View function for rendering the quiz.html template
def quiz_view(request):
    return render(request, 'quiz.html')

# View function for handling the quiz form submission and filtering questions based on the selected category
# It retrieves the selected category from the form data submitted via POST
def get_quiz(request):
    if request.method == 'POST':
       category = request.POST.get('category')
    if category:
            # This block of code Filters questions based on the selected category
            filtered_questions = [question for question in questions_data if question['category'] == category]
            context = {'category': category, 'questions': filtered_questions}
            return render(request, 'quiz.html', context)
    # If no category is selected, it renders the index.html page
    return render(request, 'index.html')
