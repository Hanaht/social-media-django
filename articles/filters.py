from .models import Article
import django_filters

class UserFilter(django_filters.FilterSet):
    class Meta:
        model = Article
        fields = ['author', 'title','body',]