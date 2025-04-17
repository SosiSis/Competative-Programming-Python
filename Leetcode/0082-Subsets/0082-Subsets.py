def subsets(nums):
    res = []
    subset = []

    def create_subset(i):
        if i == len(nums):
            print("Adding subset:", subset)
            res.append(subset[:])
            return

        # include nums[i]
        subset.append(nums[i])
        print("Include", nums[i], "->", subset)
        create_subset(i + 1)

        # exclude nums[i]
        subset.pop()
        print("Exclude", nums[i], "->", subset)
        create_subset(i + 1)

    create_subset(0)
    return res
print(subsets([1,2]))