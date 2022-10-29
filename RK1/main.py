from operator import itemgetter

# Язык программирования
# Средство разработки

class Browser:
    def __init__(self, name, id, numUsers):
        self.name = name
        self.id = id
        self.numUser = numUsers

class Computer:
    def __init__(self, name, id):
        self.name = name
        self.id = id

class BrowserComputer:
    def __init__(self, broswer_id, computer_id):
        self.broswer_id = broswer_id
        self.computer_id = computer_id

browsers = [
    Browser("Chrome", 1, 1),
    Browser("Firefox", 2, 2),
    Browser("Opera", 3, 3),
    Browser("Safari", 4, 4),
    Browser("Yandex", 5, 5),
    Browser("Internet Explorer", 6, 6),
    Browser("Edge", 7, 7),
    Browser("Vivaldi", 8, 8),
    Browser("Brave", 9, 9),
    Browser("Maxthon", 10, 10),
]

computers = [
    Computer("MacBook", 1),
    Computer("MacBook Air", 2),
    Computer("MacBook Pro", 3),
    Computer("iMac", 4),
    Computer("iMac Pro", 5),
    Computer("Mac Pro", 6),
    Computer("Mac mini", 7),
    Computer("Pro Display XDR", 8),
    Computer("Accessories", 9),
    Computer("High Sierra", 10),
]

browsercomputers = [
    BrowserComputer(1, 1),
    BrowserComputer(2, 2),
    BrowserComputer(3, 3),
    BrowserComputer(4, 4),
    BrowserComputer(5, 5),
    BrowserComputer(6, 6),
    BrowserComputer(7, 7),
    BrowserComputer(8, 8),
    BrowserComputer(9, 9),
    BrowserComputer(10, 10),
]

def task1():
    res = []    # Итог
    for computer in computers:
        mid_res = []
        if "MacBook" in computer.name:
            for browsercomputer in browsercomputers:
                if browsercomputer.computer_id == computer.id:
                    for browser in browsers:
                        if browser.id == browsercomputer.broswer_id:
                            mid_res.append(browser.name)
            res.append([computer.name, mid_res])
    return res

def task2():
    res = []
    for browser in browsers:
        mid_res = []
        sum = 0
        count = 0
        for browsercomputer in browsercomputers:
            if browsercomputer.broswer_id == browser.id:
                for computer in computers:
                    if computer.id == browsercomputer.computer_id:
                        sum += computer.id
                        count += 1
        try:
            mid_res.append(browser.name)
            mid_res.append(round(sum / count, 2))
            res.append(mid_res)
        except ZeroDivisionError:
            pass
    return sorted(res, key=itemgetter(1), reverse=False)

def task3():
    res = []
    for computer in computers:
        mid_res = []
        if computer.name.startswith('M'):
            for browsercomputer in browsercomputers:
                if browsercomputer.computer_id == computer.id:
                    for browser in browsers:
                        if browser.id == browsercomputer.broswer_id:
                            mid_res.append(browser.name)
            res.append([computer.name, mid_res])
    return res

def main():
    print("Task 1: ")
    print(task1())

    print("Task 2: ")
    print(task2())

    print("Task 3: ")
    print(task3())

if __name__ == "__main__":
    main()
