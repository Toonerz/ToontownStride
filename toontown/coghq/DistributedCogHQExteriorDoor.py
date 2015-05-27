from direct.interval.IntervalGlobal import *
from direct.distributed.ClockDelta import *
from toontown.toonbase import ToontownGlobals
from direct.directnotify import DirectNotifyGlobal
from direct.fsm import ClassicFSM
import DistributedCogHQDoor
from toontown.hood import ZoneUtil
from BossLobbyGui import BossLobbyGui

class DistributedCogHQExteriorDoor(DistributedCogHQDoor.DistributedCogHQDoor):

    def __init__(self, cr):
        DistributedCogHQDoor.DistributedCogHQDoor.__init__(self, cr)

    def selectLobby(self, avId):
        self.lobbyGui = BossLobbyGui(self.sendConfirmation, avId)

    def sendConfirmation(self, avId, status):
        self.lobbyGui.destroy()
        del self.lobbyGui
        self.sendUpdate('confirmEntrance', [avId, status])
