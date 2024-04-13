from django.contrib import admin
from .models import Subscription, Newsletter,Home,About,ProfileInfo,Portfolio,ContactInfo,Contact,Education,Experience,Service,ProgressModel,Profile


class ProfileInfoInline(admin.TabularInline):
    model = ProfileInfo
    extra = 1
    fieldsets = (
        ('Personal Information', {

            'fields': ('birthday', 'website', 'degree', 'city', 'email', 'phone', 'freelance', 'country'),
        }),

    )
    
class ProgressModelInline(admin.TabularInline):
    model = ProgressModel
    extra = 1

class EducationInline(admin.TabularInline):
    model = Education
    extra = 1

class ExperienceInline(admin.TabularInline):
    model = Experience
    extra = 1

@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    inlines = [
        ProfileInfoInline,
        ProgressModelInline,
        EducationInline,
        ExperienceInline
    ]

admin.site.register(Subscription)
admin.site.register(Newsletter)
admin.site.register(Home)
admin.site.register(Contact)
admin.site.register(ContactInfo)
admin.site.register(Portfolio)
admin.site.register(Service)
admin.site.register(Profile)

