import rclpy
from rclpy.node import Node
from person_msgs.srv import Query

def cb(request, response):
    if request.name == "小林壮馬":
        response.age = 20
    else:
        response.age = 255

    return response

<<<<<<< HEAD
rclpy.init()
node = Node("talker")
srv = node.create_service(Query, "query", cb)
rclpy.spin(node)
=======
class Talker():
    def __init__(self, nh):
        self.pub = nh.create_publisher(Int16, "countup", 10)
        self.n = 0
        nh.create_timer(0.5, self.cb)

    def cb(self):
        msg = Int16()
        msg.data = self.n
        self.pub.publish(msg)
        self.n += 1

def main():    
    rclpy.init()
    node = Node("talker")
    talker = Talker(node)
    rclpy.spin(node)
>>>>>>> lesson10
