import os
import kaggle

# Set Kaggle API credentials
os.environ['KAGGLE_USERNAME'] = '' # Your username in kaggle
os.environ['KAGGLE_KEY'] = '' # Your kaggle key, inside the settings

# Define dataset details
dataset_name = r'ejlok1/toronto-emotional-speech-set-tess' # get Dataset link, replace with your dataset
output_dir = r''  # You don't need to change the output

# Create the output directory if it doesn't exist
os.makedirs(output_dir, exist_ok=True)

# Print a message indicating the dataset is ready to download
print("The TESS dataset is ready to download.")

# Download and extract the dataset
kaggle.api.dataset_download_files(dataset_name, path=output_dir, unzip=True)

# Print a message when the download is complete
print("Dataset downloaded and extracted successfully!")
