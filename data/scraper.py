import requests
from bs4 import BeautifulSoup
import sys
sys.setrecursionlimit(10000)
URL = 'https://imsdb.com/all-scripts.html'
page = requests.get(URL)
soup = BeautifulSoup(page.content, "html.parser")
results = soup.find(id="mainbody")

movie_info = results.find_all("p")
total_distinct_tokens = set()
dataset = open("dataset.txt", "w+")
count = 0
for movie in movie_info:
    count += 1
    output_string = '<BOS>'
    
    movie = str(movie)
    title_idx = movie.find("title")
    
    start_idx = title_idx + len("title") + 2
    end_idx = movie.find(">", start_idx) - 1
    title = movie[start_idx:end_idx]
    title_words = title.split(" ")
    
    url_string = 'https://imsdb.com/Movie%20Scripts/'
    for i in range(len(title_words)-1):
        url_string += title_words[i] + "%20"
    url_string += "Script.html"
    
    movie_info_page = requests.get(url_string)
    movie_soup = BeautifulSoup(movie_info_page.content, "html.parser")
    results = movie_soup.find(id="mainbody")
    if (results is None):
        count -= 1
        continue
    script_info = results.find("table", class_="script-details")
    if (script_info is None):
        count -= 1
        continue
    script_details = script_info.find_all("a")
    if (script_details is None):
        count -= 1
        continue
    tokens = []
    script_details = [str(s) for s in script_details]
   
    # Get writer and genre tokens
    for j in range(len(script_details)):
        script_detail = script_details[j]
        start_idx_init = script_detail.find("w=") 
        start_idx = start_idx_init + 2
        if (start_idx_init == -1):
            start_idx_init = script_detail.find("genre/")
            start_idx = start_idx_init + len("genre/")
            if (start_idx_init == -1):
                break
            
        end_idx = script_detail.find('"', start_idx)
     
        token = "<" + script_detail[start_idx:end_idx] + ">"
        tokens.append(token)
        total_distinct_tokens.add(token)
    
    for token in tokens:
        output_string += token
    
    script_url = 'https://imsdb.com/scripts/'
    for k in range(len(title_words)-2):
        script_url += title_words[k] + "-"
    script_url += title_words[len(title_words)-2] + ".html"
    
    print(script_url)
    screenplay_page = requests.get(script_url)
    screenplay_soup = BeautifulSoup(screenplay_page.content, "html.parser")
    
    screenplay_results = screenplay_soup.find(id="mainbody")
 
    if (screenplay_results is None or len(str(screenplay_results)) == 0):
        count -= 1
        continue
    screenplay = screenplay_results.find_all("pre")
    if (screenplay is None or len(screenplay) == 0):
        count -= 1
        continue
    screenplay = str(screenplay[0])

    output_string += screenplay + "<EOS>"
    dataset.write(output_string + "\n")
    print("wrote movie " + str(count))
    

dataset.close()

# Write all distinct genres and writers to special tokens file
special_tokens = open("special-tokens.txt", "w+")
for token in total_distinct_tokens:
    special_tokens.write(token + "\n")
special_tokens.close()

    
