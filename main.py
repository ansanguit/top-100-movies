import requests
from bs4 import BeautifulSoup

WEB_FILE= "moviedata.html"
def read_web_file():
    try:
        open(WEB_FILE)
    except FileNotFoundError:
        print("You need to save the rendered htlm")
        exit()
    finally:
        with open(WEB_FILE, mode="r", encoding="utf-8") as fp:
            content= fp.read()
        soup= BeautifulSoup(content,"html.parser")
        movies = soup.find_all(name="h3", class_="jsx-4245974604")
        movies_titles= [movie.getText() for movie in movies]
        return movies_titles

result = read_web_file()
print(result)

# reverse the order

ordered_list= result[::-1]
print(ordered_list)

# or

# for i in range(len(result)-1, -1,-1):
#     ordered_list= result[i]
#     print(ordered_list)

with open("movies.txt", mode="w") as file:
     for movie in ordered_list:
          file.write(f"{movie}\n")
