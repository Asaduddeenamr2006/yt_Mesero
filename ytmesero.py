import os
import sys
import yt_dlp
from pathlib import Path


def get_download_path():
    """Create and return the download directory path."""
    download_dir = Path("downloads")
    download_dir.mkdir(exist_ok=True)
    return download_dir


def progress_hook(d):
    """Display download progress in real-time."""
    if d["status"] == "downloading":
        percent = d.get("_percent_str", "N/A").strip()
        speed = d.get("_speed_str", "N/A").strip()
        eta = d.get("_eta_str", "N/A").strip()
        # Print progress on same line
        sys.stdout.write(
            f"\r    [*] Progress: {percent} | Speed: {speed} | ETA: {eta}   "
        )
        sys.stdout.flush()
    elif d["status"] == "finished":
        print(f"\n    [+] Download finished, processing...")


def download_video(url, format_choice, download_dir):
    """Download a single video/audio from YouTube."""
    if format_choice == "mp3":
        ydl_opts = {
            "format": "bestaudio/best",
            "outtmpl": str(download_dir / "%(title)s.%(ext)s"),
            "postprocessors": [{
                "key": "FFmpegExtractAudio",
                "preferredcodec": "mp3",
                "preferredquality": "192",
            }],
            "quiet": True,
            "no_warnings": True,
            "progress_hooks": [progress_hook],
        }
    else:  # mp4
        ydl_opts = {
            "format": "bestvideo[ext=mp4]+bestaudio[ext=m4a]/best[ext=mp4]/best",
            "outtmpl": str(download_dir / "%(title)s.%(ext)s"),
            "merge_output_format": "mp4",
            "quiet": True,
            "no_warnings": True,
            "progress_hooks": [progress_hook],
        }

    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(url, download=True)
            filename = ydl.prepare_filename(info)
            if format_choice == "mp3":
                filename = filename.rsplit(".", 1)[0] + ".mp3"
            print(f"    [+] Saved as: {os.path.basename(filename)}")
            return True
    except Exception as e:
        print(f"\n    [-] Error: {e}")
        return False


def main():
    """Main loop - keep asking for URLs until user exits."""
    print("=" * 50)
    print(" YouTube Downloader")
    print("=" * 50)

    download_dir = get_download_path()
    print(f"[*] Saving to: {download_dir.absolute()}")

    # Choose format once at the start
    while True:
        format_choice = input("\nChoose format (mp3/mp4): ").strip().lower()
        if format_choice in ["mp3", "mp4"]:
            break
        print("[-] Invalid choice. Please enter 'mp3' or 'mp4'")

    print(f"\n[*] Format set to: {format_choice.upper()}")
    print("[*] Paste a YouTube URL to download, or type 'exit' to quit.\n")

    # Main download loop
    download_count = 0
    while True:
        try:
            url = input(f"[{download_count + 1}] URL: ").strip()
        except (EOFError, KeyboardInterrupt):
            print("\n\n[*] Exiting...")
            break

        # Exit commands
        if url.lower() in ["exit", "quit", "q", ""]:
            if url == "":
                continue
            print("[*] Exiting...")
            break

        # Validate URL
        if not url.startswith("http"):
            print("    [-] Invalid URL. Please enter a valid YouTube link.")
            continue

        print(f"    [*] Downloading...")
        if download_video(url, format_choice, download_dir):
            download_count += 1
        print()  # Empty line between downloads

    # Summary
    print("\n" + "=" * 50)
    print(f" Session ended. Downloaded: {download_count} file(s)")
    print(f" Location: {download_dir.absolute()}")
    print("=" * 50)


if __name__ == "__main__":
    main()
