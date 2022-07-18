/**
 *. Note: The returned array must be malloced, assume caller calls free().
 */

#include <stdio.h>
#include <stdlib.h>

int *twoSum(int *nums, int numsSize, int target, int *returnSize)
{
    *returnSize = 2;
    int *ans = (int *)malloc(sizeof(int) * 2);
    for (int i = 0; i < numsSize; i++)
        for (int j = i + 1; j < numsSize; j++)
            if (nums[i] + nums[j] == target)
            {
                ans[0] = i;
                ans[1] = j;
            }
    return ans;
}

int main(void)
{
    int returnSize = 0;
    int nums[] = {2,7,11,15};
    int *ans = twoSum(nums, 4, 9, &returnSize);
    for (int i = 0; i < 2; i++)
        printf("%d, ", ans[i]);
    printf("\n");

    return 0;
}