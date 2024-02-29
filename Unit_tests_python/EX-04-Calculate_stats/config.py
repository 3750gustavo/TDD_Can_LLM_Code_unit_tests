# config.py
from ChatGPT import calculate_stats as ChatGPT
from CodeLLama import calculate_stats as CodeLLama
from Copilot import calculate_stats as Copilot
from Bard import calculate_stats as Bard
from Claude import calculate_stats as Claude
from Perplexity import calculate_stats as Perplexity

implementations = [
    (ChatGPT, 'ChatGPT'),
    (CodeLLama, 'CodeLLama'),
    (Copilot, 'Copilot'),
    (Bard, 'Bard'),
    (Claude, 'Claude'),
    (Perplexity, 'Perplexity')
]

list1 = [10,9,11,10,8,12,11,9,10,11] # Low variation
list2 = [3,9,11,10,8,12,11,9,10,23] # With anomalies
list3 = [1,19,9,5,2,18,13,7,4,6] # High variation

def get_implementations():
    return implementations

def get_lists():
    return list1, list2, list3