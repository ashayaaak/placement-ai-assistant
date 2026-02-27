import os
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

KB_PATH = "knowledge_base"

def load_documents():
    docs = []
    for file in os.listdir(KB_PATH):
        with open(os.path.join(KB_PATH, file), "r", encoding="utf-8") as f:
            docs.append(f.read())
    return docs

documents = load_documents()
vectorizer = TfidfVectorizer()
doc_vectors = vectorizer.fit_transform(documents)

def get_context(query):
    query_vec = vectorizer.transform([query])
    similarities = cosine_similarity(query_vec, doc_vectors)
    best_doc_index = similarities.argmax()
    return documents[best_doc_index]