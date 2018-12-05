from django.shortcuts import render,get_object_or_404
from django.contrib import messages
# Create your views here.
from django.contrib.auth.mixins import LoginRequiredMixin,PermissionRequiredMixin
from django.urls import reverse
from django.views import generic
from subreddits.models import SubReddit,SubRedditMember

class CreateSubReddit(LoginRequiredMixin,generic.CreateView):
    fields = ('name','description')
    model = SubReddit

class SingleSubReddit(generic.DetailView):
    model = SubReddit

class ListSubReddit(generic.ListView):
    model = SubReddit

class JoinSubReddit(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('subreddits:single',kwargs={'slug':self.kwargs.get('slug')})

    def get(self,request,*args,**kwargs):
        subreddit = get_object_or_404(SubReddit,slug=self.kwargs.get('slug'))

        try:
            SubRedditMember.objects.create(user=self.request.user,subreddit=subreddit)
        except:
            messages.warning(self.request,'Already a Member!!!')
        else:
            messages.success(self.request,'You are now a member')

        return super().get(request,*args,**kwargs)


class LeaveSubReddit(LoginRequiredMixin,generic.RedirectView):
    def get_redirect_url(self,*args,**kwargs):
        return reverse('subreddits:single',kwargs={'slug':self.kwargs.get('slug')})

    def get (self,request,*args,**kwargs):
        try:
            membership = models.SubRedditMember.objects.filter(
                user = self.request.user,
                subreddit__slug = self.kwargs.get('slug')
            ).get()
        except models.SubRedditMember.DoesNotExist:
            messages.warning(self.request,'Sorry! you are not in this Subreddit')

        else:
            membership.delete()
            messages.success(self.request,'You have left the SubReddit')

        return super().get(request,*args,**kwargs)
