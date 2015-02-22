from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from cofy.models import *
# Create your views here.

def index(request):
	return render_to_response('cofy/index.html', context_instance=RequestContext(request))

def job(request, job_noc):
 	og = occupational_groupings.objects.get(noc = job_noc)
    	employments = employment.objects.get(noc = job_noc)
	growth = employment_growth.objects.get(noc = job_noc)
	imm = immigration.objects.get(noc = job_noc)
	openings = job_openings.objects.get(noc = job_noc)
	seekers = job_seekers.objects.get(noc = job_noc)
	otherReplacements = other_replacement.objects.get(noc = job_noc)
	otherSeekers = other_seekers.objects.get(noc = job_noc)
	retire = retirements.objects.get(noc = job_noc)
	schoolLeavers = school_leavers.objects.get(noc = job_noc)
	sum = summary.objects.get(noc = job_noc)

	subjobs = og.occupation.split('; ')
	subjobs = [jobs[7:] for jobs in subjobs]

	result = render_to_response('cofy/job.html', {"og":og, "employments":employments, "growth":growth, "imm":imm, "openings":openings, "seekers":seekers, "otherReplacements":otherReplacements, "otherSeekers":otherSeekers, "retire":retire, "schoolLeavers":schoolLeavers, "sum":sum, "subjobs":subjobs})
	return result

def joblist(request):
	jobs = occupational_groupings.objects.all().order_by('occupational_grouping')
	results = render_to_response('cofy/joblist.html', {'jobs':jobs}, context_instance = RequestContext(request))
	return results

def about(request):
	return render_to_response('cofy/about.html', context_instance=RequestContext(request))

