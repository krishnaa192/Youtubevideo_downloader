from pytube import YouTube
# link="https://www.youtube.com/watch?v=JIoj1RYvz1Y&ab_channel=MarwaLoud"
link="https://www.youtube.com/watch?v=WcIcVapfqXw&ab_channel=SelenaGomezVEVO"
ytube=YouTube(link)
# title
# print(ytube.title)
# thumbnail
# print(ytube.thumbnail_url)
vide0=ytube.streams.filter(progressive=True).all()
# vide0=ytube.streams.filter(only_audio=True)
# list all straming 
vid=list(enumerate(vide0))
for i in vid:
    print(i)
    # print(i[1].title)
    # print(i[1].resolution)
    # print(i[1].filesize)
strm=int(input("enter: "))
vide0[strm].download()
print("sucess")