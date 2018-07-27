from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from dictionary.models import Node

def add_comment_to_node(request, id):
    node = get_object_or_404(Node.objects.filter(pk=id))
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.node = node
            comment.user = request.user
            comment.save()
            return redirect('node_detail', node.id)
    else:
        form = CommentForm()
    return render(request, 'comments/add_comment_to_node.html', {'form': form})
