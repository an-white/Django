from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

# valores por defecto
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([item[1][0], item[0]] for item in get_all_styles())
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])


# creacion de modelo basica
class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)  # datetime field
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    # añadir opciones a seleccionar en el campo y un valor por defecto
    language = models.CharField(choices=LANGUAGE_CHOICES, default="python", max_length=140)
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=120)

    class Meta:
        ordering = ["created"]
