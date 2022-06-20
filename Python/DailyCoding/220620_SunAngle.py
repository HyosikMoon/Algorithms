from typing import Union

def sun_angle(time: str) -> Union[int, str]:
    # 0.25 degrees per min
    angle = 0
    angle = (int(time[:2]) - 6)*60*0.25 + int(time[3:])*0.25
    if angle > 180 or (int(time[:2]) - 6 < 0): return "I don't see the sun!"
    return angle
