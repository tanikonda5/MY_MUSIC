from django.shortcuts import render,get_object_or_404,redirect
from .models import Album,Song
from django.views import generic
from django.views.generic import View
from django.template import loader
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate,login,logout
from .forms import UserForm
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator#to add decorator
# Create your views here.
from django.http import HttpResponse
from django.http import Http404
from django.core.mail import send_mail




#def index(request):
 #   albums=Album.objects.all()
    #template = loader.get_template('music/index.html')
  #  context ={
   #     'albums':albums
    #}
    #return HttpResponse(template.render(context,request))
    #return render(request, 'music/index.html', context)

#def detail(request,album_id):
    #return HttpResponse("<h1>the album "+album_id+"</h1>")

    #try:
     #   album=Album.objects.get(pk=album_id)
    #except Album.DoesNotExist:
     #   raise Http404("Album Does not Exist")


    #http shortcut
 #   album = get_object_or_404(Album,pk=album_id)

  #  context = {
   #     'album': album
    #}
    #return render(request,'music/details.html',context)

#def favorite(request,album_id):
 #   album = get_object_or_404(Album, pk=album_id)
  #  try:
   #     selected_song=album.song_set.get(pk=request.POST['song'])
    #except (KeyError,Song.DoesNotExist):
     #   return render(request,'music/details.html',{'album':album , 'error_msg':'your song does not exits' })
    #else:
     #   selected_song.is_fav=True;
      #  selected_song.save()
       # return render(request,'music/details.html',{'album':album })

def logout_view(request):
    logout(request)
    return redirect('login')


@method_decorator(login_required, name = 'dispatch')
class IndexView(generic.ListView):
    template_name = 'music/index.html'
    context_object_name = 'albums'

    def get_queryset(self):
        return Album.objects.all()


class DetailView(generic.DetailView):
    model = Album
    template_name = 'music/details.html'

    def get_queryset(self):
        return Album.objects.all()


class AlbumCreate(CreateView):
    model = Album
    fields = ['title','singer','year','album_logo']
    template_name = 'music/album_form.html'


class SongCreate(CreateView):
    model = Song
    fields = ['album','file_type','song_title','is_fav']
    template_name = 'music/song_form.html'


class AlbumUpdate(UpdateView):
    model = Album
    fields = ['title', 'singer', 'year', 'album_logo']


class AlbumDelete(DeleteView):
    model = Album
    success_url = reverse_lazy('music:index')


class UserFormView(View):
    form_class = UserForm
    template_name = 'music/registration_form.html'

    #display blank form
    def get(self,request):
        form = self.form_class(None)
        return render(request,self.template_name, {'form':form})


    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user= form.save(commit = False) # stores the info locally

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            user = authenticate(username = username, password = password)

            if user is not None:

                if user.is_active:
                    login(request, user)
                    return redirect('login')# replaces index page



        return render(request,self.template_name, {'form':form})








