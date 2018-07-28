from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentFormForNode, CommentFormForEdge
from dictionary.models import Node, Edge

def add_comment_to_node(request, id):
    node = get_object_or_404(Node.objects.filter(pk=id))
    if request.method == "POST":
        form = CommentFormForNode(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.node = node
            comment.user = request.user
            comment.save()
            return redirect('node_detail', node.id)
    else:
        form = CommentFormForNode()
    return render(request, 'comments/add_comment_to_node.html', {'form': form})

def add_comment_to_edge(request, id):
    edge = get_object_or_404(Edge.objects.filter(pk=id))
    if request.method == "POST":
        form = CommentFormForEdge(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.edge = edge
            comment.user = request.user
            comment.save()
            return redirect('edge_detail', edge.id)
    else:
        form = CommentFormForEdge()
    return render(request, 'comments/add_comment_to_edge.html', {'form': form})
