from django.shortcuts import render,redirect
from .models import DiEntry
from django.contrib.auth.decorators import login_required


def home_page(request):
    return render(request,('diary_of_calm/home_page.html'))

# def my_entries(request):
#     return render(request,'diary_of_calm/my_entries.html')

@login_required 
def create_entry(request):
    if request.method == 'POST':
        title = request.POST.get('title') 
        content = request.POST.get('content')
        DiEntry.objects.create(
            user=request.user,
            title=title,
            content=content
        )
        return redirect('home') 
    return render(request, 'diary_of_calm/create_entry.html') 

@login_required
def my_entries(request):
    entries = DiEntry.objects.filter(user=request.user)
    entries = entries.order_by('-created_at')
    return render(request, 'diary_of_calm/my_entries.html', {'entries': entries})

