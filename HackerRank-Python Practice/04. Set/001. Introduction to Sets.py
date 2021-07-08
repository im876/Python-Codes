def average(array):
    # your code goes here
    average = sum(set(arr)) / len(set(arr))
    return average

if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
