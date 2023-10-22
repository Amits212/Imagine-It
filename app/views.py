from django.http import HttpResponse, JsonResponse
from django.template import loader
from .forms import VideoForm
from django.shortcuts import render, redirect
from .models import Video, Comment

def login(request):
  template = loader.get_template('login.html')
  context = {'context': None}
  return HttpResponse(template.render(context, request))


def home(request):
  filter_param = request.GET.get('video_name')
  all_videos = Video.objects.all()

  if filter_param:
    all_videos = Video.objects.filter(caption__icontains=filter_param)

  return render(request, 'home.html', {'all_videos': all_videos})

def upload(request):
  all_videos = Video.objects.all()
  if request.method == "POST":
    form = VideoForm(request.POST, request.FILES)
    if form.is_valid():
      form.save()
      return redirect("http://127.0.0.1:8000/login/home/")
  else:
    form = VideoForm()
  return render(request, 'upload.html', {'form': form, 'all_videos': all_videos})

def delete_video(request, video_id):
  if request.method == 'POST':
    video = Video.objects.get(pk=video_id)
    video.delete()
  return redirect('home')


def increment_like(request, video_id):
  if request.method == 'POST':
    video = Video.objects.get(pk=video_id)
    video.increment_likes()
    return JsonResponse({'likes': video.like})
  return redirect('home')

def add_comment(request, video_id):
  if request.method == 'POST':
    video = Video.objects.get(pk=video_id)
    comment_text = request.POST.get('comment_text')
    Comment.objects.create(video=video, text=comment_text)
  return redirect('home')
