import json
"""
https://adventofcode.com/2022/day/7
"""

DISKSPACE = 70000000
UPDATE_SPACE = 30000000

class File:
    def __init__(self, size, name, parent_fullpath):
        self.parent = parent_fullpath
        self.size = size
        self.name = name


class Directory:
    def __init__(self, name, fullpath, parent_fullpath):
        self.parent = parent_fullpath
        self.name = name
        self.fullpath = fullpath
        self.files = {}
        self.directories = []
        self.size = None

    def add_file(self, file, fullpath):
        self.files[fullpath] = file

    def add_directory(self, fullpath):
        self.directories.append(fullpath)

    def compute_size(self, filesystem):
        if self.size == None:
            size = 0
            for f in self.files:
                size += self.files[f].size
            for d in self.directories:
                if d in filesystem:
                    size += filesystem[d].compute_size(filesystem)
            self.size = size
        return self.size


class Device:
    def __init__(self, input, diskspace):
        root = Directory(name='<root>', fullpath='', parent_fullpath=None)
        self.filesystem = {'': root}
        self.diskspace = diskspace
        self.pwd = ''
        self.last_cmd = None

        for line in input:
            self.process(line.strip())

    def cmd(self, command):
        parts = command.split(' ')
        self.last_cmd = parts[1]
        if parts[1] == 'cd':
            if parts[2] == '..':
                if None is not self.filesystem[self.pwd].parent:
                    self.pwd = self.filesystem[self.pwd].parent
                return
            elif parts[2] == '/':
                self.pwd = ''
            else:
                fullpath = self.check_path_exists(parts[2])
                self.pwd = fullpath
        #elif parts[1] == 'ls':

    def check_path_exists(self, path):
        fullpath = self.filesystem[self.pwd].fullpath + '/' + path
        if fullpath not in self.filesystem[self.pwd].directories:
            self.filesystem[self.pwd].add_directory(fullpath)
            self.filesystem[fullpath] = Directory(name=path, fullpath=fullpath, parent_fullpath=self.filesystem[self.pwd].fullpath)
        return fullpath

    def output(self, result):
        parts = result.split(' ')
        if parts[0] == 'dir':
            # dir listing
            self.check_path_exists(parts[1])
        else:
            filepath = self.pwd + '/' + parts[1]
            file = File(size=int(parts[0]), name=parts[1], parent_fullpath=self.pwd)
            self.filesystem[self.pwd].add_file(file, filepath)

    def process(self, line):
        is_cmd = False
        if line[0] == '$':
            is_cmd = True
            self.cmd(line)
        else:
            self.output(line)
        return is_cmd

#####

file = open('input', 'r')
lines = file.readlines()
device = Device(input=lines, diskspace=DISKSPACE)

answer_pt1 = 0
for d in device.filesystem:
    size = device.filesystem[d].compute_size(device.filesystem)
    if size < 100000:
        answer_pt1 += size
        #print(device.filesystem[d].name, size)

print('Answer #1: ', answer_pt1)

total_used_space = device.filesystem[''].compute_size(device.filesystem)
print('Used space: ', total_used_space)
unused_space = DISKSPACE-total_used_space
print('Unused space: ', unused_space)

space_needed = UPDATE_SPACE - unused_space
print('Needed space: ', space_needed)

answer_pt2 = 0
for d in device.filesystem:
    size = device.filesystem[d].compute_size(device.filesystem)
    if size > space_needed:
        if size < answer_pt2 or answer_pt2 == 0:
            answer_pt2 = size
            print('Found delete candidate: ', device.filesystem[d].name, size)

print('Answer #2: ', answer_pt2)
