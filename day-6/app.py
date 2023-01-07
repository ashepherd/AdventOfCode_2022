
"""
https://adventofcode.com/2022/day/6
"""

class Device:
    def __init__(self, msg):
        self.message = msg

    def detect_start_of_packet(self, detector=4):
        index = None
        size = len(self.message)
        for index in range(0, size):
            chunk = self.message[index:index+detector]
            dupe = False
            for c in chunk:
                if chunk.count(c) > 1:
                    dupe = True
                    break
            if False == dupe:
                print(chunk)
                return index + detector
        return None


test = Device('mjqjpqmgbljsphdztnvjfqwrcgsmlb')
print(4, test.detect_start_of_packet(detector=4))
print(14, test.detect_start_of_packet(detector=14))

test = Device('bvwbjplbgvbhsrlpgdmjqwftvncz')
print(4, test.detect_start_of_packet(detector=4))
print(14, test.detect_start_of_packet(detector=14))

test = Device('nppdvjthqldpwncqszvftbrmjlhg')
print(4, test.detect_start_of_packet(detector=4))
print(14, test.detect_start_of_packet(detector=14))

test = Device('nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg')
print(4, test.detect_start_of_packet(detector=4))
print(14, test.detect_start_of_packet(detector=14))

test = Device('zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw')
print(4, test.detect_start_of_packet(detector=4))
print(14, test.detect_start_of_packet(detector=14))

file = open('input', 'r')
lines = file.readlines()

for line in lines:
    test = Device(line.strip())
    print(4, test.detect_start_of_packet(detector=4))
    print(14, test.detect_start_of_packet(detector=14))