class Baseconfig(object):
    SUPPORT_EMAIL="support@bookworm.com"
    # connecting to my database
SQLALCHEMY_DATABASE_URI="mysql+mysqlconnector://root@127.0.0.1/personalweb"


# Useful when we are programming
class Liveconfig(Baseconfig):
    API_URL="http//test.com"

class Testcpnfig(Baseconfig):
    API_URL = "http://live.com"