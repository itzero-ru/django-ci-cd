from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect

from .models import Articles, Comments
from .forms import ArticlesForm, CommentForm
from django.views.generic import DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormMixin
from django.urls import reverse
from django.shortcuts import render
from django.db.models import Count
from django.core.paginator import Paginator
# Create your views here.

def news_home(request):
    """Список всех постов на странице с новостями
    
    Включена пагинация по страницам
    """
    news = Articles.objects.order_by('-date')
    paginator = Paginator(news,10) # Кол-во постов на странице
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    for item in page_obj:
        """Подсчет кол-ва комментариев поста"""
        item.all_comments = len(item.comments_articles.all())

    return render(request, 'news/news_home.html', {'page_obj':page_obj})

class NewsDetailView(FormMixin, DetailView):
    """Обработка страницы статьи"""
    model = Articles
    template_name = 'news/details_view.html'
    context_object_name = 'article'
    form_class = CommentForm
    success_msg = 'Коментарий успешно создан'

    def post(self, request, *args, **kwargs):
        """Обработка отправленной формы, переданной методом POST"""
        form = self.get_form()

        if form.is_valid:
            return self.form_valid(form)
        else:
            return self.form_invalid(form)
    
    def form_valid(self, form):
        """Запись данных формы в БД"""
        self.object = form.save()
        self.object.article = self.get_object()
        self.object.save()
        #return super().form_valid(form)
        return HttpResponseRedirect('/news/'+ str(self.get_object().id))
    
class NewsUpdateView(UpdateView):
    """Обновление данных статьи"""
    model = Articles
    template_name = 'news/create.html'
    form_class = ArticlesForm

class NewsDeleteView(DeleteView):
    """Удаление статьи"""
    model = Articles
    success_url = '/news/'
    template_name = 'news/news-delete.html'

def create(request):
    """Создание статьи через форму сайта"""
    error = ''

    if request.method == 'POST':
        form = ArticlesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = 'Форма введена неверной'
    form = ArticlesForm()

    data = {
        'form': form,
        'error': error
    }

    return render(request, 'news/create.html', data)