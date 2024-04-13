from django.shortcuts import render,redirect,get_object_or_404
from .models import Subscription, Newsletter
from django.contrib import messages
from .forms import SubscriptionForm,NewsLetterForm
from django.core.cache import cache
from django.views.decorators.cache import cache_page
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import Subscription
from django.http import JsonResponse
from django.core.mail import send_mail
from django.views import View
from django.contrib.auth.models import User
from django.db.models import F
from core.models import Profile
from blog.models import Post
from .forms import EditProfileForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Tag,Post,Visit,Categorys
from comment.models import Comment
from .models import  Home, About,ProfileInfo,ProgressModel,Education,Experience,Service,Portfolio,Contact,Home,ContactInfo
from django.db.models import Count


# Create your views here.

# @cache_page(60 * 15)  # Cache the page for 15 minutes
def index(request):
    # Check if the cached version of the page exists
    cached_data = cache.get('index_page_data')
    if cached_data:
        return cached_data

    posts = Post.objects.all()
    home = Home.objects.latest('time_added')
    tags = Tag.objects.all()[:12]
    categories = Categorys.objects.all()
    category = Categorys.objects.all()[:5]
    
    first_post_pictures_by_tag = {}  # Dictionary to store the first post picture for each tag
    for tag in tags:
        first_post = Post.objects.filter(tag=tag).first()
        if first_post:
            first_post_pictures_by_tag[tag] = first_post.picture.url


    # Increment visit count for each post
    for post in posts:
        post_visit, created = Visit.objects.get_or_create(post=post)
        post_visit.count += 1
        post_visit.save()
        
        # for tag in post.tag.all():
        #     tag_visit, created = Visit.objects.get_or_create(post=post, tag=tags)
        #     tag_visit.count += 1
        #     tag_visit.save()

    # Retrieve popular posts based on visit counts
    popular_posts = Post.objects.annotate(visit_count=F('visit')).order_by('-visit_count')[:5]
    # popular_tags = Tag.objects.annotate(visit_count=F('visit')).order_by('-visit_count')[:12]


    # Fetch the last three comments
    latest_comments = Comment.objects.order_by('-date')[:4]

    context = {
        'posts': posts,
        'home': home,
        'tags': tags,
        # 'popular_tags': popular_tags,
        'first_post': tags,
        'category': category,
        'categories': categories,
        'popular_posts': popular_posts,
        'latest_comments': latest_comments,
        'first_post_pictures_by_tag': first_post_pictures_by_tag,
    }

    # Cache the rendered template
    rendered_template = render(request, 'index.html', context)
    # cache.set('index_page_data', rendered_template, 60 * 15)  # Cache the data for 15 minutes
    return rendered_template

def service(request):
    
    services = Service.objects.all()
    portfolios = Portfolio.objects.all()
    tags = Tag.objects.all()
    category = Categorys.objects.all()
    context = {
        'services':services,
        'category':category,
        'portfolios':portfolios,
        'tags':tags,
    }
    return render(request, 'services.html', context)


def about(request):
    #about
    about = About.objects.latest('updated')
    profileInfo = ProfileInfo.objects.all()
    skills = ProgressModel.objects.all()
    educations = Education.objects.all()
    experiences = Experience.objects.all()
    category = Categorys.objects.all()
    tags = Tag.objects.all()
     #contact
    contactinfos = ContactInfo.objects.all()
    
    context = {
        'about': about,
        'category': category,
        'profileInfo': profileInfo,
        'skills': skills,
        'educations': educations,
        'experiences': experiences,
        'contactinfos': contactinfos,
        'tags': tags,
    }
    return render(request, 'about.html', context)

from django.http import HttpResponse

def send_newsletter(request):
    if request.method == 'POST':
        # Retrieve the newsletter content from the form
        title = request.POST.get('title')
        content = request.POST.get('content')

        # Fetch all subscribers
        subscribers = Newsletter.objects.all()

        # Send the newsletter to each subscriber
        for subscriber in subscribers:
            send_mail(
                title,  # Subject
                content,   # Message 
                'morrishenry502@email.com',  # Sender's email address
                [subscriber.email],  # Recipient's email address
                fail_silently=False,
            )

        # Return success response
        return HttpResponse("Newsletter successfully sent to all subscribers!")
    else:
        # Handle GET request (if necessary)
        pass


# Define a signal handler to send email notifications 
@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        # Fetch all subscribers
        subscribers = Subscription.objects.all()

        # Compose email content
        subject = 'New Post Notification'
        message = f'A new post "{instance.title}" has been published. Check it out!'
        from_email = 'morrishenry502@gmail.com'  # Replace with your email
        recipient_list = [subscriber.email for subscriber in subscribers]

        # URL of the post image
        post_image_url = instance.picture.url

        # Send email notifications
        send_mail(subject, message, from_email, recipient_list, html_message=get_email_template(post_image_url))
        
@receiver(post_save, sender=Post)
def send_post_notification(sender, instance, created, **kwargs):
    if created:
        # Fetch all subscribers
        newsletters = Newsletter.objects.all()

        # Compose email content
        subject = 'New Post Notification'
        message = f'A new post "{instance.title}" has been published. Check it out!'
        from_email = 'morrishenry502@gmail.com'  # Replace with your email
        recipient_list = [newsletter.email for newsletter in newsletters]

        # URL of the post image
        post_image_url = instance.picture.url

        # Send email notifications
        send_mail(subject, message, from_email, recipient_list, html_message=get_email_template(post_image_url))

def get_email_template(post_image_url):
    try:
        # Assuming you have retrieved a Post instance named `post`
        post = Post.objects.latest('posted')
        post_image_url = post.picture.url

        # Print the post image URL to verify
        print("Post Image URL:", post_image_url)

        # Define the email template
        template = f"""
        <html>
        <body>
            <h1>New Post Notification</h1>
            <p>A new post has been published. Check it out!</p>
            <img src="{post_image_url}" alt="Post Image">
        </body>
        </html>
        """
        return template

    except Post.DoesNotExist:
        return "No posts available."

# Generate the email template
email_template = get_email_template('post_image_url')

# Print the email template
print(email_template)

# You can then send the email using your preferred email sending method.



# class SubscribeView(FormView):
#     form_class = SubscriptionForm


#     def form_valid(self, form):
#         email = form.cleaned_data['email']
#         if Subscription.objects.filter(email=email).exists():
#             return JsonResponse({'success': False, 'message': 'You have already subscribed with this email.'})
#         form.save()
#         return JsonResponse({'success': True, 'message': 'You have successfully subscribed!'})

# class SubscriptionSuccessView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         # You can return an empty HttpResponse since there's no need to render anything
#         return JsonResponse({})

from django.views import View
class SubscribeView(View):
    def post(self, request, *args, **kwargs):
        form = SubscriptionForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Subscription.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': "You are already subscribed to the newsletter."})
            form.save()
            return JsonResponse({'success': True, 'message': "You have successfully subscribed!"})
        else:
            return JsonResponse({'success': False, 'message': "Invalid form data."}, status=400)
    
# class NewsletterView(FormView):
#     form_class = NewsLetterForm

#     def form_valid(self, form):
#         email = form.cleaned_data['email']
        
#         if Newsletter.objects.filter(email=email).exists():
#             return JsonResponse({'success': False, 'message': "You are already subscribed to the newsletter."})
        
#         form.save()
#         return JsonResponse({'success': True, 'message': "You have successfully subscribed to the newsletter!"})

# class NewsletterSuccessView(TemplateView):
#     def get(self, request, *args, **kwargs):
#         # Return an empty HTTP response
#         return JsonResponse({})
from django.views import View
class NewsletterView(View):
    def post(self, request, *args, **kwargs):
        form = NewsLetterForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            if Newsletter.objects.filter(email=email).exists():
                return JsonResponse({'success': False, 'message': "You are already subscribed to the newsletter."})
            form.save()
            return JsonResponse({'success': True, 'message': "You have successfully subscribed to the newsletter!"})
        else:
            return JsonResponse({'success': False, 'message': "Invalid form data."}, status=400)




def contact(request):
    contactinfos = ContactInfo.objects.latest('created')
    category = Categorys.objects.all()
    tags = Tag.objects.all()
    if request.method == "POST":
        fname = request.POST.get('name')
        femail = request.POST.get('email')
        fsubject = request.POST.get('subject')
        fmessage = request.POST.get('message')

        try:
            # Create and save the contact query
            query = Contact(name=fname, email=femail, subject=fsubject, message=fmessage)
            query.save()

            # Send email
            send_mail(
                'Contact Form Submission',
                f'Name: {fname}\nEmail: {femail}\nSubject: {fsubject}\nMessage: {fmessage}',
                femail,  # Sender's email address
                ['morrishenry502@gmail.com'],  # Recipient's email address
                fail_silently=False,
            )

            # Return a JSON response indicating success
            return JsonResponse({'success': True, 'message': 'Thanks for contacting us! We will get back to you soon.'})
        except Exception as e:
            # Return a JSON response indicating failure
            return JsonResponse({'success': False, 'message': 'An error occurred while processing your request. Please try again later.'})

    # Render the contact form template with CSRF token
    context = {
        'contactinfos': contactinfos,
        'category': category,
        'tags': tags,
    }
    return render(request, 'contact.html', context)


@login_required
def userProfile(request, username):
    tags = Tag.objects.all()
    category = Categorys.objects.all()
    user = get_object_or_404(User, username=username)
    profile = Profile.objects.get_or_create(user=user)[0]  # Get or create the profile for the user
    
    
    context = {
        'profile': profile,
        'user': user,
        'tags': tags,
        'category': category,
    }
    return render(request, 'profile.html', context)

    
@login_required
def profileUpdate(request):
    tags = Tag.objects.all()
    category = Categorys.objects.all()
    user = request.user
    profile = Profile.objects.get(user=user)

    if request.method == "POST":
        form = EditProfileForm(request.POST, request.FILES, instance=profile)
        if form.is_valid():
            new_username = form.cleaned_data.get('username')
            new_email = form.cleaned_data.get('email')
            
            # Check if the new username is unique
            if User.objects.exclude(pk=user.pk).filter(username=new_username).exists():
                messages.error(request, 'Username already exists. Please choose a different one.')
            # Check if the new email is unique
            elif User.objects.exclude(pk=user.pk).filter(email=new_email).exists():
                messages.error(request, 'Email already exists. Please choose a different one.')
            else:
                # Update profile with new data
                user.username = new_username
                user.email = new_email
                profile.image = form.cleaned_data.get('image')
                user.save()
                profile.save()
                return redirect('profile', username=user.username)
    else:
        form = EditProfileForm(instance=profile)
    context = {
        "form": form,
        "tags": tags,
        "category": category,
    }
    return render(request, "update_profile.html", context)
