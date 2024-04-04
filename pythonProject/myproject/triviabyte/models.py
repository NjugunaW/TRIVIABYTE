from django.db import models
# import random
# import uuid
# from django.utils import timezone
# from django.contrib.auth.models import User


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.question_text

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer_text = models.CharField(max_length=255)

    def __str__(self):
        return self.answer_text



# class BaseModel(models.Model):
#     uid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
#     created_at = models.DateTimeField(auto_now_add=True)
#     updated_at = models.DateTimeField(auto_now=True)

#     class Meta:
#         abstract = True

#     def save(self, *args, **kwargs):
#         if not self.pk:
#             self.created_at = timezone.now()
#         self.updated_at = timezone.now()
#         super().save(*args, **kwargs)

# class QuizApp(BaseModel):
#     name = models.CharField(max_length=100, unique=True)

# class QuizCategory(BaseModel):
#     name = models.CharField(max_length=100, unique=True)

# class Question(BaseModel):
#     question_text = models.TextField()
#     category = models.ForeignKey(QuizCategory, on_delete=models.CASCADE)
#     marks = models.IntegerField(default=1)

#     def __str__(self) -> str:
#         return self.question_text

#     def fetch_answers(self):
#         answers = list(Answer.objects.filter(question=self))
#         random.shuffle(answers)
#         data = []
#         for answer in answers:
#             data.append({
#                 'text' : answer.text,
#                 'is_correct' : answer.is_correct
#             })

#         return data

# class Answer(BaseModel):
#     text = models.TextField()
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     is_correct = models.BooleanField(default=False)

# class Score(BaseModel):
#     username = models.CharField(max_length=100)
#     score = models.IntegerField()

#     def __str__(self):
#         return f"{self.username}'s Score: {self.score}"
