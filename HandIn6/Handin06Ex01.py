from Download import Downloader
url_list = ["https://www.gutenberg.org/files/1342/1342-0.txt", "https://www.gutenberg.org/files/11/11-0.txt", "https://www.gutenberg.org/files/84/84-0.txt"]

down = Downloader(url_list)
#down.multi_download(url_list)
hard = down.hardest_read()
print(hard)