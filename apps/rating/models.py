from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


    class Meta:
        verbose_name_plural = 'Fanlar'

    def __str__(self):
        return self.name
class Question(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    text = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = 'Savollar'

    def __str__(self):
        return self.text





class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    is_correct = models.BooleanField()

    def __str__(self):
        return self.choice



    class Meta:
        verbose_name_plural = 'Javoblar'





