import pandas as pd
from sklearn.decomposition import PCA
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

# Load the dataset with appropriate encoding
data = pd.read_csv('dataset.csv', encoding='latin1')  # You may need to try different encodings like 'latin1'

# Fill NaN values in the review column with an empty string
data['review'].fillna('', inplace=True)

# Extract independent variable (reviews)
reviews = data['review']

# Apply TF-IDF Vectorization to convert text data to numerical features
vectorizer = TfidfVectorizer(max_features=1000)  # You can adjust max_features as per your dataset size
X = vectorizer.fit_transform(reviews)

# Apply PCA
pca = PCA(n_components=2)  # You can change the number of components as per requirement
principal_components = pca.fit_transform(X.toarray())

# Create a new DataFrame for the transformed data
new_data = pd.DataFrame(data=principal_components, columns=['PC1', 'PC2'])
new_data['review'] = reviews

# Save the new dataset to a CSV file
new_data.to_csv('new_dataset_pca.csv', index=False)
