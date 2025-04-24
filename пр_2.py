class Solution:
    def containsNearbyDuplicate(self, nums: list[int], k: int) -> bool:
        last_seen = {}

        for i, num in enumerate(nums):
            if num in last_seen and i - last_seen[num] <= k:
                return True
            last_seen[num] = i

        return False


# Тестування
if __name__ == "__main__":
    sol = Solution()
    nums1 = [1, 2, 3, 1]
    k1 = 3
    print("Example 1 Output:", sol.containsNearbyDuplicate(nums1, k1))  # Очікувано: True
