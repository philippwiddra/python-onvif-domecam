from MegapixelDomeCamera import MegapixelDomeCamera

camera = MegapixelDomeCamera("192.168.178.99", user = "Philipp", password = "Johannes")
# print(camera.getRotationStatus())
camera.moveToPositionPreset("1")