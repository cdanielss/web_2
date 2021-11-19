from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


class Post(models.Model):
    title = models.CharField('Título', max_length=500, blank=False, null=False)
    intro = models.CharField('Introdução', max_length=500, blank=False, null=False)
    resume = models.TextField('Resumo', blank=False, null=False)
    conclusion = models.TextField('Conclusão', blank=False, null=False)
    image = models.ImageField()

    price = models.FloatField('Preço', blank=False, null=False)
    graphics = models.FloatField('Gráficos', blank=False, null=False)
    optimization = models.FloatField('Otimização', blank=False, null=False)
    gameplay = models.FloatField('Gameplay', blank=False, null=False)
    difficulty = models.FloatField('Dificuldade', blank=False, null=False)

    authorComment = models.CharField('Autor do Comentario', max_length=50, blank=False, null=False)
    comment = models.CharField('Comentario', max_length=500, blank=False, null=False)

    author = models.CharField('Autor do Post', max_length=50, blank=False, null=False)
    Aboutauthor = models.CharField('Sobre autor do Post', max_length=500, blank=False, null=False)

    date = models.DateField('Data de publicação', auto_now_add=True)
    slug = models.SlugField('URL', editable=False)

    def __str__(self):
        return self.title
    
    def save(self, *args, **kwargs):
        value = self.title
        self.slug = slugify(value, allow_unicode=True)
        super().save(*args, **kwargs)

class Email(models.Model):
    emails2 = models.EmailField(default="c@c.com", max_length=50)