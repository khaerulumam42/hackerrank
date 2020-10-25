# Enter your code here. Read input from STDIN. Print output to STDOUT
def door_mat(n, m):
    stripped = "---"
    stand_dot = ".|."
    median_n = int((n-1)/2)
    for i in range(n):
        if i == (n-1)/2:
            threshold = int((m-7)/2)
            print("-"*threshold+"WELCOME"+"-"*threshold)
        else:
            stripped_times = abs(median_n-i)
            stand_dot_multiplier = int(n-abs((median_n*2)-(i*2)))
            start = stripped*stripped_times
            middle = stand_dot*stand_dot_multiplier
            end = stripped*stripped_times
            print(start+middle+end)

if __name__ == '__main__':
    n, m = input().strip().split(" ")
    
    door_mat(int(n), int(m))
