from datetime import datetime
import re
import os

def main():
    print("====================================")
    print(" ✏ post writer by outstandingboy")
    print("====================================")
    today = datetime.today()

    category = input("category: ")
    while category == "":
        category = input("category: ")

    datePattern = re.compile('[0-9]{4}-[0-9]{2}-[0-9]{2}')
    date = "%04d-%02d-%02d"%(today.year, today.month, today.day)
    _date = input("date (default: %s): "%date)

    while not (_date == "" or datePattern.match(_date)):
        _date = input("date (default: %s): "%date)

    if _date != "":
        date = _date

    filename = input("filename: ")
    while filename == "":
        filename = input("filename: ")

    filename = filename.replace(" ", "-")
    if filename.endswith(".md"):
        filename = filename[0:-3]

    print("%s/%s-%s.md"%(category, date, filename))

    postDir = "_posts/%s"%(category)
    postPath = "_posts/%s/%s-%s.md"%(category, date, filename)
    imgPath = "imgs/%s/%s-%s"%(category, date, filename)

    os.makedirs(postDir, exist_ok=True)
    post = open(postPath, "w")
    post.write("---\n")
    post.write('layout: post\n')
    post.write('title: "TITLE"\n')
    post.write('summary: "SUMMARY"\n')
    post.write('thumbnail: "https://media.giphy.com/media/xU9TT471DTGJq/giphy.gif"\n')
    post.write("category: %s\n"%category)
    post.write("tags: []\n")
    post.write("comments: true\n")
    post.write("---\n")
    post.write("<!-- ![이미지](https://github.com/outstanding1301/outstanding1301.github.io/blob/master/%s/이미지파일?raw=true) -->\n"%(imgPath))
    post.close()
    print("[📄] create file %s"%postPath)

    os.makedirs(imgPath, exist_ok=True)
    print("[📂] create directory %s"%imgPath)

    print("[😏] Done")

if __name__ == "__main__":
    main()