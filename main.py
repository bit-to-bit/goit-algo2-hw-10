import string
import requests
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
import matplotlib.pyplot as plt

def get_text(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text

def remove_punctuation(text):
    return text.translate(str.maketrans("", "", string.punctuation))

def map_function(words_chunk):
    return [(word, 1) for word in words_chunk]

def shuffle_function(mapped_values):
    shuffled = defaultdict(list)
    for key, value in mapped_values:
        shuffled[key].append(value)
    return shuffled.items()

def reduce_function(key_values):
    key, values = key_values
    return key, sum(values)

def map_reduce(text, num_workers=4):
    text = remove_punctuation(text).lower()
    words = text.split()
    
    chunk_size = max(1, len(words) // num_workers)
    chunks = [words[i:i + chunk_size] for i in range(0, len(words), chunk_size)]
    
    mapped_values = []
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        results = executor.map(map_function, chunks)
        for result in results:
            mapped_values.extend(result)
            
    shuffled_values = shuffle_function(mapped_values)
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        reduced_values = list(executor.map(reduce_function, shuffled_values))
        
    return dict(reduced_values)

def visualize_top_words(word_counts, top_n=10):
    sorted_word_counts = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)[:top_n]
    
    words = [item[0] for item in sorted_word_counts]
    counts = [item[1] for item in sorted_word_counts]
    
    plt.figure(figsize=(10, 6))
    plt.barh(words[::-1], counts[::-1], color='skyblue')
    plt.xlabel('Frequency')
    plt.ylabel('Words')
    plt.title(f'Top {top_n} Most Frequent Words')
    plt.tight_layout()
    plt.show()

if __name__ == '__main__':
    url = "https://gutenberg.net.au/ebooks01/0100021.txt"
    try:
        text = get_text(url)
        word_counts = map_reduce(text)
        visualize_top_words(word_counts, top_n=10)
    except Exception as e:
        print(f"Error: {e}")
