import pytest
from project import extract_video_info, show_video_info, convert_video_format

# Test function for extract_video_info
def test_extract_video_info():
    assert extract_video_info("https://www.youtube.com/watch?v=dQw4w9WgXcQ") == "Dummy Video Information"

# Test function for show_video_info
def test_show_video_info():
    video_info = {"title": "Dummy Video", "duration": "00:05:00", "resolution": "720p"}
    assert show_video_info(video_info) == True

# Test function for convert_video_format
def test_convert_video_format():
    input_format = "mp4"
    output_format = "avi"
    video_file_path = "path/to/input_video.mp4"
    assert convert_video_format(video_file_path, output_format) == "path/to/output_video.avi"
