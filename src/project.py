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
