import os
import yt_dlp

def get_user_input():
    print("🔗 YouTube Downloader for Video or Playlist")
    url = input("Enter YouTube video or playlist URL: ").strip()
    return url

def main():
    url = get_user_input()

    # Output folder: YouTube_Downloads in current directory
    output_folder = os.path.join(os.getcwd(), "YouTube_Downloads")
    os.makedirs(output_folder, exist_ok=True)

    # yt-dlp options for high-quality downloads
    ydl_opts = {
        'outtmpl': os.path.join(output_folder, '%(playlist_title)s/%(playlist_index)s - %(title)s.%(ext)s'),
        'format': 'bestvideo[ext=mp4]+bestaudio[ext=m4a]/best',
        'merge_output_format': 'mp4',
        'noplaylist': False,
        'ignoreerrors': True,
        'quiet': False,
        'postprocessors': [{
            'key': 'FFmpegVideoConvertor',
            'preferedformat': 'mp4',
        }],
    }

    print(f"\n📥 Downloading from: {url}\n")

    # Run yt-dlp
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    print(f"\n✅ Download complete! Files saved in: {output_folder}")

if __name__ == '__main__':
    main()
