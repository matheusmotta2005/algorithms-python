def main():
    input = [7,2,3,1,4,5,6]
    log(input,-1)

    #SORT ALGORITHM

    log(input,1)

def log(value,pos):
    position = ""
    if pos<0:
        position = "Before: "
    elif pos>0:
        position = "After: "
    else:
        position = "Output: "
    print(position+str(value))

main()