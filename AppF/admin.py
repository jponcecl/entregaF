from django.contrib import admin

# By JuanK
from .models import Movie
from datetime import datetime

# Register your models here.

# By JuanK
class MovieAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'nombre_tr', 'descrip', 'fecha_est', 'antiguedad']
    search_fields = ['nombre', 'nombre_tr']
    list_filter = ['nombre']

    def antiguedad(self, object):
        print('**********',object)
        if object.fecha_est:
            dif = (datetime.now().date() - object.fecha_est).days
            years = int(dif // 365.25)
            rem_days = int(dif % 365.25)
            return f'{years} años, {rem_days} dias'
            #return (datetime.now().date() - object.fecha_est).days
# By JuanK
admin.site.register(Movie, MovieAdmin)
