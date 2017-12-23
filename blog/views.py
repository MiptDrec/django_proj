import random
from django.shortcuts import render, get_object_or_404,redirect
from django.utils import timezone
from .models import Post, Activities,Sets
from .forms import SetsForm,UploadPhotoToSets
best_articles = Post.objects.order_by('-views').all()[:3]

# Create your views here.
def main(request):
	sets = Sets.objects.all()
	prev_s = preview_for_table(sets)

	return render(request, 'blog/main.html', {'posts':sets,'prevs':prev_s})

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
	prev = preview_of_set(activities.sets)
	return render(request, 'blog/activities.html', {'activities': activities,'pre':prev } )

  
def gen_sets(request, pk3):
	age_sets = Sets.objects.filter(age__contains=pk3)	
	return render(request, 'blog/age_set.html', {'age':pk3,'age_sets':preview_for_table(age_sets)})

def sets(request, pk):
	sets_ = Sets.objects.order_by('pk').reverse()
	max_id = sets_[1].id
	other_sets = []
	similar = set()
	for i in range(3):
		
		while True:
			random_id = random.randint(0, max_id)
			if random_id not in similar:
				break
		other_sets.append(preview_of_set(sets_[random_id]))
		similar.add(random_id)
	set_ = Sets.objects.get(pk = pk)
	
	active = Activities.objects.filter(sets=set_.brief)
	return render(request, 'blog/set.html', {'sets':set_, 'active':active, 'r':max_id,'other':other_sets})	

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

def preview_of_set(b):
	string = '<div class="preview">'
	string += '<a href="/sets/'+str(b.pk)+'">'+b.title+'</a> <br><img width=80% src="'
	string += b.main_image.url+'"\></div></a>'
	return string
def preview_for_table(b):
	string = '<table border = 1 table-layout="fixed" width=100%><tr width=2%>'
	for i in range(0,len(b)):
		if (i+1) % 4 == 0:
			string += '</tr><tr width=2%>'
		string+='<td width=2%>'+preview_of_set(b[i])+'</td>'
	string +=  '</tr></table>'
	return string
