# YouTube Downloader CLI

A lightweight Python script for downloading YouTube videos or extracting audio. It runs in an interactive loop, allowing multiple sequential downloads without restarting the program.

## Prerequisites

- **Python 3.x**
- **yt-dlp**: The core downloading library.
  ```bash
  pip install yt-dlp
  ```
  *(Recommended: Use a virtual environment `python3 -m venv venv` to avoid conflicts with system-managed Python packages).*
- **FFmpeg**: Required only if you choose the `mp3` format for audio extraction and conversion. Install it via your system's default package manager (e.g., `apt`, `brew`, `winget`, `xbps`).

## Usage

1. Run the script from your terminal:
   ```bash
   python ytmesero.py
   ```
2. Select the desired output format when prompted (`mp3` or `mp4`).
3. Paste a YouTube URL and press `Enter`. The download progress will display in real-time.
4. Once finished, the prompt will return for the next URL.
5. To exit the program, type `exit`, `q`, or press `Ctrl+C`.

## Example Session

```text
==================================================
 YouTube Downloader
==================================================
[*] Saving to: /path/to/project/downloads

Choose format (mp3/mp4): mp4

[*] Format set to: MP4
[*] Paste a YouTube URL to download, or type 'exit' to quit.

[1] URL: https://www.youtube.com/watch?v=dQw4w9WgXcQ
    [*] Downloading...
    [download] 100% of 15.20MiB in 00:02
    [+] Saved as: Example Video Title.mp4

[2] URL: exit
[*] Exiting...

==================================================
 Session ended. Downloaded: 1 file(s)
 Location: /path/to/project/downloads
==================================================
```

## Notes

- All downloaded files are automatically saved in a `downloads` directory created in the same folder as the script.
- If you encounter a `ModuleNotFoundError: No module named 'yt_dlp'`, ensure your virtual environment is activated or that the package was installed for the correct Python interpreter.
