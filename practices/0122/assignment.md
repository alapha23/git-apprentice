### Assignments for 0122

#### 1\. Palindrome Number [Source](https://leetcode.com/problems/palindrome-number/)

Given an integer `x`, return true if `x` is palindrome integer.

An integer is a **palindrome** when it reads the same backward as forward.
* For example, `12321` is a palindrome while `123` is not.


```
# -> bool means the return value is always a bool
# x: int means the input x has type int
def isPalindrome(x: int) -> bool:
    return True

print(isPalindrome(12421))
print(isPalindrome(824428))
print(isPalindrome(-12))
print(isPalindrome(53533535))
```

##### Hint: Consider the conditions when x is negative

#### 2\. Binary Search

Assuming that we're searching for a value val in a sorted array, the algorithm compares val to the value of the middle element of the array, which we'll call `mid`.

* If `mid` is the element we are looking for (best case), we return its index.
* If not, we identify on which side of `mid` `val` is more likely to be on based on whether val is smaller or greater than `mid`, and discard the other side of the array.
* We then recursively or iteratively follow the same steps, choosing a new value for `mid`, comparing it with `val` and discarding half of the possible matches in each iteration of the algorithm.

```
def binarySearch(lst, target):
  index = 0
  return index

# Assume every element is unique in the list
lst = [1,3,5,2,9,34,12,-4,32]
target = 12
result = binarySearch(lst, target)
print(result)
```

##### Hint: Read [this](https://www.geeksforgeeks.org/binary-search/)


#### 3\. Two Sum [Source](https://leetcode.com/problems/two-sum/)

Given an array of integers `nums` and an integer `target`, return indices of the two numbers such that they add up to `target`.

You may assume that each input would have **exactly one solution**, and you may not use the `same` element twice.

You can return the answer in any order.

**Example 1:**

```
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
```
**Example 2:**
```
Input: nums = [3,2,4], target = 6
Output: [1,2]
```

**Example 3:**
```
Input: nums = [3,3], target = 6
Output: [0,1]
```
**Constraints**
* 2 <= nums.length <= 104
* -109 <= nums[i] <= 109
* -109 <= target <= 109
* Only one valid answer exists.

##### Hint: Iterate through the list, search for value (target - nums[i])

```
def twoSum(nums: List[int], target: int) -> List[int]:
        

lst = [1,5,2,8,12]
target = 10
result = twoSum(lst, target)
print(result)
```

#### 4\. Fibbonaci [Source](https://leetcode.com/problems/fibonacci-number/)

The **Fibonacci numbers**, commonly denoted F(n) form a sequence, called the **Fibonacci sequence**, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,
```
F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
```
Given `n`, calculate `F(n)`.

**Example 1:**
```
Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
```
**Example 2:**
```
Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
```
**Example 3:**
```
Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
```

**Constraints:**

* `0 <= n <= 30`

```
def fib(n):


print(fib(5))
print(fib(8))
print(fib(10))
```


