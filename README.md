# ol-pose-estimation

# SCRIPTS
get_frames_from_image.py
- summary: converts .mp4 video into frames and saves each as an .png image
- inputs: .mp4 video
- outputs: folder of .png images


# FOLDERS
- frames_raw: raw .png iamges of the frames
- labels_json: .json labeled for labelme
- labels_txt: YOLO formatted labels
- train:
- yolo_data:
    - images:
    - labels:
    - data.yaml
- runs:
    - detect:
      - predict_master:
      - train
