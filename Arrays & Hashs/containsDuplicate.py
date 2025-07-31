def hasDuplicate(nums):
        

        s = set(nums)

        if len(s) == len(nums):
            return False
        return True