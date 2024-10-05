import nltk
from collections import defaultdict
from sklearn.feature_extraction.text import TfidfVectorizer

# Downloads the Punkt model
nltk.download('punkt')

# TextRank-based summarization
def sentence_similarity(sent1, sent2):
    words1 = set(sent1.split())
    words2 = set(sent2.split())
    return len(words1.intersection(words2)) / ((len(words1) + len(words2)) / 2)

def build_similarity_matrix(sentences):
    matrix = [[0 for _ in range(len(sentences))] for _ in range(len(sentences))]
    for i, sent1 in enumerate(sentences):
        for j, sent2 in enumerate(sentences):
            if i != j:
                matrix[i][j] = sentence_similarity(sent1, sent2)
    return matrix

def text_rank_summary(text, num_sentences=5):
    """
    Summarize the text using TextRank.
    """
    sentences = nltk.sent_tokenize(text)
    matrix = build_similarity_matrix(sentences)
    sentence_ranks = [sum(matrix[i]) for i in range(len(sentences))]
    ranked_sentences = sorted(((sentence_ranks[i], s) for i, s in enumerate(sentences)), reverse=True)
    summary = ' '.join([ranked_sentences[i][1] for i in range(min(num_sentences, len(ranked_sentences)))])
    return summary

# TF-IDF-based keyword extraction
def extract_keywords(text, num_keywords=10):
    """
    Extracts top TF-IDF keywords from the document.
    """
    vectorizer = TfidfVectorizer(max_features=num_keywords, stop_words='english', ngram_range=(1, 2))
    X = vectorizer.fit_transform([text])
    return vectorizer.get_feature_names_out().tolist()
