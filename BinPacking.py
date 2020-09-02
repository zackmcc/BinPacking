###
#   Name: Zackary McClamma
#   Course: CPS 530
#   Date: 08 AUG 2020
###


# This is an implementation of the best fit bin packing algorithm, it first finds the largest value in the array
# then compares that value to the smallest value in the array to determine if both values can fit in the bin, if
# both items will not fit then the largest item is added to its own bin and then the smaller value is placed back
# into the input array. This process is repeated until the input array is empty.
# Inputs:  input_arr - An array of values to be packed into bins
#          bin_size - The size of each bin the input array will be packed into
#
# Outputs: bin_arr - This is an array of arrays where each element of the bin array is the bins that contain the
#                    values from the input array
#
# Running time: O(n log n)
def pack(input_arr, bin_size):
    bin_arr = []
    current_bin = []

    # While the input array is not empty
    while input_arr:
        a = max(input_arr)  # Get max element from array
        input_arr.remove(a)  # remove selected element from the input array

        # While the total value of the current bin plus the current selected element from teh input array does not
        # exceed the bin size
        while sum(current_bin) + a < bin_size:
            current_bin.append(a)  # Append the value to the current bin
            # if the input array is not empty
            if input_arr:
                a = min(input_arr)  # Get the minimum value from the input array
            else:  # Otherwise break out of the loop
                break
            # Check if the current selected element will fit in the bin
            if sum(current_bin) + a < bin_size:
                input_arr.remove(a)  # If it fits remove the element from the input array

        bin_arr.append(current_bin)  # After exiting the current_bin loop append the bin to the bin array
        current_bin = []  # reset the current_bin to empty (start a new bin)
    return bin_arr  # Return the array of bins

def test(input_arr, bin_size):
    print("=============================================================================================")
    print("Bin Size:  " + str(bin_size))
    print("Input array: \n\t\t\t[" + ', '.join(str(x) for x in input_arr) + ']\n')
    print("After bin packing: \n\t\t\t\t\t" + '\n\t\t\t\t\t'.join(str(x) for x in pack(input_arr, bin_size)) + '\n')
    #print("=============================================================================================")
    return


def main():
    print("\nEntering Main method \n")
    test([0.66, 0.33, 0.83, 0.5, 0.33], 1.0)
    test([0.21, 0.83, 0.56, 0.33, 0.66, 0.12, 0.44], 1.0)
    test([0.21, 0.83, 0.56, 0.33, 0.66, 0.12, 0.44], 1.5)
    test([0.21, 0.83, 0.56, 0.33, 0.66, 0.12, 0.44, 0.65, 0.18, 0.11, 0.99, 0.28, 0.01, 0.02, 0.25, 0.36], 1.0)
    test([0.21, 0.83, 0.56, 0.33, 0.66, 0.12, 0.44, 0.65, 0.18, 0.11, 0.99, 0.28, 0.01, 0.02, 0.25, 0.36], 2.0)
    print("Program Complete \n")


if __name__ == '__main__':
    main()
