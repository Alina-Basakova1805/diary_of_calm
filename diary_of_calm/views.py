from django.shortcuts import render


def home_page(request):
    return render(request,('diary_of_calm/home_page.html'))

# def my_entries(request):
#     return render(request,'diary_of_calm/my_entries.html')

