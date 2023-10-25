""" 
This script post-processes label masks produced and exported using Gimp

Seems like it's actually not necessary.

This includes the following steps:
1. Identify all masks in a folder. For all masks that haven't been processed yet:
2. Threshold at 127 and set to 0 and 1 instead of 0 and 255
3. Reduce to a single channel instead of 4 channels
4. Save in new folder
"""

import os
import imageio
import argparse

def create_mask(input_folder, output_folder):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Get a list of PNG files in the input folder
    png_files = [f for f in os.listdir(input_folder) if f.lower().endswith('.png')]

    for png_file in png_files:
        input_path = os.path.join(input_folder, png_file)
        output_path = os.path.join(output_folder, png_file)

        # Load the PNG image
        image = imageio.imread(input_path)

        # Extract the first channel
        channel1 = image[:, :, 0]

        # Threshold the first channel at 127 to create the mask
        mask = (channel1 > 127).astype('uint8') * 255

        # Save the mask as a new PNG image
        imageio.imwrite(output_path, mask)

        print(f"Mask saved to {output_path}")

if __name__ == "__main__":
    # input_folder = input("Enter the input folder path: ")
    # output_folder = input("Enter the output folder path: ")

    parser = argparse.ArgumentParser(description='Postprocessing of gimp label pngs.')
    parser.add_argument('input_folder', type=str,
                        help='Enter the input folder path')
    parser.add_argument('output_folder', type=str,
                        help='Enter the output folder path')

    args = parser.parse_args()

    create_mask(args.input_folder, args.output_folder)
