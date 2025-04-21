# Multimodal-Emotion-Cause-Clause-detection


Group 3 
Chiranjibi Pradhan
Swapnil Srivastava
Ayush Sharma

# 🎬 Multimodal Fear Emotion Segment Extractor

This Jupyter Notebook processes `.srt` subtitle files, audio, and video files to extract fear-inducing segments using a combination of NLP and audio/video analysis. The system uses DistilBERT for text processing and Torch libraries for audio/video handling.

---

## 📦 Requirements

Before running the notebook, install the following dependencies:

## bash
pip install torch torchvision torchaudio transformers moviepy pandas


##Directory Structure
project_root/
├── main_code.ipynb
├── data/
│   ├── sample_video.mp4
│   ├── sample_audio.wav
│   ├── subtitles.srt
│   └── segments.csv
