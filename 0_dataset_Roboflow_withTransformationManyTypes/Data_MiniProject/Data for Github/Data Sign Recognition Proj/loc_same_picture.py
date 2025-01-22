import os
import cv2
import hashlib

def dhash(image, hash_size=8):
    """Compute the difference hash of the image."""
    resized = cv2.resize(image, (hash_size + 1, hash_size))
    diff = resized[:, 1:] > resized[:, :-1]
    return sum([2 ** i for (i, v) in enumerate(diff.flatten()) if v])

def remove_duplicates(directory):
    """Remove duplicate images from a directory."""
    image_hashes = {}
    for filename in os.listdir(directory):
        filepath = os.path.join(directory, filename)
        if os.path.isfile(filepath):
            image = cv2.imread(filepath, cv2.IMREAD_GRAYSCALE)
            if image is not None:
                h = dhash(image)
                if h in image_hashes:
                    print(f"Duplicate found: {filename} and {image_hashes[h]}")
                    os.remove(filepath)
                else:
                    image_hashes[h] = filename

# Sử dụng hàm
directory_path = "same_name"  # Relative path
remove_duplicates(directory_path)
