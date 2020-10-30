from django.db import models


class Question(models.Model):
    title = models.CharField(max_length=255)
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('position',)
        verbose_name = 'Пункт калькулятора'
        verbose_name_plural = 'Пункты калькулятора'


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE, related_name='choices')
    choice_text = models.CharField(max_length=200)
    position = models.PositiveIntegerField(default=1)

    def __str__(self):
        return self.choice_text

    class Meta:
        verbose_name = 'Вариант'
        verbose_name_plural = 'Вариант'
