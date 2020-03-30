from django.shortcuts import render
from django.http import HttpResponse

def home_page_views(request):
    return render(request, 'testapp/home.html')

def movie_news_views(request):
    news1 = "news one"
    news2 = "news one are"
    news3 = "news three are"
    news4 = "news four are"
    news5 = "news five are"

    my_dict={'news1':news1,
             'news2':news2,
             'news3':news3,
             'news4':news4,
             'news5':news5,}

    return render(request, 'testapp/mnews.html', my_dict)

def local_news_views(request):
    lnews1 = "local news 1"
    lnews2 = "local news 2"
    lnews3 = "local news 3"

    my_dict2 = {'lnews1':lnews1, 'lnews2':lnews2, 'lnews3':lnews3,}
    return render(request, 'testapp/lnews.html', my_dict2)

def sports_news_views(request):
    snews1 = "sport news is "
    snews2 = "sport news is "
    snews3 = "sport news is "

    my_dict3 = {'snews1':snews1, 'snews2':snews2, 'snews3':snews3,}
    return render(request, 'testapp/snews.html', my_dict3)
