# Question 1

nums = list(range(30, 61, 5))
print(nums)

print(nums[:: -1])

nums.append(65)
nums = nums[:: -1]
print(nums)



# Question 2

newlist = []
for i in range(0,21):
    newlist.append(i)
print(newlist)

newlist.remove(0)
print(newlist)

print(len(newlist))
print(max(newlist))
print(min(newlist))

total = 0
for i in newlist:
    total += i
print(total)



# Question 3

weather = {'sunny': 'play', 'rainy': 'watch TV', 'cloudy': 'walk'}

for key, value in weather.items():
    print('when', key, 'let us', value)   
    
weather['snowy'] = 'ski' 
