import os

import cv2
import numpy as np


def get_video(message: str, path: str):
    message = message.replace('ё', 'е')
    title = message if message and len(message) > 0 else "empty"
    path = os.path.join(path, f"{title}.mp4")
    if os.path.exists(path):
        return {'title': title, 'path': path}
    width, height = 100, 100
    fps = 30
    duration_seconds = 3
    out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))
    frame = np.zeros((height, width, 3), dtype=np.uint8)

    font = cv2.FONT_HERSHEY_COMPLEX
    font_scale = 1
    font_thickness = 1
    font_color = (255, 255, 255)

    message_size, _ = cv2.getTextSize(message, font, font_scale, font_thickness)
    y = height // 2
    delta = max(message_size[0] // (fps*duration_seconds), 1)

    for x in range(width // 2 - delta, width // 2 - delta * fps * duration_seconds - delta, -delta):
        frame.fill(0)
        cv2.putText(frame, message, (x, y), font, font_scale, font_color, font_thickness)
        out.write(frame)

    out.release()

    return {'title': title, 'path': path}
