
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Activities,Sets, Photo
from .forms import SetsForm,UploadPhotoToSets
best_articles = Post.objects.order_by('-views').all()[:3]

# Create your views here.
def main(request):
	posts = Sets.objects.all()
	best_articles = Post.objects.order_by('-views').all()[:3]
	return render(request, 'blog/main.html', {'posts':posts, 'best_articles':best_articles})
def post_detail(request,pk):
	post = get_object_or_404(Post, pk=pk)
	postview =  Post.objects.get(pk=pk)
	if postview:
		postview.views = postview.views + 1
	postview.save()
	best_articles = Post.objects.order_by('-views').all()[:3]
	return render(request, 'blog/post_detail.html', {'post': post, 'best_articles':best_articles})
def activities(request, pk1):
	activities = get_object_or_404(Activities, pk=pk1)
	return render(request, 'blog/activities.html', {'activities': activities, 'best_articles':best_articles})
def age_of_activities(request,pk3):
	activities = Activities.objects.filter(age__contains=pk3)
	string = 'blog/'+pk3+'-'+str(int(pk3)+1)+'.html'
	return render(request, string, {'post': pk3, 'activities': activities, 'best_articles':best_articles})   
def sets(request, pk):
	imgs = Photo.objects.filter(sets = pk)
	sets = Sets.objects.get(pk = pk)
	return render(request, 'blog/set.html', {'sets':sets, 'imgs':imgs})	

def sets_new(request):
	if request.method == "POST":
		form = UploadPhotoToSets(request.POST, request.FILES)
		if form.is_valid():
			sets = Sets.objects.get(pk = 1)
			sets.add_photo( form.cleaned_data['pic'])
			sets.photos.append(form.cleaned_data['pic'])
			sets.save()
			return redirect('main')
	else:
		form = UploadPhotoToSets()
	return render(request, 'blog/set_edit.html', {'form': form})
