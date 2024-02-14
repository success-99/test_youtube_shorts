import requests
import json

# link2 = "https://youtu.be/vJ7wIAGUl5U?si=a4GVY3nrHf77W9JR"
link2 = 'https://youtube.com/shorts/IoaQTkQSs6c?si=74GaLRvmrSrKBL3z'

def dow_ysh(link):
    link1 = link[27:][:11]

    url = "https://yt-api.p.rapidapi.com/dl"

    querystring = {"id": f"{link1}"}

    headers = {
        "X-RapidAPI-Key": "62b08e04d2mshcf4c456c3bc52ddp16b155jsn5e168e916348",
        "X-RapidAPI-Host": "yt-api.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    natija = json.loads(response.text)
    title = natija['title'][:5]
    itag_22_url = None
    itag_18_url = None
    for video_format in natija.get("formats", []):
        if video_format.get("itag") == 22:
            itag_22_url = video_format.get("url")
        elif video_format.get("itag") == 18:
            itag_18_url = video_format.get("url")

    # Agar itag 22 bo'lmasa, itag 18 bo'lgan urlni olish
    selected_url = itag_22_url if itag_22_url else itag_18_url
    return selected_url,title



# result = dow_ysh(link2)
# print(result)














# import requests
#
# url = "https://yt-api.p.rapidapi.com/dl"
#
# querystring = {"id":"Jf71ErL8Kmo"}
#
# headers = {
# 	"X-RapidAPI-Key": "62b08e04d2mshcf4c456c3bc52ddp16b155jsn5e168e916348",
# 	"X-RapidAPI-Host": "yt-api.p.rapidapi.com"
# }
#
# response = requests.get(url, headers=headers, params=querystring)
#
# print(response.json())

# #

def download_video(url, title):
    try:
        response = requests.get(url)
        content_type = response.headers.get('content-type')

        if 'video' in content_type:
            video_data = response.content
            with open(f"{title}.mp4", 'wb') as video_file:
                video_f = video_file.write(video_data)
            return video_f
        else:
            print("Manzil video turida emas.")

    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")


# Sizning berayotgan manzilni o'zgartiring
# video_url = "https://rr2---sn-5go7ynlk.googlevideo.com/videoplayback?expire=1707847856&ei=UFzLZaLtOdiyv_IPzaKAqAQ&ip=188.126.94.120&id=o-AGvSPXKJr7SK19leKxlbxW86u6S8CQOrOGieAcknFsD1&itag=22&source=youtube&requiressl=yes&xpc=EgVo2aDSNQ%3D%3D&mh=Xr&mm=31%2C29&mn=sn-5go7ynlk%2Csn-5goeenez&ms=au%2Crdu&mv=m&mvi=2&pl=23&initcwndbps=1760000&vprv=1&svpuc=1&mime=video%2Fmp4&cnr=14&ratebypass=yes&dur=38.754&lmt=1706365989495147&mt=1707825905&fvip=4&fexp=24007246&c=ANDROID&txp=5432434&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cxpc%2Cvprv%2Csvpuc%2Cmime%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AJfQdSswRQIgSnhkaghbumS3iW0THMM80SikW9A9qSmPDXRNbdZlojcCIQDk9RBV8biJvNwrlCQUgG2YdhwR6tQ7PrlOpAmWN0qfQw%3D%3D&lsparams=mh%2Cmm%2Cmn%2Cms%2Cmv%2Cmvi%2Cpl%2Cinitcwndbps&lsig=APTiJQcwRQIhAJXZEXT2ycN8q6tkbJBDSjq4NVvdazxE8r6fpaDhtMhWAiACUcZOxcVw8KQ4Cu2b9U7lAyo01gPq2AxF2-_VHj9m2A%3D%3D&title=Arnavut%20Ci%C4%9Feri%20Nas%C4%B1l%20Yap%C4%B1l%C4%B1r%3F%20Pamuk%20Gibi%20Arnavut%20Cig%CC%86eri%20%23cig%CC%86er%20%23arnavutcig%CC%86eri%20%20%23foodie%20%23yemek"
# download_video(url_v, title=t)
