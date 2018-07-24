from django.shortcuts import render
from dictionary.models import Node


nodes = Node.objects.all()
def home(request):
    return render(request, "home.html", {
    		"title": "Öküzün Elifi",
    		"nodes": nodes,
    	})

def node_detail(request, id):
	node = Node.objects.get(id=id)
	incoming = node.incoming.all()
	outgoing = node.outgoing.all()

	return render(request, "node_detail.html", {
    		"title": "Öküzün Elifi: %s" % node.name,
    		"incoming": incoming,
    		"outgoing": outgoing,
    		"node": node,
    	})

def about(request):
	return render(request, "about.html")

def support(request):
	return render(request, "support.html")
