class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "6524770736"
    sudo_users = "5147296244", "1722114839"
    GROUP_ID = -1002141862465
    TOKEN = "7700642994:AAEBpbBwpeS59LYSCKsf2wRTsTJmsM49jIs"
    mongo_url = "mongodb+srv://HaremDBBot:ThisIsPasswordForHaremDB@haremdb.swzjngj.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/b925c3985f0f325e62e17.jpg", "https://telegra.ph/file/4211fb191383d895dab9d.jpg"]
    SUPPORT_CHAT = "GODL_FC"
    UPDATE_CHAT = "GODL_FC"
    BOT_USERNAME = "@CollectCricketBot"
    CHARA_CHANNEL_ID = "-1002285622749"
    api_id = 26626068
    api_hash = "bf423698bcbe33cfd58b11c78c42caa2"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
