import imageio
import json

# Load program options from config file
with open('configs/config.json') as config_file:
    config = json.load(config_file) 

# Setup your target indices to show transformations forward and in reverse   
image_indices = [x for x in range(config['NUM_FRAMES'])]
reverse_image_indices = image_indices[::-1] 
total_indices = image_indices + reverse_image_indices

# Iterate over all target indices and append each image to an array
image_array = []
for file_num in total_indices:
    image_array.append(imageio.imread(config['IMAGES_PATH'] + config['IMAGE_PREFIX'] + str(file_num) + '.' + config['IMAGE_TYPE']))

# Save your image array as the file type specified in your save path
imageio.mimsave(config['VIDEO_SAVE_PATH'], image_array, fps = config['FPS'])