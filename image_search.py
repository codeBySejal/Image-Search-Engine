import streamlit as st
import chromadb
from chromadb.utils.embedding_functions import OpenCLIPEmbeddingFunction
from chromadb.utils.data_loaders import ImageLoader
import os

client = chromadb.PersistentClient(path='vector_db')
embedding_function = OpenCLIPEmbeddingFunction()
data_loader = ImageLoader()

collection = client.get_or_create_collection (
    name = 'clip_collection',
    embedding_function= embedding_function,
    data_loader= data_loader,
)

banner_image_path = 'ai-search-banner.jpg'
st.image(banner_image_path,use_column_width = True)

st.title('Image Search Engine')

query = st.text_input('Enter your search query: ')
parent_path = 'images'
if st.button('Search'):
    results = collection.query(query_texts=[query],n_results=3,include = ["distances"])
    for image_id,distance in zip(results['ids'][0], results['distances'][0]):
        image_path = os.path.join(parent_path,image_id)
        st.image(image_path,caption = os.path.basename(image_path))
        st.write(f'Distance: {distance}')

