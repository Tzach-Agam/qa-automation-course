class HardDisk:
    def __init__(self, current_mem, num_of_files):
        self.current_mem = current_mem
        self.num_of_files = num_of_files
        self.all_mem = 100

    def show(self):
        print(f"All disk info: all available memory: {self.all_mem} \n"
              f"current memory: {self.current_mem} \n"
              f"number of files: {self.num_of_files}")

    def freeSpace(self):
        free_space = self.all_mem - self.current_mem
        return free_space

    def addFile(self, size):
        if self.freeSpace() < size:
            return False
        else:
            self.current_mem += size
            self.num_of_files += 1
            return True

    def delFile(self, size):
        if self.freeSpace() >= size:
            self.current_mem -= size
            self.num_of_files -= 1
        elif self.freeSpace() < 0:
            self.current_mem = 0
            self.num_of_files -= 1

The_disk = HardDisk(0, 0)
The_disk.addFile(10)
The_disk.addFile(10)
The_disk.addFile(10)
The_disk.delFile(10)
The_disk.show()

