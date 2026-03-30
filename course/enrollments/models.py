from django.db import models
from django.conf import settings
from courses.models import Course
# Create your models here.

User = settings.AUTH_USER_MODEL

class Enrollment(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('student', 'course') 

    def __str__(self):
        return f"{self.student} - {self.course}"