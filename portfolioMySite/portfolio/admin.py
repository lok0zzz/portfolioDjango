from django.contrib import admin

from .models import Linguagem
from .models import Projeto

admin.site.register(Linguagem)
admin.site.register(Projeto)

