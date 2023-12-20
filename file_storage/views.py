from django.shortcuts import render, redirect
from .forms import MyForm
from .models import FileStorage


def upload_file(request):
    if request.method == 'POST':
        form = MyForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['uploaded_file']

            # Save the file information to your model
            FileStorage.objects.create(uploaded_file=file)

            return redirect('success')
    else:
        form = MyForm()

    return render(request, 'upload.html', {'form': form})


def success(request):
    return render(request, 'success.html')
