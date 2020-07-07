import time

from Utils.Writer import Writer


class LoginOk(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104

    def encode(self):
        timeStamp = str(round(time.time()))

        self.writeInt(0)
        self.writeInt(self.player.LowID)
        # HighID, lowID
        self.writeInt(0)
        self.writeInt(self.player.LowID)
        # HighID, lowID
        self.writeString(self.player.Token)  # Token

        self.writeString()
        self.writeString()

        self.writeInt(24)  # MajorVersion
        self.writeInt(152)  # Build
        self.writeInt(1)  # MinorVersion

        self.writeString("dev")  # Environment

        self.writeInt(2)  # SessionCount
        self.writeInt(172)  # PlayTimeSeconds
        self.writeInt(0)  # DaySinceStartedPlaying

        self.writeString("")  # FacebookAppId
        self.writeString(timeStamp)  # ServerTime
        self.writeString("")  # AccountCreatedDate

        self.writeInt(4294967295)

        self.writeString("UA")  # City
        self.writeString()  # City

        self.writeInt(1)
        self.writeString()  # LocalRegion
        
        self.writeInt(2)

        self.writeString("https://game-assets.brawlstarsgame.com")  # Url Game Assets
        self.writeString("http://a678dbc1c015a893c9fd-4e8cc3b1ad3a3c940c504815caefa967.r87.cf2.rackcdn.com")  # Url cdn

        self.writeInt(1)

        self.writeString("https://event-assets.brawlstars.com")  # Url event assets
