#!/usr/bin/python
#-*-coding=utf-8

# pip install onvif_zeep

import zeep
from onvif import ONVIFCamera, ONVIFService, ONVIFError

def zeep_pythonvalue(self, xmlvalue):
    return xmlvalue

zeep.xsd.simple.AnySimpleType.pythonvalue = zeep_pythonvalue


class MegapixelDomeCamera:
    def __init__(self, host, port = 8999, user = "Admin", password = "admin"):
        self.__camera = ONVIFCamera(host, port, user, password, "wsdl/")
        self.__mediaService = self.__camera.create_media_service()
        self.__ptzService = self.__camera.create_ptz_service()
        self.__mediaProfileToken = self.__mediaService.GetProfiles()[0].token
        self.__ptzNodeToken = self.__ptzService.GetNodes()[0].token

    def getSnapshot(self):
        response = self.__mediaService.GetSnapshotUri(self.__mediaProfileToken)
        return response.Uri

    def getRotationStatus(self):
        return self.__ptzService.GetStatus(self.__mediaProfileToken)

    # def move(self):
    #     vector = 10
    #     speed = 5
    #     return self.__ptzService.RelativeMove(self.__mediaProfileToken, vector)

    def getPositionPresets(self):
        return self.__ptzService.GetPresets(self.__mediaProfileToken)

    def moveToPositionPreset(self, presetToken):
        p = self.__ptzService.create_type("GotoPreset")
        p.ProfileToken = self.__mediaProfileToken
        p.PresetToken = presetToken

        self.__ptzService.GotoPreset(p)