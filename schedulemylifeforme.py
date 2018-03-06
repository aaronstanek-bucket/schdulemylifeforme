import pbcl
import time

def start():
    w = pbcl.load("todo.pbcl")
    tasks = []
    while True:
        w.forward()
        if w.term:
            break
        tasks.append([w.get_var("name"),w.get_var("due")])
    return tasks

def make_time_numbers(t):
    for i in range(len(t)):
        t[i][1] = time.strptime(t[i][1],"%Y %m %d %H %M")

def handle_top(top,n):
    spot = 0
    while True:
        if spot>=3:
            return
        if spot>=len(top):
            top.append(n)
            return
        if n[1]<top[spot][1]:
            k = top[spot]
            top[spot] = n
            n = k
            del(k)
        spot += 1

def get_top_three(t):
    ou = []
    for x in t:
        handle_top(ou,x)
    return ou

def main():
    z = start()
    make_time_numbers(z)
    z = get_top_three(z)
    for i in range(len(z)):
        print(str(i+1)+". "+str(z[i][0]))

main()
