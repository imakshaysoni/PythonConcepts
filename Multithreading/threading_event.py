import threadingimport requestsevent = threading.Event()import timefile_name = 'downloaded_file.txt'def download_file_in_chunk():    url = "https://facebook.com/"    url = 'https://jsonplaceholder.typicode.com/posts/1/comments'    print("Downloading file")    iter = requests.get(url, stream=True)    with open(file_name, 'wb') as file:        for chunk in iter.iter_content(chunk_size=10):                file.write(chunk)    print("File Downloaded")    time.sleep(0.14)    event.set()def word_count():    print("Counting word count for downloaded file")    while not event.isSet():        print("File is still downloading... waiting to finish")        event.wait()    with open(file_name, 'r') as file:        words = file.read()        print(words)        word_freq = getCount(words)        print(f"Frequency of each word present in file; {word_freq}")def getCount(words):    freq = {}    words_list = words.split()    for ch in words_list:        if ch in freq.keys():            freq[ch] += 1        else:            freq[ch] = 1    return freqt1 = threading.Thread(target=download_file_in_chunk)t2 = threading.Thread(target=word_count)t1.start()t2.start()t1.join()t2.join()