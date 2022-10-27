from tobrot.sample_config import Config
#Fill your all data, read readme for reference

class Config(Config):
    TG_BOT_TOKEN= "5492691108:AAFhFgRYgEkYu8NRf-SN93BNweWCGSXsGXQ"
    APP_ID = 12899143
    API_HASH = "0091bdc55aacee12b5b0ab73546df90c"
    OWNER_ID = 1963848011
    AUTH_CHANNEL = [-751911777]
    DESTINATION_FOLDER = "FDM-Shared Drive" #Name of your folder read readme(not id of the folder)
    RCLONE_CONFIG = """type = drive\nscope = drive\ntoken = {"access_token":"ya29.a0Aa4xrXOpv2ZrPjH53RwQ-6b4o1_QEVXX5Wj49fPq7xCwivqJ5Xdm0AHIsHNCIVqfy916lf_csZdwJ359i7ve4kqu9rQ-DOG8v5tVjLYGaDSMCOhTw_E9DE6IViJ_E8bO9CLUsxW-iOjOwF7JX3R1NbM9F3bkaCgYKATASARISFQEjDvL9eWIR47dv3a9LQWlsl4xV8g0163","token_type":"Bearer","refresh_token":"1//0gkDlidGyf_2tCgYIARAAGBASNwF-L9IrFrwQRx6IFnnQwKx8DgL7MDe9nobgxjK39VR1ZaI1kC-0BRI0lUsr4cEQp2c7xS1HrWo","expiry":"2022-10-27T15:43:02.1702463+06:00"}"""
    #fill taking reference of this config, dont remove """ from both side of the RCLONE_CONFIG variable 
    #FOR CUSTOM COMMANDS READ REAME AND FILL THEM...
