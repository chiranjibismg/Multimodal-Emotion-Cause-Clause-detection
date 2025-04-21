# Multimodal-Emotion-Cause-Clause-detection


Group 3 
Chiranjibi Pradhan
Swapnil Srivastava
Ayush Sharma

# Multimodal Fear Detection

This Jupyter Notebook implements a multimodal pipeline for detecting fear and cause segments in short video clips, using subtitles (SRT), video frames, audio, and a Transformer + 3D‑CNN backbone.

---

📋 Contents

- `main_code.ipynb` – the main notebook  
- `mapping.json` – a JSON map from video to subtitle file  
- `data/` – directory containing your `.mp4` and `.srt` files  

---

## 🛠️ Requirements

1. **Python** ≥ 3.7  
2. **pip**  
3. **ffmpeg** (for `moviepy`)  
4. *(Optional)* A CUDA‑enabled GPU for PyTorch acceleration  

---

## ⚙️ Installation

1. **Clone** this repo (or place the notebook in your project folder).  
2. **Create & activate** a virtual environment (recommended):
   ```bash
   python3 -m venv venv
   source venv/bin/activate      # Linux / macOS
   venv\Scripts\activate       # Windows PowerShell
   ```
3. **Install** Python dependencies:
   ```bash
   pip install torch torchvision torchaudio transformers \
               moviepy scikit-learn pandas numpy tqdm
   ```
4. **Install** system‑level packages:
   ```bash
   # Ubuntu / Debian:
   sudo apt-get update && sudo apt-get install -y ffmpeg
   # macOS (with Homebrew):
   brew install ffmpeg
   ```

---

## 🗂️ Data Preparation

1. **Organize** your raw files:
   ```
   data/
     ├─ clip1.mp4
     ├─ clip1.srt
     ├─ clip2.mp4
     ├─ clip2.srt
     └─ …
   ```
2. **Create** a JSON mapping file (`mapping.json`) in the project root:
   ```json
   {
     "data/clip1.mp4": "data/clip1.srt",
     "data/clip2.mp4": "data/clip2.srt"
   }
   ```

---

## 🚀 Running the Notebook

1. **Launch** Jupyter Notebook:
   ```bash
   jupyter notebook main_code.ipynb
   ```
2. **Execute** each cell in order:
   - The first cell installs packages—you may skip it if you installed them already.
   - Ensure the `mapping.json` path is correct and that `json_av_srt_map` loads properly.

---

## 🔍 Key Usage Snippets

```python
import json
from torch.utils.data import DataLoader
from main_code import build_entries_from_mapping, MultimodalFearDataset

# 1. Load mapping
with open('mapping.json', 'r') as f:
    json_av_srt_map = json.load(f)

# 2. Build entries
entries = build_entries_from_mapping(json_av_srt_map)

# 3. Create Dataset & DataLoader
dataset = MultimodalFearDataset(entries)
loader = DataLoader(dataset, batch_size=4, shuffle=True)

# 4. Run one batch inference
for text, video, audio, labels in loader:
    text_tokens = {k: v.to(device) for k, v in text.items()}
    video, audio, labels = video.to(device), audio.to(device), labels.to(device)
    preds = model(text_tokens, video, audio).detach()
    print(preds, labels)
    break
```

---
