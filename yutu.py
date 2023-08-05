from pytube import YouTube

def download_video(url, output_path='./'):
    try:
        yt = YouTube(url)
        video = yt.streams.get_highest_resolution()  # Get the highest resolution stream

        print(f"Downloading '{yt.title}'...")

        # Setting the output path and filename
        output_file = f"{output_path}{yt.title}.mp4"
        
        # Download the video
        video.download(output_path=output_path, filename=yt.title)

        print("Download complete!")

    except Exception as e:
        print("An error occurred:", str(e))

if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    download_video(video_url)
