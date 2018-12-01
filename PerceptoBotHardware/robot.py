from gpiozero import Robot
import pyrebase

robot = Robot(left=(9,10), right=(7,8))

direction = True

config = {
    'apiKey': "AIzaSyD4_3GgD07jSsugc5Tht33Xsz_PisX4VuQ",
    'authDomain': "perceptobot.firebaseapp.com",
    'databaseURL': "https://perceptobot.firebaseio.com",
    'projectId': "perceptobot",
    'storageBucket': "perceptobot.appspot.com",
    'messagingSenderId': "766339239713"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()


def linear_handler(message):
    if (db.child("direction").get().val()):
        robot.forward(message['data'])
    else:
        robot.backward(message['data'])


def lateral_handler(message):
    if (message['data'] < -1):
        robot.left()
    elif (message['data'] > 1):
        robot.right()
    else:
        robot.stop()


linear_stream = db.child("linearAcc").stream(linear_handler)
lateral_stream = db.child("lateralAcc").stream(lateral_handler)