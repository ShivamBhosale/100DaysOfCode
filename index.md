## The100DaysOfCode Challenge

In this blog I will be sharing my journey from Day1 to Day100 of my #The100DaysofCode Challenge..


### Day 1

On the first day of the challenge I decided to practise some of the basic programs such as Anagram check and array pair sum.

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

For more details see [GitHub Flavored Markdown](https://guides.github.com/features/mastering-markdown/).

### Jekyll Themes

Your Pages site will use the layout and styles from the Jekyll theme you have selected in your [repository settings](https://github.com/ShivamBhosale/100DaysofCode/settings). The name of this theme is saved in the Jekyll `_config.yml` configuration file.

### Support or Contact

Having trouble with Pages? Check out our [documentation](https://docs.github.com/categories/github-pages-basics/) or [contact support](https://github.com/contact) and we’ll help you sort it out.
