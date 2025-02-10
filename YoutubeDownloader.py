from pytube import YouTube



def HelloWorld(name):
    print("hello World "+name)
HelloWorld("lothar")
HelloWorld("louis")

def DownloadURL(URL):
    video = YouTube(URL)
    video = video.streams.filter(file_extension="mp4").get_highest_resolution()
    video.download()


DownloadURL("https://youtu.be/iwhTPrtNdsI")