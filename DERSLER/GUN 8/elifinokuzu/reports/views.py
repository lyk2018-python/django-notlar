from django.shortcuts import render, redirect
from reports.forms import ReportForm
from django.urls import reverse


def reportdone(request):
    return render(request, "reports/reportdone.html")

def report(request):
    if request.method == "POST":
        form = ReportForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.save()
            return redirect(reverse("reportdone"))
    else:
        form = ReportForm()
    return render(request, 'reports/report.html', {'form': form})