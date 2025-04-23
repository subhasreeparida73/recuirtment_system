from django.shortcuts import render, redirect
from .forms import JobForm, CandidateForm
from .models import Candidate
import fitz  # PyMuPDF
from .utils.resume_reader import extract_text_from_resume
from .utils.parser import parse_resume


def extract_text_from_resume(resume_file):
    if resume_file.name.endswith(".pdf"):
        with fitz.open(stream=resume_file.read(), filetype="pdf") as doc:
            text = ""
            for page in doc:
                text += page.get_text()
            return text
    else:
        # fallback to .txt or basic read
        return resume_file.read().decode("utf-8", errors="ignore")


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
        form = CandidateForm(request.POST, request.FILES)
        if form.is_valid():
            candidate = form.save(commit=False)

            resume_file = request.FILES['resume']
            text = extract_text_from_resume(resume_file)

            job = candidate.job
            parsed_data = parse_resume(text, job.requirements)

            candidate.skills = parsed_data["skills"]
            candidate.experience_years = parsed_data["experience_years"]
            candidate.score = parsed_data["score"]
            candidate.save()

            return redirect('add_candidate')
    else:
        form = CandidateForm()
    return render(request, 'add_candidate.html',{'form':form})
def candidate_list(request):
    candidates = Candidate.objects.all().order_by('score')
    return render(request, 'candidate_list.html', {'candidates':candidates})
