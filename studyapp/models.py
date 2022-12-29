from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Help(models.Model):
    name = models.CharField(max_length=200, verbose_name="Name")
    phone = models.IntegerField(verbose_name="Phone No")
    email = models.EmailField(verbose_name='Email')
    subject = models.CharField(max_length=150, verbose_name='Subject')
    message_date = models.DateField( verbose_name='Message Date')
    message = models.TextField(max_length=3000)
    

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        ordering = ['-message_date']
        verbose_name = "Help"
        verbose_name_plural = "Helps"


class Notes(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Notes"
        verbose_name_plural = "Notes"

    def __str__(self):
        return f"{self.title}"


class Homework(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=200)
    
    title = models.CharField(max_length=200)
    description = models.TextField()
    due = models.DateTimeField()
    is_finished = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = "Homework"
        verbose_name_plural = "Homework"

    def __str__(self):
        return f"{self.subject}, {self.title}"

class ToDo(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(verbose_name="Title", max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_finished = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f'{self.title}'

    class Meta:
        
        ordering = ['-created_at']
        verbose_name = "ToDo"
        verbose_name_plural = "ToDos"