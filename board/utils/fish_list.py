import requests

def get_fish_list():
    headers = {"X-API-KEY": "3102fefa-0819-4322-a697-abc0791c72d3", "Accept-Version": "1.0.0"}
    params = {"month": "current"}
    response = requests.get("https://api.nookipedia.com/nh/fish", headers=headers, params=params)
    if response.status_code == 200:
        fish_list = []
        for fish in response.json():
            if "location" not in fish:
                continue
            fish_dict = {
                "url": fish.get("url"),
                "name": fish.get("name"),
                "image_url": fish.get("image_url"),
                "render_url": fish.get("render_url"),
                "location": fish.get("location"),
                "shadow_size": fish.get("shadow_size"),
                "rarity": fish.get("rarity"),
                "north": fish.get("north"),
                "south": fish.get("south"),
            }
            fish_list.append(fish_dict)

        fish_list.sort(key=lambda x: x['name'])
        return fish_list[:10] # 최대 10개의 물고기 정보 반환
    else:
        print(response.json())  # response의 내용을 출력
        return None
