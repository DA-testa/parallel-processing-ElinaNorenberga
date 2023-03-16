# python3

class Process:
    def __init__(self, number, processing, seconds):
        self.number = number
        self.processing = processing
        self.seconds = seconds


class Data:
    def __init__(self, number, taken):
        self.number = number
        self.taken = taken


def parallel_processing(n, m, data):
    output = []
    processes = []
    for process in range(n):
        processes.append(Process(process, False, 0))

    dataList = []
    for da in data:
        dataList.append(Data(da, False))

    seconds = 0

    for da in dataList:
        taken = False
        while taken == False:
            for process in processes:
                if (process.seconds <= seconds):
                    process.processing = False
                if taken == False:
                    taken = add_job(process, seconds, da, output)
            if (taken == False):
                seconds = seconds + 1

    return output


def add_job(process, seconds, da, output):
    if (process.processing == False and process.seconds <= seconds):
        process.processing = True
        process.seconds = process.seconds + da.number
        output.append([process.number, seconds])
        return True
    else:
        return False


def main():
    n = 0
    m = 0

    data = []

    ievade = input()
    text = ""
    if ievade == "F":
        text = input()
        with open(text) as f:
            lines = f.readlines()
            array = lines[0].split()
            n = int(array[0])
            m = int(array[1])
            array = lines[1].split()
            for a in array:
                data.append(int(a))
    if ievade == "I":
        n = int(input("Enter number of elements : ")) 
        for i in range(0, n):
            ele = int(input())
            data.append(ele)

    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()