# This is a sample Python script to communication via websocket with scale Pue5.

from RdgWebSocket import RdgWebSocket

websocket = RdgWebSocket()


def switch(ws_element):
    option = int(input("----------------------"
                       "\nSelect your option: "
                       "\n1. Get mod info"
                       "\n2. Change platform"
                       "\n3. Taring scale"
                       "\n4. Zeroing scale\n"))

    if option == 1:
        websocket.get_mod_info(ws_element)
        switch(ws_element)

    elif option == 2:
        websocket.change_platform(ws_element)
        switch(ws_element)

    elif option == 3:
        websocket.taring_scale(ws_element)
        switch(ws_element)

    elif option == 4:
        websocket.zeroing_scale(ws_element)
        switch(ws_element)

    else:
        print("Incorrect option")


if __name__ == '__main__':
    ws = websocket.connect(str(input("Enter ip address: ")))
    websocket.register_listner(ws)
    switch(ws)
