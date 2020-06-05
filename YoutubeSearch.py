api_key = "KSNAKFKANKKKVIFNWodgkj_sN-xyiNy0Vrq4YeY" #Please input your own API key here
import webbrowser
from apiclient.discovery import build
#setting up to access youtube through its API
youtube = build('youtube', 'v3' , developerKey=api_key)


def main():
    #variables needed to loop the following questions below
    ys_continue = True
    while ys_continue:
        content_check = True
        view_on = True
        ask_on = True
        
        #First question
        while content_check:
            content_type = input("Are you looking for [V]ideos or [C]hannels?")
            if content_type.lower() == "v" or content_type.lower() == "c":
                content_check = False
                
        #Second question if user wants videos
        if content_type == "v":
            query = input("What are you searching for?")
            req = youtube.search().list(q=query , part='snippet', type="video", maxResults=10)
            res = req.execute()
            for i in range(0,len(res['items'])):
                print(i+1,". ",res['items'][i]['snippet']['title'])
            while view_on:
                
                #Third question
                view = int(input("Which one would you be interested in? [1-10]"))
                yt_website = "https://www.youtube.com/watch?v="+res['items'][view-1]['id']['videoId']
                webbrowser.open_new_tab(yt_website)
                
                #Ask user if user wants to repeat
                while ask_on:
                    repeat = input("Continue? [Y] or [N]")
                    if repeat.lower() == ("y"):
                        view_on = False
                        ask_on = False
                    elif repeat.lower() == ("n"):
                        view_on = False
                        ask_on = False
                        ys_continue = False

        #Second question if user wants channels
        elif content_type == "c":
            query = input("What are you searching for?")
            req = youtube.search().list(q=query , part='snippet', type="channel", maxResults=10)
            res = req.execute()
            for i in range(0,len(res['items'])):
                print(i+1,". ",res['items'][i]['snippet']['channelTitle'])
                
            #Third question
            while view_on:
                view = int(input("Which one would you be interested in? [1-10]"))
                yt_website = "https://www.youtube.com/channel/"+res['items'][view-1]['id']['channelId']
                webbrowser.open_new_tab(yt_website)
                
                #Ask user if user wants to repeat
                while ask_on:
                    repeat = input("Continue? [Y] or [N]")
                    if repeat.lower() == ("y"):
                        view_on = False
                        ask_on = False
                    elif repeat.lower() == ("n"):
                        view_on = False
                        ask_on = False
                        ys_continue = False

if __name__ == "__main__":
    main()
