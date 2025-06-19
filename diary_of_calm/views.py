from django.shortcuts import render,redirect
from .models import DiEntry
from django.contrib.auth.decorators import login_required
from .forms import DiEntryForm


def home_page(request):
    return render(request,('diary_of_calm/home_page.html'))

# def my_entries(request):
#     return render(request,'diary_of_calm/my_entries.html')

@login_required 
def create_entry(request):
    if request.method == 'POST': 
        form = DiEntryForm(request.POST)
        if form.is_valid():
            entry = form.save(commit = False)
            entry.user = request.user
            entry.save()
    else:
        form = DiEntryForm()
    return render(request, 'diary_of_calm/create_entry.html', {'form': form})

    #     title = request.POST.get('title') 
    #     content = request.POST.get('content')
    #     DiEntry.objects.create(user=request.user,content=content,title = title)
    #     return redirect('my_entries') 
    # return render(request, 'diary_of_calm/create_entry.html',{'form':form}) 


@login_required
def my_entries(request):
    entries = DiEntry.objects.filter(user=request.user)
    return render(request, "diary_of_calm/my_entries.html", {"entries": entries})

