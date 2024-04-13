from django.shortcuts import render, redirect, get_object_or_404,reverse
# from django.contrib.auth.decorators import login_required
from django.views.generic import ListView, CreateView, UpdateView, DeleteView,DetailView
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post,Tag,Categorys
from django.views.generic import View
from comment.forms import CommentForm
from comment.models import Comment, Reply,Reaction,AnonymousLike
from .forms import NewPostForm
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import FormView
from django.http import JsonResponse
from .forms import SearchForm
from .models import Visit
from django.http import HttpResponseNotFound
from django.http import HttpResponseBadRequest




class PostListView(ListView):
    model = Post
    template_name = 'blog.html'  # Specify the template name
    # context_object_name = 'posts'  # Specify the context variable name in the template
    ordering = "-posted"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-posted')[:4]  # Pass all tags to the template
        context['tags'] = Tag.objects.all()  # Pass all tags to the template
        context['category'] = Categorys.objects.all()  # Pass all categories to the template
        return context
    
def tags(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = Post.objects.filter(tag=tag).order_by("-posted")  # Assuming you have a 'tags' field in your Post model
    tags = Tag.objects.all()  # Fetch all tags
    first_post = posts.first()  # Fetch the first post for the tag
    first_post_picture = first_post.picture.url if first_post else None  # Get the picture URL of the first post, or None if no post exists
    category = Categorys.objects.all()
    category = Categorys.objects.all()  # Fetch all categories
    context = {
        'tag': tag,
        'posts': posts,
        'tags': tags,
        'first_post': first_post,
        'first_post_picture': first_post_picture,
        'category': category,  # Pass categories to the context
    }
    return render(request, "tag.html", context)

class AddCategoryView(CreateView):
    model = Categorys
    template_name = 'add_category.html'
    fields = '__all__'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['posts'] = Post.objects.all().order_by('-posted') # Pass all tags to the template
        context['tags'] = Tag.objects.all()  # Pass all tags to the template
        context['category'] = Categorys.objects.all()  # Pass all categories to the template
        return context
    
import json
    
# def AddLike(request, pk):

#     post = get_object_or_404(Post, id=request.POST.get('post_id'))
#     liked = False
#     if post.likes.filter(id=request.user.id).exists():
#         post.likes.remove(request.user)
#         liked = False
#     else:
#         post.likes.add(request.user)
#         liked = True
#     return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))
    
def AddLikesPost(request, pk):
    data = json.loads(request.body)
    id = data["id"]
    post = Post.objects.get(id=id)
    checker = None
    
    if request.user.is_authenticated:
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            checker = 0
        else:
            post.likes.add(request.user) 
            checker = 1
            
    likes = post.likes.count()
    
    # Determine the liked status based on the current user's interaction
    liked = post.likes.filter(id=request.user.id).exists() if request.user.is_authenticated else False
    
    info = {
        'check': checker,
        'num_of_likes': likes,
        'liked': liked,  # Include the liked status in the JSON response
    }
    
    return JsonResponse(info)

class AddLikesComment(View):
    def post(self, request, *args, **kwargs):
        comment_id = request.POST.get('comment_id')
        comment = get_object_or_404(Comment, id=comment_id)
        liked = False

        if request.user.is_authenticated:
            if comment.likes.filter(id=request.user.id).exists():
                comment.likes.remove(request.user)
                liked = False
            else:
                comment.likes.add(request.user)
                liked = True

        # Include the comment ID in the JSON response
        data = {
            'comment_id': comment_id,
            'liked': liked,
            'numb_of_likes': comment.likes.count(),
        }

        return JsonResponse(data)
    
class AddLikesReply(View):
    def post(self, request, *args, **kwargs):
        reply_id = request.POST.get('reply_id')
        reply = get_object_or_404(Reply, id=reply_id)
        liked_reply = False

        if request.user.is_authenticated:
            if reply.likes.filter(id=request.user.id).exists():
                reply.likes.remove(request.user)
                liked_reply = False
            else:
                reply.likes.add(request.user)
                liked_reply = True

        # Include the comment ID in the JSON response
        data = {
            'reply_id': reply_id,
            'liked_reply': liked_reply,
            'numb_of_likes': reply.likes.count(),
        }

        return JsonResponse(data)






# def AddReplyLike(request, pk):
#     # Get the reply object
#     reply = get_object_or_404(Reply, id=request.POST.get('reply_id'))
#     if request.user.is_authenticated:
#         # Check if the user has already liked the reply
#         if reply.likes.filter(id=request.user.id).exists():
#             # User has already liked the reply, so unlike it
#             reply.likes.remove(request.user)
#             liked_reply = False
#         else:
#             # User hasn't liked the reply, so like it
#             reply.likes.add(request.user)
#             liked_reply = True
#     else:
#         # User is not authenticated, use IP address to track likes
#         ip_address = request.META.get('REMOTE_ADDR')
#         if AnonymousLike.objects.filter(reply=reply, ip_address=ip_address).exists():
#             # If the like already exists, remove it
#             AnonymousLike.objects.filter(reply=reply, ip_address=ip_address).delete()
#             liked_reply = False
#         else:
#             # If the like does not exist, create it
#             AnonymousLike.objects.create(reply=reply, ip_address=ip_address)
#             liked_reply = True

#     # Redirect back to the post detail page
#     return HttpResponseRedirect(reverse('post-detail', args=[str(pk)]))

def CategoryView(request, cats):
    category = get_object_or_404(Categorys, name=cats)
    category_posts = Post.objects.filter(category=category)  # Assuming you have a related_name in the ManyToManyField
    
    tags = Tag.objects.all()
    categories = Categorys.objects.all()
    posts = Post.objects.all()
    
    context = {
        'category': category,
        'category_posts': category_posts,
        'tags': tags,
        'posts': posts,
        'categories': categories,
    }
    return render(request, 'category.html', context)




class PostDetailView(DetailView):
    model = Post
    template_name = "post-details.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()  # Pass all tags to the template
        context['category'] = Categorys.objects.all()  # Pass all categories to the template
          # Pass all categories to the template
        post = self.get_object()
        # categories = Category.objects.all()
        context['categories'] = Categorys.objects.all()
        comments = Comment.objects.filter(post=post).order_by('-date')
        context['comments'] = comments  # Pass comments to the template
        post = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = post.total_likes()
        
        liked = False
        if self.request.user.is_authenticated:  # Check if user is authenticated
            if post.likes.filter(id=self.request.user.id).exists():
                liked = True
        context['total_likes'] = total_likes
        context['liked'] = liked  # Pass liked status to the template
        
        # Retrieve comment_id from POST data
        comment_id = self.request.POST.get('comment_id')
        if comment_id:
            comment = get_object_or_404(Comment, id=comment_id)
            totals_likes = comment.total_likes()
            liked_comment = False
            if comment.likes.filter(id=self.request.user.id).exists():
                liked_comment = True
            context['totals_likes'] = totals_likes
            context['liked_comment'] = liked_comment  # Pass liked_comment status to the template
            
        reply_id = self.request.POST.get('reply_id')
        if reply_id:
            liked_reply = False
            reply = get_object_or_404(Reply, id=reply_id)
            total_reply_likes = reply.total_reply_likes()
            liked_reply = False
            if reply.likes.filter(id=self.request.user.id).exists():
                liked_reply = True
            context['total_reply_likes'] = total_reply_likes
            context['liked_reply'] = liked_reply
        # Retrieve reaction data for each comment
        reaction_data = {}
        for comment in comments:
            reactions = Reaction.objects.filter(comment=comment)
            reaction_data[comment.id] = {reaction.reaction_type: reaction.user.username for reaction in reactions}
        context['reaction_data'] = reaction_data  # Pass reaction data to the template

        visit, created = Visit.objects.get_or_create(post=post)
        if not created:  # If visit record already exists, increment count
            visit.count += 1
            visit.save()
        context['visit_count'] = visit.count  # Pass visit count to the template
        
        # # Retrieve total likes count and liked status for each comment
        for comment in comments:
            comment.totals_likes = comment.totals_likes()
            comment.liked_comment = comment.likes.filter(id=self.request.user.id).exists()

        # Retrieve replies for the current comment
            replies = comment.replies.all()
            for reply in replies:
                reply.total_reply_likes = reply.total_reply_likes()
                reply.liked_reply = reply.likes.filter(id=self.request.user.id).exists()
            #     return context
        
        # Pre-populate the name field for anonymous users
        initial_data = {'name': 'Anonymous'} if not self.request.user.is_authenticated else {}
        context['form'] = CommentForm(initial=initial_data)
        
        return context
    
    def post(self, request, *args, **kwargs):
            
        post = self.get_object()  # Get the current post
        
        
        if 'comment' in request.POST:
            # If it's a new comment submission
            comment = Comment(post=post)
            if request.user.is_authenticated:
                comment.user = request.user
                comment.name = request.user.username  # Use authenticated user's username
                comment.email = request.user.email  # Use authenticated user's email
            else:
                # If the user is not authenticated, retrieve the name and email from the form data
                comment.name = request.POST.get('name', 'Anonymous')  # Use name from form or default to "Anonymous"
                comment.email = request.POST.get('email')  # Use email from form or leave it blank
            comment.body = request.POST.get('body')
            comment.save()
            
            # Return JSON response indicating success
            return JsonResponse({
                                    'success': True,
                                    'message': 'Comment submitted successfully',
                                    'comment': {
                                        'body': comment.body,
                                        'name': comment.name,
                                    }
                                })
            
        

        elif 'reply' in request.POST:
            # If it's a reply submission
            comment_id = request.POST.get('comment_id')
            comment = get_object_or_404(Comment, pk=comment_id, post=post)  # Retrieve the comment object
            reply = Reply(comment=comment)
            if request.user.is_authenticated:
                reply.name = request.user.username  # Use authenticated user's username
                reply.email = request.user.email  # Use authenticated user's email
            else:
                # If the user is not authenticated, retrieve the name and email from the form data
                reply.name = request.POST.get('name', 'Anonymous')  # Use name from form or default to "Anonymous"
                reply.email = request.POST.get('email')  # Use email from form or leave it blank
            reply.body = request.POST.get('body')
            reply.post = post
            reply.user = request.user
            reply.save()
        elif 'edit_comment' in request.POST:
            # If it's an edit comment submission
            
            if request.user.is_authenticated and request.user == comment.user:
                comment_id = request.POST.get('edit_comment_id')  # Change to 'edit_comment_id'
                new_body = request.POST.get('body')

                comment = get_object_or_404(Comment, pk=comment_id, post=post)

            # Update the body of the comment
            comment.body = new_body
            comment.save()
            
        elif 'edit_reply_id' in request.POST:
            # If it's an edit comment submission
            if request.user.is_authenticated and request.user == comment.user:
                reply_id = request.POST.get('edit_reply_id')
                new_body = request.POST.get('body')

                reply = get_object_or_404(Reply, pk=reply_id)

            # Update the body of the comment
            reply.body = new_body
            reply.save()

        elif request.headers.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest':
            # If it's a delete comment submission
            comment_id = request.POST.get('delete_comment_id')
            comment = get_object_or_404(Comment, pk=comment_id) 

            # Check if the user is allowed to delete the comment
            if request.user.is_authenticated and request.user == comment.user:
                comment_id = request.POST.get('delete_comment_id')
                comment = get_object_or_404(Comment, pk=comment_id)
                comment.delete()
                return JsonResponse({'success': True, 'message': 'Comment deleted successfully'})
            else:
                return JsonResponse({'success': False, 'message': 'You are not authorized to delete this '})
            
            # Add any additional checks here, such as ensuring the current user is authorized to delete the comment
                # comment.delete()
        elif 'delete_reply_id' in request.POST:
            # If it's a delete comment submission
            reply_id = request.POST.get('delete_reply_id')
            reply = get_object_or_404(Reply, pk=reply_id)

            # Check if the user is allowed to delete the comment
            if request.user == reply.user:
                reply.delete()
            else:
                return HttpResponseBadRequest("You are not authorized to delete this reply.")
            # reply_id = request.POST.get('delete_reply_id')
            # reply = get_object_or_404(Reply, pk=reply_id)
            # # Add any additional checks here, such as ensuring the current user is authorized to delete the comment
            # reply.delete()
        
        return redirect('post-detail', pk=post.pk)
        # else:
        #     # Handle the case where post.pk is empty
        #     return HttpResponseNotFound("Post not found") 
        

        


    
    

    


class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    form_class = NewPostForm
    # fields = ['title', 'content', 'tag', 'category', 'picture']
    template_name = 'newpost.html'
    success_url = reverse_lazy('post-list')  # Adjust 'post-list' to match your URL name for the post list view
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tags'] = Tag.objects.all()  # Pass all tags to the template
        context['category'] = Categorys.objects.all()  # Pass all categories to the template
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    


class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    template_name = 'update_post.html'  # Specify the template name
    fields = ['picture','title','content','tag','category']
    success_url = reverse_lazy('post-list')  # Adjust 'post-list' to match your URL name for the post list view
    # form_class = EditPostForm # Specify the fields to include in the form
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
    
    
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False
    
    

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url = reverse_lazy('post-list')  # Specify the URL to redirect to after deletion
    template_name = 'post_confirm_delete.html'  # Specify the template name
    
    # def form_valid(self, form):
    #     form.instance.author = self.request.user
    #     return super().form_valid(form)
    
    def test_func(self) -> bool | None:
        post = self.get_object()
        if self.request.user == post.author:
            return True
        return False



def search_view(request):
    form = SearchForm(request.POST)
    if request.method == 'POST':
        query = request.POST['query']
        posts = Post.objects.filter(title__contains=query)
        tags = Tag.objects.all()  # Fetch all tags
        category = Categorys.objects.all()  # Fetch all categories
        
        context = {
            'form': form,
            'query': query,
            'posts': posts,
            'tags': tags,
            'category': category,
            
        }
        return render(request, 'search.html', context)
    else:
        return render(request, 'search.html', {})









def load_more_posts(request):
    page_number = request.GET.get('page')
    start_index = (int(page_number) - 1) * 4
    end_index = int(page_number) * 4
    
    posts = Post.objects.all().order_by('-posted')[start_index:end_index]
    has_more_posts = Post.objects.count() > end_index
    
    posts_html = render_to_string('partials/posts.html', {'posts': posts})
    
    return JsonResponse({'posts_html': posts_html, 'has_more_posts': has_more_posts})





