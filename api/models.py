from django.db import models

# Create your models here.


class FeedbackUser(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.BigIntegerField()
    message = models.CharField(null=True, max_length=300)
    dateCreated = models.DateTimeField(auto_now=True)
    slug = models.SlugField()
    def __str__(self):
        return f'{self.name} {self.phone} {self.email} {self.message}'

    def get_absolute_url(self):
        return f'/{self.slug}/'

    class Meta:
        ordering = ('dateCreated',)
