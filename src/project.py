import numpy as np
import sounddevice as sd
from PIL import Image, ImageDraw
import time
import os

# Parameters
WIDTH, HEIGHT = 256, 256
FPS = 15
PIXEL_SIZE = 16
PALETTE = [(0, 0, 0), (255, 0, 0), (255, 255, 0), (0, 255, 0), (0, 255, 255), (0, 0, 255), (255, 0, 255)]

# Create visuals folder if not exists
os.makedirs("visuals", exist_ok=True)

def audio_callback(indata, frames, time, status):
    global amplitude
    amplitude = np.linalg.norm(indata) * 10

def generate_pixel_art(amplitude):
    image = Image.new("RGB", (WIDTH, HEIGHT), (0, 0, 0))
    draw = ImageDraw.Draw(image)
    for x in range(0, WIDTH, PIXEL_SIZE):
        for y in range(0, HEIGHT, PIXEL_SIZE):
            index = int((np.sin(x * 0.1 + time.time()) + np.cos(y * 0.1 + time.time()) + amplitude) % len(PALETTE))
            draw.rectangle([x, y, x + PIXEL_SIZE, y + PIXEL_SIZE], fill=PALETTE[index])
    return image

def save_image(image, frame):
    image.save(f"visuals/frame_{frame:04d}.png")

def main():
    print("Starting PixelBeats Visualizer... Press Ctrl+C to stop.")
    global amplitude
    amplitude = 0.0
    frame = 0
    
    with sd.InputStream(callback=audio_callback):
        try:
            while True:
                img = generate_pixel_art(amplitude)
                save_image(img, frame)
                frame += 1
                time.sleep(1 / FPS)
        except KeyboardInterrupt:
            print("\nVisualization stopped.")

if __name__ == "__main__":
    main()
