from django.shortcuts import render

# Create your views here.
def view1(request):
	myname="Chaithra"
	favplayer="MS.Dhoni"
	favbird="Peacock"
	favanimal="Lion"
	favsubject="Python"
	d={'name':myname,'player':favplayer,'bird':favbird,'animal':favanimal,'subject':favsubject}
	return render(request,'staticapp1/1.html',d)