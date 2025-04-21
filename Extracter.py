import csv
import os
import sys
import logging
from moviepy.editor import VideoFileClip
import datetime

# --- Config ---
CSV_FILE = 'squid_game_s2_ep7.csv'         # Path to input CSV
VIDEO_FILE = 'Squid.Game.S02E07.ENG.1080p.NF.x264-[y2flix.cc].mp4'    # Path to input video
CLIPPED_DIR = 'squid_game_s2_ep7'           # Output folder for clips

# --- Logging ---
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

# --- Helpers ---
def parse_time(time_str):
    """Parse time string (HH:MM:SS.ms or MM:SS.ms) to seconds."""
    if not time_str:
        return None
    try:
        time_str = time_str.replace(',', '.')
        parts = time_str.split(':')
        parts = [float(p) for p in parts]
        if len(parts) == 3:
            return parts[0] * 3600 + parts[1] * 60 + parts[2]
        elif len(parts) == 2:
            return parts[0] * 60 + parts[1]
        else:
            return parts[0]
    except Exception as e:
        logging.warning(f"Failed to parse time '{time_str}': {e}")
        return None

# --- Ensure output folder exists ---
os.makedirs(CLIPPED_DIR, exist_ok=True)

# --- Process ---
try:
    with open(CSV_FILE, 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        with VideoFileClip(VIDEO_FILE) as video:
            for idx, row in enumerate(reader, 1):
                start = parse_time(row['start_timestamp'])
                end = parse_time(row['end_timestamp'])
                segment_name = row['event_id']
                if start is None or end is None or end <= start:
                    logging.warning(f"Skipping segment {idx}: Invalid times (start={start}, end={end})")
                    continue

                logging.info(f"Clipping Segment {idx}: {start:.2f}s → {end:.2f}s")
                clip = video.subclip(start, end)
                
                # Save the video clip
                video_out_path = os.path.join(CLIPPED_DIR, f"{segment_name}.mp4")
                clip.write_videofile(video_out_path, codec='libx264', audio_codec='aac', preset='ultrafast', logger=None)
                
                # Extract and save the audio
                audio = clip.audio
                audio_out_path = os.path.join(CLIPPED_DIR, f"{segment_name}.mp3")
                audio.write_audiofile(audio_out_path, codec='mp3', logger=None)

except FileNotFoundError as e:
    logging.error(f"File not found: {e.filename}")
    sys.exit(1)
except Exception as e:
    logging.error(f"Unexpected error: {e}")
    sys.exit(1)
