# The100DaysOfCode Challenge

In this blog I will be sharing my journey from Day1 to Day100 of my #The100DaysofCode Challenge..


## Day 1

On the first day of the challenge I decided to practise some of the basic programs such as Anagram check and array pair sum.

### Anagram Check
```markdown
# 100 Days of Code Challenge
# Method 1
def anagram_check(s1, s2):
    s1 = s1.replace(' ','').lower()
    s2 = s2.replace(' ','').lower()

    return sorted(s1) == sorted(s2)

print(anagram_check('Clint eastwood','old west action'))

# Method 2

def anagram_check2(s3,s4):
    s3 = s3.replace(' ','').lower()
    s4 = s4.replace(' ','').lower()

    if (len(s3) != len(s4)):
        return False
    
    count = {}
    for letter in s3:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in s4:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    
    for k in count:
        if count[k] != 0:
            return False

    return True

print(anagram_check2("Hello","helloo"))
    
```

### Array pair sum
```
def pair_sum(arr,k):

    if len(arr)<2:
        return ("Array too short")
    
    #Sets for tracking

    seen = set()
    output = set()

    for num in arr:
        target = k-num
        if target not in seen:
            seen.add(num)

        else:
            output.add(((min(num,target)), max(num,target)))
        return len(output)
        print("\n").join(map(str,list(output)))

print(pair_sum([1,3,2,2],4))
```


