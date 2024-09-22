from PIL import Image
import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import numpy as np
from tqdm import tqdm
import os


client = chromadb.PersistentClient(path='vector_db')
embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()

collection = client.get_or_create_collection (
    name = 'clip_collection',
    embedding_function= embedding_function,
    data_loader= data_loader,
)

def add_images_to_collection(folder_path):
    image_files = [os.path.join(folder_path,image_name) for image_name in 
    os.listdir(folder_path)]

    for image_path in image_files:
        try:
            image = np.array(Image.open(image_path))
            collection.add(
                ids = [os.path.basename(image_path)],
                images=[image]
            )
        except Exception as e:
            print(f'Error processing {image_path}: {e}')
        
image_folder_path = 'images'
add_images_to_collection(image_folder_path)