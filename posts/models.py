from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    published_date = models.DateTimeField()
    image = models.ImageField(upload_to='media/')
    body = models.TextField()

    def __str__(self):
        return self.title

    def pub_date_clean(self):
        return self.published_date.strftime('%b %e, %Y')

    def summary(self):
        return self.body[:100] + "..."