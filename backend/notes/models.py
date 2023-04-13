from django.db import models


class Note(models.Model):
    title = models.CharField(max_length=255, verbose_name='Note Title')
    content = models.TextField(verbose_name='Content')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Created time')
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name='Updated time')

    class Meta:
        verbose_name = 'Note'

    def __str__(self):
        return self.title
