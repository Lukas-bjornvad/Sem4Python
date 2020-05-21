import webget
from concurrent.futures import ThreadPoolExecutor
class NotFoundException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

class Downloader():
    def __init__(self,urls):
        self.urls = urls
    def download(self, url):
        try:
            webget.download(url, "cheese")
        except:
            raise NotFoundException('404 Not found')

    def multi_download(self, urls):
        def getter(lister):
            for item in lister: 
                name = item.split("/")[-1]
                print(name)
                try:
                    self.download(item)
                except:
                    print('Exception occured')
        
        def multithreading(func, args, workers=5):
            with ThreadPoolExecutor(workers) as ex:
                res = ex.map(func(args))
                return res
        multithreading(getter, urls)
   
    def __iter__(self):
        self.pos = 0
        return self
    def __next__(self):
        lis = self.urls
        p = self.pos
        if p >= len(lis):
            raise StopIteration
        else:
            self.pos += 1
        return lis[self.pos]

    def urllist_generator(self):
        num = 0
        while num <= self.urls:
            yield self.urls[num]
            num += 1

    def avg_vowels(self, text):
        def isVowel(ch): 
            return ch.upper() in ['A', 'E', 'I', 'O', 'U'] 
  
    # Returns count of vowels in str  
        def countVowels(str): 
            count = 0
            for i in range(len(str)): 
  
             # Check for vowel 
                if isVowel(str[i]): 
                    count += 1
            return count 
        return countVowels(text)
    #print(avg_vowels("Hello Human"))
    def getfiles(self):
        files= self.urls
        count = 0
        for fil in self.urls:
            files[count] = fil.split("/")[-1]
            count +=1
        return files

    def hardest_read(self):
        dic = {}
        files = self.getfiles()
        for fil in files:
            print(fil)
            f = open(fil, encoding="utf8")
            text = f.read()
            dic[fil] = self.avg_vowels(text)
        return max(dic)

    


