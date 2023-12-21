# views.py

from django.shortcuts import render, redirect
from .forms import FileUploadForm

def upload_file(request):
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = FileUploadForm()
    return render(request, 'upload_file.html', {'form': form})

def success(request):
    return render(request, 'success.html')
