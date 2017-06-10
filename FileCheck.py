import urllib.request
import urllib.parse


def read_file():
    file=open('/Users/snehabhi/Downloads/movie_quotes.txt')
    file_txt=file.read()
    file.close()
    check_profanity(file_txt)

def check_profanity(chk_text):
    chk=urllib.parse.quote(chk_text)
    url=urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+chk)
    resp=url.read()
    if b'true' in resp:
        print("****************************************************")
        print("Profanity Aler!! Restricted Word present in the file")
        print("****************************************************")
    elif b'false' in resp:
        print("***************************************************")
        print("File is clear!! No restricted words in the document")
        print("***************************************************")
    else:
        print("***************************")
        print("Could not read the document")
        print("***************************")
    url.close()

read_file()
