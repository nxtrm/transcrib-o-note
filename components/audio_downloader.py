import yt_dlp
import os

def download_audio(youtube_url,output_dir ):
    #downloader options
    options = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(output_dir, '%(title)s.%(ext)s'),  # Specify the output directory and filename template
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    #downloading
    with yt_dlp.YoutubeDL(options) as ydl:
        info = ydl.extract_info(youtube_url, download=False)
        ydl.download([youtube_url])

        file_name = ydl.prepare_filename(info)

    #making a correct path (idk why it does it)
    file = file_name[:-4] +"mp3"

    return file
