class Directory:
    def __init__(self, parent, subdirectories, files):
        self.parent = parent if parent is not None else self
        self.subdirectories = subdirectories
        self.files = files
    
    def size(self):
        return sum(file_len for file_len in self.files) + sum([directory.size() for directory in self.subdirectories.values()])

    def get_sizes(self):
        sizes = [self.size()]
        for subdirectory in self.subdirectories.values():
            sizes.extend(subdirectory.get_sizes())
        return sizes

with open('advent_of_code2022/d7p1input.txt') as file:
    root = Directory(None, {}, [])
    wd = root

    line = file.readline()
    while line != '':
        line = line.split()

        if line[1] == "cd":
            if line[2] == "/":
                wd = root
            elif line[2] == "..":
                wd = wd.parent
            else:
                wd = wd.subdirectories[line[2]]
        elif line[1] == "ls":
            pass
        else:
            if line[0] == "dir":
                wd.subdirectories[line[1]] = Directory(wd, {}, [])
            else:
                wd.files.append(int(line[0]))

        line = file.readline()

print(sum([size for size in root.get_sizes() if size <= 100000]))