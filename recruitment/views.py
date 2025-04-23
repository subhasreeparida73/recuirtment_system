from django.shortcuts import render, redirect
from .forms import JobForm, CandidateForm

# View for adding jobs
def add_job(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_job')  # Redirect after successful form submission
    else:
        form = JobForm()
    return render(request, 'add_job.html', {'form': form})

# View for adding candidates
def add_candidate(request):
    if request.method == 'POST':
        form = CandidateForm(request.POST, request.FILES)  # Remember to include request.FILES to handle resume file upload
        if form.is_valid():
            form.save()
            return redirect('add_candidate')  # Redirect after successful form submission
    else:
        form = CandidateForm()
    return render(request, 'add_candidate.html', {'form': form})