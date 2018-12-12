from django.shortcuts import render
from django.views import generic
from .models import News

# Create your views here.

def IndexView (request):
    hot_list = News.objects.filter().order_by('-created_time')[:12]
    image_text = News.objects.exclude(article_image='None').order_by('-created_time')[:1]
    break_list1 = News.objects.filter(category='china').order_by('-created_time')[:13]
    break_list2 = News.objects.filter(category='international').order_by('-created_time')[:13]
    break_list3 = News.objects.filter(category='science').order_by('-created_time')[:13]
    news_list = {'hot_list': hot_list, 'image_text': image_text, 'break_list1': break_list1,
            'break_list2': break_list2, 'break_list3': break_list3}
    print(image_text[0].article_image)
    return render(request, "news/index.html",
                  {'hot_list': hot_list, 'image_text': image_text, 'break_list1': break_list1,
                    'break_list2': break_list2, 'break_list3': break_list3}
                  )



class DetailView(generic.DetailView):
    model = News
    template_name = 'news/detail.html'
    context_object_name = 'news'
    pk_url_kwarg = 'id'

    def get_object(self, queryset=None):
        obj = super(DetailView, self).get_object()
        print(obj)
        return obj



