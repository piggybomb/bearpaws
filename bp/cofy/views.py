from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from cofy.models import cofy_employment, cofy_employment_growth, cofy_immigration, cofy_job_openings, cofy_job_openings, cofy_job_seekers, cofy_occupational_groupings, cofy_other_replacement, cofy_other_seekers, cofy_retirements, cofy_school_leavers, cofy_summary


# Create your views here.

def index(request):
	return render_to_response('cofy/index.html', context_instance=RequestContext(request))

def job(request, job_noc, slug):
    job = cofy_occupational_groupings.objects.get(noc = job_noc)
    
    result = render_to_response('<html path>', {"job", job}
    return result
