# Image Resizer Tool

A simple Python script that batch resizes and optionally converts all images in a folder using the Pillow library. This tool automates image resizing tasks to save time and ensure consistency.

## Features

- Resize all images in a specified folder to custom dimensions.
- Supports common image formats like JPG, PNG, BMP, GIF, TIFF.
- Optional image format conversion (e.g., convert PNG to JPEG).
- Automatically creates an output folder if it doesn't exist.
- Gracefully handles errors and skips problematic files.

## Requirements

- Python 3.x
- Pillow library

Install Pillow using pip:

```bash
pip install pillow
