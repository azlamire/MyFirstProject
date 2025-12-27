import pytube
for link in pytube.Playlist('https://youtube.com/playlist?list=PLMsYwX5jgZjHcMBi5SdniHYyVh8Nlw93n&si=tsOYwfrbUE55xEto'):
    YtUrl = pytube.YouTube(link)
    audio = YtUrl.streams.get_audio_only().download()
