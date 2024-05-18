import random
from shorts_view_booster.action import ActionClass


def boost_view(list_search_key, video_key, number_of_runs):
    action = ActionClass()
    action.open_driver()

    try:
        for _ in range(number_of_runs):
            search_key = random.choice(list_search_key)
            action.search_video(search_key)

            if action.chose_video(video_key):
                action.watch_video()

                for _ in range(random.randint(1, 2)):
                    action.watch_next_video()

                if action.check_next_video_content(video_key):
                    action.watch_next_video()
            else:
                print('Can not find video')

            action.go_to_home_page()

    except Exception as e:
        print(e)
        action.close_driver()


# list_search_key = ['girl xinh douyin', 'the most beautiful girls on douyin',
#                    'beautiful girl douyin top 1', 'beautiful girl top 1', 'beautiful girl douyin', 'douyin top 1', 'douyin girl top 1', 'douyin girl top 1 2024', 'douyin girl top 1 new']

# boost_view(list_search_key, 'Top 1 Girl Xinh', 999)
