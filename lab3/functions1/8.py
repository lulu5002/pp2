def spy_game(nums):
    for x in range(0, len(nums) - 2):
        if nums[x] == 0 and nums[x + 1] == 0 and nums[x + 2] == 7:
            print("True")
            return True
    print("False")

spy_game([1,0,2,4,0,6,7]) 
