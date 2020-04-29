import webget
class NotFoundException(ValueError):
    def __init__(self, *args, **kwargs):
        ValueError.__init__(self, *args, **kwargs)

class Downloader():
    def __init__(self,url_list):
        self.url_list = url_list
    def download(self,url,filename):
        try:
            webget.download(ulr, filename)
        except:
            raise NotFoundException('404 Not found')
    def multi_download(self):
        