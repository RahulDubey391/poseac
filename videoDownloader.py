from pytube import YouTube
import pandas as pd

def getInputVideoFiles(YT_LIST_FILE):
    try:
        df = pd.read_csv(YT_LIST_FILE)
        links = df['links'].tolist()
        return links
    
    except Exception as e:
        raise(e)


def downloadYtVideo(video_links,
                    UPLOAD_FOLDER):
    if video_links:
        for link in video_links:
            try:
                yt = YouTube(link.strip())
                stream = yt.streams.get_highest_resolution()
                filename = stream.default_filename
                stream.download(output_path=UPLOAD_FOLDER)
                print('Video downloaded Successfully!')
            except Exception as e:
                print(f"Error downloading video: {str(e)}")

        return True
    else:
        return False
    