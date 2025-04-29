# PixelBeats: A Music-Driven Pixel Art Visualizer

## Demo
Demo Video:

## Github Repository
Github Repo: https://github.com/DemInaArasu/Pixel-Beats

## Description
**PixelBeats** is a generative art project that creates visually dynamic, retro-style pixel art in real-time based on live audio input. It reacts to sound amplitude and frequency patterns to produce evolving pixel grid compositions using a vibrant, shifting color palette. The visuals are saved as a series of image frames that can be compiled into animations, used in VJ performances, or simply enjoyed as digital art.

## Repository Structure
pixelbeats-visualizer/ │ ├── visuals/ # Output image frames from the visualization ├── src/ # Source code folder │ └── project.py # Main program logic (audio input, visuals, saving) ├── README.md # This file ├── proposal.md # Project planning and milestones └── requirements.txt # Third-party libraries needed to run the project

## Design Considerations

- **Pixel Grid Format**: Inspired by retro 8-bit and pixel art styles, visuals are displayed on a 256x256 canvas, divided into 16x16 pixel blocks.
- **Audio-Reactive Visuals**: The visuals respond to real-time audio input using amplitude detection with `sounddevice`.
- **Modular Structure**: The program is organized around a main function and supporting functions for visualization and audio handling, following good coding practices.
- **Color Palettes**: The artwork cycles through a curated color palette that complements the dynamic patterns generated from sound.

## How to run
cd src
project.py Pixel-Beats
