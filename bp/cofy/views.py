import json

from django.utils.safestring import *
from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from cofy.models import *

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

	jobSummary = summary.objects.get(noc = job_noc)

	subjobs = og.occupation.split('; ')
	subjobs = [jobs[7:] for jobs in subjobs]

	#TODO1: improve the serialization process when we revamp the current models 
	#TODO2: may need to change how this works if we are to implement AJAX in the future

	years = ['y2012','y2013','y2014','y2015','y2016','y2017','y2018','y2019','y2020','y2021','y2022']

	data = {}
	data['employment']        = [float(getattr(employments,x)) for x in years]
	data['growth']            = [float(getattr(growth,x)) for x in years]
	data['immigration']       = [float(getattr(imm,x)) for x in years]
	data['openings']          = [float(getattr(openings,x)) for x in years]
	data['seekers']           = [float(getattr(seekers,x)) for x in years]
	data['otherReplacements'] = [float(getattr(otherReplacements,x)) for x in years]
	data['otherSeekers']      = [float(getattr(otherSeekers,x)) for x in years]
	data['retirement']        = [float(getattr(retire,x)) for x in years]
	data['schoolLeavers']     = [float(getattr(schoolLeavers,x)) for x in years]

	jobData = mark_safe(json.dumps(data))

	result = render_to_response('cofy/job.html', {"og":og, "jobData":jobData, "jobSummary":jobSummary, "subjobs":subjobs})
	return result

def joblist(request):
        a = occupational_groupings.objects.filter(occupational_grouping__istartswith='a').order_by('occupational_grouping')
	b = occupational_groupings.objects.filter(occupational_grouping__istartswith='b').order_by('occupational_grouping')
	c = occupational_groupings.objects.filter(occupational_grouping__istartswith='c').order_by('occupational_grouping')
	d = occupational_groupings.objects.filter(occupational_grouping__istartswith='d').order_by('occupational_grouping')
	e = occupational_groupings.objects.filter(occupational_grouping__istartswith='e').order_by('occupational_grouping')
	f = occupational_groupings.objects.filter(occupational_grouping__istartswith='f').order_by('occupational_grouping')
	g = occupational_groupings.objects.filter(occupational_grouping__istartswith='g').order_by('occupational_grouping')
	h = occupational_groupings.objects.filter(occupational_grouping__istartswith='h').order_by('occupational_grouping')
	i = occupational_groupings.objects.filter(occupational_grouping__istartswith='i').order_by('occupational_grouping')
	j = occupational_groupings.objects.filter(occupational_grouping__istartswith='j').order_by('occupational_grouping')
	k = occupational_groupings.objects.filter(occupational_grouping__istartswith='k').order_by('occupational_grouping')
	l = occupational_groupings.objects.filter(occupational_grouping__istartswith='l').order_by('occupational_grouping')
	m = occupational_groupings.objects.filter(occupational_grouping__istartswith='m').order_by('occupational_grouping')
	n = occupational_groupings.objects.filter(occupational_grouping__istartswith='n').order_by('occupational_grouping')
	o = occupational_groupings.objects.filter(occupational_grouping__istartswith='o').order_by('occupational_grouping')
	p = occupational_groupings.objects.filter(occupational_grouping__istartswith='p').order_by('occupational_grouping')
	q = occupational_groupings.objects.filter(occupational_grouping__istartswith='q').order_by('occupational_grouping')
	r = occupational_groupings.objects.filter(occupational_grouping__istartswith='r').order_by('occupational_grouping')
	s = occupational_groupings.objects.filter(occupational_grouping__istartswith='s').order_by('occupational_grouping')
	t = occupational_groupings.objects.filter(occupational_grouping__istartswith='t').order_by('occupational_grouping')
	u = occupational_groupings.objects.filter(occupational_grouping__istartswith='u').order_by('occupational_grouping')
	v = occupational_groupings.objects.filter(occupational_grouping__istartswith='v').order_by('occupational_grouping')
	w = occupational_groupings.objects.filter(occupational_grouping__istartswith='w').order_by('occupational_grouping')
	x = occupational_groupings.objects.filter(occupational_grouping__istartswith='x').order_by('occupational_grouping')
	y = occupational_groupings.objects.filter(occupational_grouping__istartswith='y').order_by('occupational_grouping')
	z = occupational_groupings.objects.filter(occupational_grouping__istartswith='z').order_by('occupational_grouping')
	results = render_to_response('cofy/joblist.html', {'a': a, 'b':b, 'c':c, 'd':d,'e':e, 'f':f, 'g':g, 'h':h, 'i':i, 'j':j, 'k':k, 'l':l, 'm':m, 'n':n, 'o':o, 'p':p, 'q':q, 'r':r, 's':s, 't':t, 'u':u, 'v':v, 'w':w, 'x':x, 'y':y, 'z':z}, context_instance = RequestContext(request))
	return results

def about(request):
	return render_to_response('cofy/about.html', context_instance=RequestContext(request))

