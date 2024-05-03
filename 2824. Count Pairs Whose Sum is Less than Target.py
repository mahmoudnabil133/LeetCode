# this hashed solution if we wanted to count the only distinct pairs , not all pairs which there sum < targetsum.
class Solution:
    def countPairs(self, nums: List[int], target: int) -> int:
        ctr = 0
        # fst_iterated = []
        for i in range(len(nums)):
            # scnd_iterated = []
            # if nums[i] in fst_iterated:
            #     print('this nums[i]:', nums[i], 'is first iterated at index :' , i)
            #     continue

            for j in range(i + 1, len(nums), 1):
                # if nums[j] in scnd_iterated:
                #     print('this nums[j]:', nums[j], 'is second iterated at index:', j)
                #     continue
                pair = nums[i] + nums[j]
                if pair < target :
                    ctr += 1
                    # if nums[i] in fst_iterated and nums[j] in scnd_iterated:
                    #     print('here')
                    #     pass
                    # else:
                    #   ctr += 1
                    #   print('pair: (', nums[i], ', ', nums[j], ')')
                # scnd_iterated.append(nums[j])

            # fst_iterated.append(nums[i])
        return ctr
