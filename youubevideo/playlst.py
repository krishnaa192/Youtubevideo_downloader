from pytube import Playlist
py=Playlist("https://www.youtube.com/watch?v=JD-age0BPVo&list=PLzMcBGfZo4-kCLWnGmK0jUBmGLaJxvi4j&ab_channel=TechWithTim")
print(f'Downloading:{py.title}')
for video in py.videos:
    video.streams.first().download()