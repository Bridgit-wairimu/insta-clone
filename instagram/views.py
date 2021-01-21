from django.shortcuts  import render,redirect,get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import NewPostForm,EditProfileForm,CommentForm,SignupForm, InstaLetterForm

from .models import Post,Profile,Likes,Comment
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import User
from django.urls import reverse

# Create your views here.
def welcome(request):
    images = Post.objects.all()
    current_user = request.user
    users = Profile.objects.all()
	
    if request.method == 'POST':
        form = NewPostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.profile
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = NewPostForm()
    params = {
        'images': images,
        'form': form,
        'users': users,

    }
    return render(request, 'welcome.html', params)


@login_required(login_url='/accounts/login/')
def profile(request):
        
	return render(request,'profile.html')
	


@login_required
def NewPost(request):
	user = request.user
	files_objs = []

	if request.method == 'POST':
		form = NewPostForm(request.POST, request.FILES)
		if form.is_valid():
			files = request.FILES.getlist('content')
			caption = form.cleaned_data.get('caption')

			for file in files:
				file_instance = PostFileContent(file=file, user=user)
				file_instance.save()
				files_objs.append(file_instance)

			p, created = Post.objects.get_or_create(caption=caption, user=user)
			p.save()
			return redirect('welcome')
	else:
		form = NewPostForm()

	context = {
		'form':form,
	}

	return render(request, 'newpost.html', context)



@login_required
def EditProfile(request):
	user = request.user.id
	profile = Profile.objects.get(user__id=user)
	BASE_WIDTH = 400

	if request.method == 'POST':
		form = EditProfileForm(request.POST, request.FILES)
		if form.is_valid():
			profile.picture = form.cleaned_data.get('picture')
			profile.first_name = form.cleaned_data.get('first_name')
			profile.last_name = form.cleaned_data.get('last_name')
			profile.location = form.cleaned_data.get('location')
			profile.url = form.cleaned_data.get('url')
			profile.profile_info = form.cleaned_data.get('profile_info')
			profile.save()
			return redirect('profile')
	else:
		form = EditProfileForm()

	context = {
		'form':form,
	}

	return render(request, 'edit_profile.html', context)


@login_required(login_url='/accounts/login/')
def comment(request):
    current_user = request.user
    if request.method == 'POST':
        form = CommentForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.Author = current_user
            post.save()
        return redirect('welcome')

    else:
        form = CommentForm()
    return render(request, 'one_post.html', {"form": form})


def like(request):
    image = get_object_or_404(Post, id=request.POST.get('id'))
    is_liked = False
    if image.likes.filter(id=request.user.id).exists():
        image.likes.remove(request.user)
        is_liked = False
    else:
        image.likes.add(request.user)
        is_liked = False

    params = {
        'image': image,
        'is_liked': is_liked,
        'total_likes': image.total_likes()
    }
    return render(request, 'likepage.html',params)



@login_required(login_url='login')
def search_profile(request):
    
	if 'search' in request.GET and request.GET["search"]:
		
		search_term = request.GET.get("search")
		profiles = Profile.objects.filter(user__username__icontains = search_term)
		message = f"{search_term}"

		return render(request,'search.html',{"message":message,"profiles":profiles})
	else:
		message = "You haven't searched for any item"
		return render(request,'search.html',{"message":message})



