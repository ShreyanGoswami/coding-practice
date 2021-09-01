def sort(arr):
    track = {0: 0, 1: 0, 2: 0}
    for n in arr:
        if n in track:
            track[n] = track[n] + 1
    outputRes = ""
    for key, value in track.items():
        for i in range(0, value):
            outputRes += str(key) + " "
    outputRes = outputRes.strip()
    print(outputRes)


def main():
    t = int(input())
    for i in range(0, t):
        n = int(input())
        inp = input().strip()
        if inp is not None and inp != "":
            inp = inp.split(" ")
            inp = [int(i) for i in inp]
            sort(inp)


main()
