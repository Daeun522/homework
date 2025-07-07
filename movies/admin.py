from django.contrib import admin
from django.db.models import Avg
from .models import Movie, Rating

# Register your models here.
@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'average_score', 'created_at')

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(avg_score=Avg('ratings__score')).order_by('-avg_score')
    
    def average_score_display(self, obj):  
        return round(obj.avg_score, 2) if obj.avg_score is not None else 0
    average_score_display.short_description = 'Average Score'
    average_score_display.admin_order_field = 'avg_score'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    list_display = ('movie', 'score', 'created_at')