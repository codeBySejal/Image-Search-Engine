# Image-Search-Engine
Image Search Application using open source implementation of Open AI's CLIP model

This is an image search application that uses the open-source implementation of OpenAI's CLIP model to enable text-based image search. The application converts images into embeddings and stores them in a vector database, Chroma DB. The user can search for images by providing a text query, which is converted into embeddings and compared against the stored embeddings to find the most relevant images.

Key Features:
1. Text-based Image Search: Input text descriptions to find matching images.
2. CLIP-based Embeddings: Uses OpenAI's CLIP model to generate embeddings for both images and text.
3. Chroma Vector Database: Stores image embeddings for efficient retrieval.
4. Scalable: Easily extendable to accommodate larger datasets.

Tech Stack:
1. Python
2. OpenAI's CLIP Model (open-source implementation)
3. Chroma DB (for storing and searching vector embeddings)
4. Streamlit

HOW TO USE: 
Install dependencies: Install all required Python packages by running: pip install -r requirements.txt
Store Images in Chroma DB: Convert and store the images as embeddings in the vector database: python add_images.py
Search for Images by Text: Run the search script to search for images using text descriptions: python image_search.py

How it Works:
Embedding Creation: The add_images.py script processes each image, converts it into a CLIP embedding, and stores the embeddings in Chroma DB.
Text-based Search: The image_search.py script takes a text query, converts it into a CLIP embedding, and compares it against the stored image embeddings in Chroma DB to return the closest matches.
