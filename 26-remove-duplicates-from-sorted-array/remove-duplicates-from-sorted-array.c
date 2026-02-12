#include <stdio.h>

int removeDuplicates(int* nums, int numsSize) {
    // If the array is empty, there are no duplicates to remove.
    if (numsSize == 0) {
        return 0;
    }

    // Pointer 'j' tracks the index where the next unique element will be placed.
    // We start 'j' at 1 because the first element (index 0) is always unique initially.
    int j = 1;

    // Pointer 'i' iterates through the rest of the array.
    for (int i = 1; i < numsSize; i++) {
        // If the current element at 'i' is different from the previous element at 'i-1',
        // it means we found a new unique number.
        if (nums[i] != nums[i - 1]) {
            // Place the unique number at index 'j'
            nums[j] = nums[i];
            // Increment 'j' to prepare for the next unique number.
            j++;
        }
    }

    // The value of 'j' at the end is the new length of the array with unique elements.
    return j;
}