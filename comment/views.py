from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from .models import Comment, Reply
from .forms import CommentForm, ReplyForm

class PostDetailView(TemplateView):
    template_name = 'post_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Fetch comments and replies for the post
        post_id = kwargs.get('post_id')
        comments = Comment.objects.filter(post_id=post_id)
        context['comments'] = comments
        context['comment_form'] = CommentForm()
        context['reply_form'] = ReplyForm()
        return context

    def post(self, request, *args, **kwargs):
        post_id = kwargs.get('post_id')
        comment_form = CommentForm(request.POST)
        reply_form = ReplyForm(request.POST)

        if comment_form.is_valid():
            # Save the comment to the database
            comment = comment_form.save(commit=False)
            comment.post_id = post_id
            comment.save()
            return redirect('post_detail', post_id=post_id)

        if reply_form.is_valid():
            # Save the reply to the database
            reply = reply_form.save(commit=False)
            comment_id = request.POST.get('comment_id')
            reply.comment_id = comment_id
            reply.save()
            return redirect('post_detail', post_id=post_id)

        # If neither form is valid, re-render the template with errors
        context = self.get_context_data(**kwargs)
        context['comment_form'] = comment_form
        context['reply_form'] = reply_form
        return render(request, self.template_name, context)
