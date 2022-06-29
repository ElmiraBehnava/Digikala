from django.db import models


class ScrapedData(models.Model):
    title = models.CharField(max_length=150)
    description = models.TextField()
    date = models.DateField(auto_now_add=True)
    url = models.URLField(max_length=200)

    def __str__(self):
        return self.title
