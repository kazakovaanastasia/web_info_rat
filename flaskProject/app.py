from flask import Flask, render_template
from request import *
app = Flask(__name__)


@app.route('/')
def hello_world():
    url="http://ratmania.ru/forum/index.php?board=50.0"
    http=[]
    urls=get_urls(url)
    for i in urls:
        http.append(i)


    array=analise_more(http)
    av=page_info(array)

    return render_template("table.html",out=array,av=av)


if __name__ == '__main__':
    app.run()
