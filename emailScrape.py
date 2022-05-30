import argparse
import requests 
from bs4 import BeautifulSoup 
import re
import pyfiglet



if __name__ =='__main__':
    title = "Email Scraper"
    ASCII_art = pyfiglet.figlet_format(title)
    print(ASCII_art)
    
    p = argparse.ArgumentParser()
    p.add_argument('-website', type=str, required=True)
    arg = p.parse_args()



    m = r"\w+\@\w+\.\w+"

    URL = arg.website.upper()

    page = requests.get(URL)


    def remove(html):
        soup = BeautifulSoup(html, "html.parser")
        for data in soup(['style', 'script']):
            data.decompose()

        return ''.join(soup.stripped_strings)


    it = re.findall(m, remove(page.content))
    if it:
        print("Links and Emails found: \n\n" + ','.join(it), '\n')

        print("Follow @LonerCode on GitHub :)")

    else:
        print("Not found")











