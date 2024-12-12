from pytube import YouTube
while True:
    url=input("URL do vídeo:")
    yt = YouTube(url)
    print(yt.title)
    opt=input("Para baixar video digite '1' para audio digite '2': ")
    print(opt)
    print(type(opt))
    if opt == "1":
        videos = yt.streams.filter(mime_type="video/mp4")
        for video in videos:
            print(video)
    elif opt == '2':
        videos = yt.streams.filter(mime_type="audio/mp4")
        for video in videos:
            print(video)
    else:
        print("o valor digitado não é válido!")
    print("===========================================")
    itag = input("Digite o itag do video: ")
    stream = yt.streams.get_by_itag(itag)
    print(stream)
    stream.download(output_path="/home/hmoura/Vídeos")