#!/usr/bin/python3

def scrapper(query,mode, paths ,nb_imgs = 15, motor = "Google", mobile = False, weight = 200, height = 100) :

    """
    query : Your word to search /n
    mode : content / img / * is for dev
    path : for img
    
    motor : default is google
    mobile : default is false
    weight : weight approx desired google only 
    height : height approx desired google only

    """
    print("BEGIN")

    #module    
    import requests
    from bs4 import BeautifulSoup
    import wget 
    import os

    # path
    if mode == "IMG" :
        path = paths + "/"
    
    # required for search
    requete = query.replace(" ", "+")

    # Motor selection
    if motor.upper() == "GOOGLE" :
        if mode.upper() == "CONTENT" :
            URL = f"https://google.com/search?q={requete}"
        else :#img
            URL = "https://www.google.com/search?q=" + requete 
            URL = URL + "&sxsrf=ALeKk00fRPM3Wz-svHb3PwWOPo9pVZHadg:1610377394983"                        # recherche img unknow
            URL = URL + "&source=lnms&tbm=isch&sa=X&ved=2ahUKEwiP1NOkk5TuAhWGy4UKHUjSDFcQ_AUoA3oECAkQBQ" # recherche img unknow
            URL = URL + "&biw={weight} &bih={height} ".format(weight = weight , height = height)         # format img
    else :
        pass #later

    print(URL)

    # Desktop or Mobile || Firefox
    if mobile is False : 
        USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
    else : 
        USER_AGENT = "Mozilla/5.0 (Linux; Android 7.0; SM-G930V Build/NRD90M) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.125 Mobile Safari/537.36"

    print(" INTERMEDIATE ")
    if mode.upper() == "IMG"  :
    # Return
        limite = 50
        nb_img = 1
        history = []
        print(" INTERMEDIATE 2")
        while nb_img < limite :
            header = {"user-agent" : USER_AGENT}
            responce = requests.get(url = URL,headers = header)
            soup = BeautifulSoup(responce.content, "html.parser")   

            for result in soup.find_all('img'):

                if nb_img < limite : 
                        pictures = result.get('data-src')
                        print(pictures)
                        if pictures is None :
                            print("Passing empty file")
                        else :
                            if pictures in history :
                                print("déja dans le dossier")
                            else : 
                                print("downloading : {pictures}" .format(pictures = pictures ) )
                                file_name = wget.download(pictures, path + query+str(nb_img))
                                nb_img = nb_img + 1
                                history.append(pictures)
    
    print('done')

scrapper("Couvert sale",mode = "IMG",paths = "plastique")