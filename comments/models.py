from django.db import models

# Create your models here.

class Comment(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=255)
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    article = models.ForeignKey('blog.Article', on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:20]
