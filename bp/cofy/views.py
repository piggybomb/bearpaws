from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from cofy.models import employment, employment_growth, immigration, job_openings, job_openings, job_seekers, occupational_groupings, other_replacement, other_seekers, retirements, school_leavers, summary


# Create your views here.

def index(request):
	return render_to_response('cofy/index.html', context_instance=RequestContext(request))

def job(request, job_noc):
    job = occupational_groupings.objects.get(noc = job_noc)
    result = render_to_response('cofy/job.html', {"job", job})
    return result

def joblist(request):
	jobs = occupational_groupings.objects.all()
	results = render_to_response('cofy/joblist.html', {'jobs':jobs}, context_instance = RequestContext(request))
	return results
