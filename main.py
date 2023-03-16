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

    firstLine = input()
    inputArray = firstLine.split()
    n = int(inputArray[0])
    m = int(inputArray[1])

    secondLine = input()
    inputArray = secondLine.split()
    for i in range(0, m):
        ele = int(inputArray[i])
        data.append(ele)

    result = parallel_processing(n,m,data)
    
    for i, j in result:
        print(i, j)

if __name__ == "__main__":
    main()