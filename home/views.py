from django.shortcuts import render
from pytube import YouTube


def index(request):
    try:
        url = request.POST.get('yt-url')
        yt = YouTube(url)
        yt.streams.filter(progressive=True, file_extension='mp4').order_by(
            'resolution').desc().first().download()
    except Exception as e:
        print(e)
    return render(request, 'index.html', {'url': url})
