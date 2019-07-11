from django.shortcuts import render, HttpResponse
from . import models as mymod
from django.views.generic import TemplateView

from . import forms as myform
# Create your views here.
def home(request):
	return render(request,'polls/index.html')

#get selected polling unit
def puGet(request):
	poll = request.GET.get('value')
	print(poll)
	template="polls/pu-resultp.html"
	result = mymod.AnnouncedPuResults.objects.filter(polling_unit_uniqueid=poll)
	context={
	"result":result,
	}
	return render(request,template,context)

# display details of selected polling unit
def puResult(request):
	template="polls/pu-result.html"
	pu=mymod.PollingUnit.objects.all()
	context={
	"polling":pu
	}
	return render(request,template,context)

def party(request):
	parties=mymod.Party.objects.all()

	for x in parties:
		result = mymod.AnnouncedPuResults.objects.filter(party_abbreviation=x.partyname)
		print (x.partyname +' '+ result)

	return HttpResponse(x.partyname)


def addpollingresult(request):
    if request.method == 'POST':
        formset = myform.pollingFormset(result_id=resultid, data=request.POST)
        if formset.is_valid():
            formset.save()
    else:
        formset = myform.pollingFormset(None)
    return render(request,"polls/manage-poll.html", {"formset": formset})
