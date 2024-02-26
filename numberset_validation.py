# code for validating a set of nnumbers using array

import array

def validateNum(min_num, max_num, disabled_num, arr):
    for i in range(len(arr)):
        if (arr[i]<min_num) or (arr[i]>max_num) :
            print ("Invalid Number:", arr[i])
        elif arr[i] not in disabled_num:
            print ("Valid number:", arr[i])
         
        else:
            arr[i]+=1

def main():
    min_num = int(input("Enter the minimum number:"))
    max_num = int(input("Enter maximum number:"))
    disabled_num =set(map(int, input("Enter the disabled numbers: ").split()))
    arr = [1, 5, 7, 8, 9, 12]
    validateNum(min_num, max_num, disabled_num, arr)

main()
