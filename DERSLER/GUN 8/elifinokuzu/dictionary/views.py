import random
from django.shortcuts import render, redirect
from dictionary.models import Node, Edge
from .forms import SubmissionForm
from django.urls import reverse


def home(request):
    nodes = Node.objects.all()

    if len(Node.objects.all()) > 0:
        random_word = random.choice(Node.objects.all()).id
    else:
        random_word = "None"

    return render(request, 'home.html', {
        'title': 'Öküzün Elifi',
        'nodes': nodes,
        'random_word': random_word,
    })

def node_detail(request, id):
    node = Node.objects.get(id=id)
    incoming = node.incoming.all()
    outgoing = node.outgoing.all()
    return render(request, 'node_detail.html', {
        'node': node,
        'incoming': incoming,
        'outgoing': outgoing,
        'title': 'Öküzün Elifi: %s' % node.name,
    })

def edge_detail(request, id):
    edge = Edge.objects.get(id=id)
    return render(request, 'edge_detail.html', {
        'edge': edge,
        'edge.source': edge.source,
        'edge.destination': edge.destination,
        'edge.type_of_edge': edge.type_of_edge,
        'title': 'Öküzün Elifi: %s' % edge.type_of_edge,
    })

def about(request):
    return render(request, 'about.html')

def support(request):
    return render(request, 'support.html')

def submit(request):
    form = SubmissionForm()

    if request.method == "POST":
        form = SubmissionForm(request.POST)
        if form.is_valid():

            if [i for i in Node.objects.all() if i.name == form.cleaned_data['source_node']] == [] \
                or [i for i in Node.objects.all() if i.name == form.cleaned_data['target_node']] == []:
                
                try:
                    source_node = Node.objects.get(name=form.cleaned_data['source_node'])
                except Node.DoesNotExist:
                    source_node = Node.objects.create(name=form.cleaned_data['source_node'],language=form.cleaned_data['source_language'],user=request.user,)

                try:
                    target_node = Node.objects.get(name=form.cleaned_data['target_node'])
                except Node.DoesNotExist:
                    target_node = Node.objects.create(name=form.cleaned_data['target_node'],language=form.cleaned_data['target_language'],user=request.user,)

                edge = Edge.objects.create(source=source_node,destination=target_node,is_directed=False,type_of_edge=form.cleaned_data['type_of_edge'],resource=form.cleaned_data['resource'],user=request.user,)
            
            else:
                return render(request, 'submit.html',
                    {"error" : "there are already those nodes available, please try new one", 
                    'form': SubmissionForm()}
                    )

            return redirect(reverse("node_detail", args=[source_node.id]))
    return render(request, 'submit.html',{"form" : form})