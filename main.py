from fastapi import FastAPI
from shorts_view_booster import index as shorts_view_booster

app = FastAPI()


@app.post("/boost_shorts_views")
def boost_shorts_views(list_search_key_string: str, video_key: str, number_of_runs: int):
    list_search_key = list_search_key_string.split(',')
    shorts_view_booster.boost_view(list_search_key, video_key, number_of_runs)
