import urllib
import requests

def book_to_words(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    booktxt = urllib.request.urlopen(book_url).read().decode()
    bookascii = booktxt.encode('ascii','replace')
    return bookascii.split()

def radix_a_book(book_url='https://www.gutenberg.org/files/84/84-0.txt'):
    words = book_to_words()
    
    longest = len(words[0])
    for i in range(len(words)):
        if len(words[i]) > longest:
            longest = len(words[i])
    
    for i in range(len(words)):
        words[i] += '\0'.encode('ascii', 'replace') * (longest - len(words[i]))

    for i in range(longest - 1, -1, -1):
        words = counting_sort(words, i)
    
    for i in range(len(words)):
        words[i] = words[i].decode('ascii').replace('\x00', '')
        words[i] = bytes(words[i], encoding='ascii')

    # print(words)
    return words
    
def counting_sort(lst, index):
    count = [0] * 127
    output = [0] * len(lst)

    for word in lst:
        count[word[index]] += 1

    for i in range(1, len(count)):
        count[i] += count[i - 1]
    
    for i in range(len(lst) - 1, -1, -1):
        idx = lst[i][index]
        output[count[idx] - 1] = lst[i]
        count[idx] -= 1
    
    for i in range(0, len(lst)):
        lst[i] = output[i]
    
    return lst