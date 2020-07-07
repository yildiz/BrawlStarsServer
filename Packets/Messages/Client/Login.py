from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Players
from Packets.Messages.Server.LoginOk import LoginOk
from Utils.reader import CoCMessageReader
from database.player import DataBase

class Login(CoCMessageReader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.db = DataBase()

    def decode(self):
        self.player.HighID = self.read_int()
        self.player.LowID = self.read_int()
        self.player.Token = self.read_string()
        self.major = self.read_int()
        self.minor = self.read_int()
        self.build = self.read_int()

    def process(self):
        self.player.LowID = 1
        self.player.HighID = 0
        self.player.Token = "None"
        if self.player.LowID is not None:
            LoginOk(self.client, self.player).send()