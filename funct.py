import math

def getDirectionRadians(self, hand) -> float:
        """Get the direction of the vector formed by the joystick and its
        origin in radians.

        :returns: The direction of the vector in radians
        """
        return math.atan2(self.getX(hand), -self.getY(hand))


def getDirectionDegrees(self, hand) -> float:
    """Get the direction of the vector formed by the joystick and its
    origin in degrees.

    :returns: The direction of the vector in degrees
    """
    return math.degrees(self.getDirectionRadians(hand))