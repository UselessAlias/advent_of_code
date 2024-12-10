from . import aoc_2024_runner

FREESPACE = "."

class FileBlock:
    def __init__(self, id):
        self.id = id

    def __mul__(self, other):
        return [self for _ in range(other)]
    
    def __eq__(self, other):
        if type(other) != type(self):
            return False
        if self.id == other.id:
            return True
        return False
    
    def __str__(self):
        return str(self.id)
    
    def __repr__(self):
        return str(self.id)
    
class DiskSpace:
    def __init__(self, value, length):
        self.value = value
        self.length = length

    def __repr__(self):
        return str(self.value)
    
def find_next_free_space(diskmap, start=0):
    index = start
    while True:
        space = diskmap[index]
        if space == FREESPACE:
            return index
        else:
            index += 1

def find_next_file_space(diskmap, start=None):
    if not start:
        index = len(diskmap) - 1
    else:
        index = start
    while index >= 0:
        if type(diskmap[index]) == FileBlock:
            return index
        else:
            index -= 1

def find_next_file_diskspace(diskmap, start):
    while start >= 0:
        if type(diskmap[start].value) == FileBlock:
            return start
        else:
            start -= 1

def find_next_empty_diskspace(diskmap, length, end):
    index = 0
    while index <= end:
        if diskmap[index].value == FREESPACE and diskmap[index].length >= length:
            return index
        
        index += 1

def solution(input_lines):
    file_num = True
    file_index = 0
    diskmap = []
    for num in input_lines[0]:
        if file_num:
            diskmap += FileBlock(file_index) * int(num)
            file_index += 1
            file_num = False
        else:
            diskmap += FREESPACE * int(num)
            file_num = True

    lowest_freespace = find_next_free_space(diskmap)
    highgest_filespace = find_next_file_space(diskmap)

    while highgest_filespace > lowest_freespace:
        diskmap[lowest_freespace], diskmap[highgest_filespace] = diskmap[highgest_filespace], diskmap[lowest_freespace]
        lowest_freespace = find_next_free_space(diskmap, lowest_freespace)
        highgest_filespace = find_next_file_space(diskmap, highgest_filespace)

    checksum = 0
    index = 0
    while True:
        disk_space = diskmap[index]
        if disk_space == FREESPACE:
            break
        checksum += index * disk_space.id
        index += 1

    file_num = True
    file_index = 0
    diskmap = []
    for num in input_lines[0]:
        if file_num:
            diskmap.append(DiskSpace(FileBlock(file_index),int(num)))
            file_index += 1
            file_num = False
        else:
            diskmap.append(DiskSpace(FREESPACE, int(num)))
            file_num = True

    high_fileblock_index = find_next_file_diskspace(diskmap, len(diskmap) - 1)
    while high_fileblock_index:
        fileblock = diskmap[high_fileblock_index]
        empty_diskspace_index = find_next_empty_diskspace(diskmap, fileblock.length, high_fileblock_index)
        if empty_diskspace_index:
            if diskmap[empty_diskspace_index].length == diskmap[high_fileblock_index]:
                diskmap[high_fileblock_index], diskmap[empty_diskspace_index] = diskmap[empty_diskspace_index], diskmap[high_fileblock_index]
            else:
                empty_space = diskmap[empty_diskspace_index]
                high_fileblock_space= diskmap[high_fileblock_index]

                new_empty_space = DiskSpace(FREESPACE, empty_space.length - high_fileblock_space.length)
                empty_space.length = high_fileblock_space.length 

                diskmap[high_fileblock_index], diskmap[empty_diskspace_index] = diskmap[empty_diskspace_index], diskmap[high_fileblock_index]
                diskmap.insert(empty_diskspace_index + 1, new_empty_space)

                high_fileblock_index += 1


        high_fileblock_index = find_next_file_diskspace(diskmap, high_fileblock_index - 1)

    collapsed_diskmap = []
    for item in diskmap:
        collapsed_diskmap += item.value * item.length

    fileblock_checksum = 0
    index = 0
    while index < len(collapsed_diskmap):
        disk_space = collapsed_diskmap[index]
        if not disk_space == FREESPACE:
            fileblock_checksum += index * disk_space.id
        index += 1

    return checksum, fileblock_checksum

aoc_2024_runner.add_daily_solution("09", solution)