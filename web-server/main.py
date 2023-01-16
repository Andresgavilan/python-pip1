import store
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()

@app.get('/')
def get_list():
    return [1, 2, 3, 4,]

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """ 
        <h1> This is a sample of web servidor</h1>
        <p>this is a paragrph</p>
    """

def run():
    store.get_categories()

if __name__ == '__main__':
    run()
