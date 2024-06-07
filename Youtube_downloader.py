import time
from pytube import YouTube 


video_url = input ("Кидай ссылку епта")
save_location = "D:\загрузки"

yt = YouTube(video_url)

stream = yt.streams.filter (res='720p', progressive=True).first()
stream.download(output_path=save_location)
time.sleep(10)