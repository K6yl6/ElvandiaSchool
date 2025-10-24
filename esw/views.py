from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ContactForm

from .forms import (
    CandidateForm, FatherForm, MotherForm, GuardianForm,
    Emergency1Form, Emergency2Form, Emergency3Form, SchUpdateForm
)
from .models import schUpdate


# ========== MAIN PAGES ==========

def home(request):
    recent_updates = schUpdate.objects.all().order_by('-created_at')[:3]
    return render(request, 'home.html', {'recent_updates': recent_updates})

def about_us(request):
    return render(request, 'about_us.html')

def academics(request):
    return render(request, 'academics.html')

def admission(request):
    return render(request, 'admission.html')

def contact(request):
    return render(request, 'contact.html')


# ========== ADMISSION FORM ==========

def admission_form_view(request):
    prefixes = {
        "candidate": "candidate",
        "father": "father",
        "mother": "mother",
        "guardian": "guardian",
        "e1": "e1",
        "e2": "e2",
        "e3": "e3",
    }

    if request.method == 'POST':
        candidate_form = CandidateForm(request.POST, prefix=prefixes["candidate"])
        father_form = FatherForm(request.POST, prefix=prefixes["father"])
        mother_form = MotherForm(request.POST, prefix=prefixes["mother"])
        guardian_form = GuardianForm(request.POST, prefix=prefixes["guardian"])
        e1_form = Emergency1Form(request.POST, prefix=prefixes["e1"])
        e2_form = Emergency2Form(request.POST, prefix=prefixes["e2"])
        e3_form = Emergency3Form(request.POST, prefix=prefixes["e3"])

        if (
            candidate_form.is_valid() and father_form.is_valid() and
            mother_form.is_valid() and guardian_form.is_valid() and
            e1_form.is_valid() and e2_form.is_valid() and e3_form.is_valid()
        ):
            candidate_form.save()
            father_form.save()
            mother_form.save()
            guardian_form.save()
            e1_form.save()
            e2_form.save()
            e3_form.save()

            messages.success(request, "Admission form submitted successfully!")
            return redirect('home')
        else:
            messages.error(request, "There were errors in the form. Please correct them and submit again.")
    else:
        candidate_form = CandidateForm(prefix=prefixes["candidate"])
        father_form = FatherForm(prefix=prefixes["father"])
        mother_form = MotherForm(prefix=prefixes["mother"])
        guardian_form = GuardianForm(prefix=prefixes["guardian"])
        e1_form = Emergency1Form(prefix=prefixes["e1"])
        e2_form = Emergency2Form(prefix=prefixes["e2"])
        e3_form = Emergency3Form(prefix=prefixes["e3"])

    return render(
        request,
        "admission_form.html",
        {
            "candidate_form": candidate_form,
            "father_form": father_form,
            "mother_form": mother_form,
            "guardian_form": guardian_form,
            "e1_form": e1_form,
            "e2_form": e2_form,
            "e3_form": e3_form,
        },
    )


# ========== SCHOOL UPDATES ==========

def schupdate_list(request):
    updates = schUpdate.objects.all().order_by('-created_at')
    return render(request, "schupdate_list.html", {"updates": updates})

def schupdate_detail(request, pk):
    update = get_object_or_404(schUpdate, pk=pk)
    return render(request, "schupdate_detail.html", {"update": update})

def schupdate_create(request):
    if request.method == 'POST':
        form = SchUpdateForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('schupdate_list')
    else:
        form = SchUpdateForm()
    return render(request, 'schupdate_form.html', {"form": form})

# main/views.py
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ContactForm

def contact_view(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "✅ Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "⚠️ Please correct the errors below.")
    else:
        form = ContactForm()
    
    return render(request, 'contact.html', {'form': form})