from django.db import models


class words(models.Model):

    word = models.CharField(max_length = 250)
    meaning = models.TextField()
    example_1 = models.TextField(blank=True)
    example_2 = models.TextField(blank=True)
    example_3 = models.TextField(blank=True)
    example_4 = models.TextField(blank=True)
    example_5 = models.TextField(blank=True)
    example_6 = models.TextField(blank=True)
    example_7 = models.TextField(blank=True)
    example_8 = models.TextField(blank=True)
    example_9 = models.TextField(blank=True)
    example_10 = models.TextField(blank=True)

    def __str__(self):
        return self.word

    class Meta:

        verbose_name_plural = "words"
