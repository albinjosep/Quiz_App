from django.db import models

class Question(models.Model):
    text = models.CharField(max_length=255)
    option_a = models.CharField(max_length=100)
    option_b = models.CharField(max_length=100)
    option_c = models.CharField(max_length=100)
    option_d = models.CharField(max_length=100)
    correct_option = models.CharField(max_length=1)  # 'a', 'b', 'c', or 'd'

    def __str__(self):
        return self.text

class UserSubmission(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField(max_length=1)  # 'a', 'b', 'c', or 'd'
    is_correct = models.BooleanField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Question: {self.question.text}, Selected: {self.selected_option}, Correct: {self.is_correct}"

class QuizSession(models.Model):
    start_time = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Session started at {self.start_time}"
