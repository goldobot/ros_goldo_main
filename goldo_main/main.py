import rospy
from std_msgs.msg import String
import goldo_msgs.msg


from enum import Enum

class MatchState(Enum):
    Idle=0
    PreMatch=1
    WaitForStartOfMatch=2
    Match=3
    PostMatch=4
    Debug=5


class Main:
    def __init__(self):
        self.pub_match_state = rospy.Publisher('match_state', goldo_msgs.msg.MatchState, queue_size=10, latch=True)
        self.pub_markers = rospy.Publisher('markers', goldo_msgs.msg.Markers, queue_size=10, latch=True)
        self.match_state = MatchState.Idle