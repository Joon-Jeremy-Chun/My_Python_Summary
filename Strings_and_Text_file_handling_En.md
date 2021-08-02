# Strings and Text files handling
+ It needs to read data or string types from text files. 
+ Vary of `method` options will help manipulation on the string.
+ Input text file data can save data type.
+ Can control string `split`, `strip(delete)`, and `connect`.

# Strings handling
## 1. To Split string `.split()`
+ Use `.split()` method.
+ list type comes out as a result of the method.
```python
my_str.split([sep]) # the data will be split by 'sep'
```
+ Unspecified parameters on the `.split()` method, the data will be splited by all of `empty space( )` and `newline(\n)`

ex) Split the dat by `space`
```python
my_str = "I love you vary much"
my_str.split()
```
out : ['I', 'love', 'you', 'vary', 'much']
<br/><br/>

ex) Split the data with `comma(,)`
```python
my_str = "I love you vary much"
my_str.split()
```
out : ['I', 'love', 'you', 'vary', 'much']
<br/><br/>
+ specific parameter `maxsplit = #` will commit the numbers of splits.

ex) Divide the data `three sections` by `space`
```python
my_str = "I love you vary much"
my_str.split( maxsplit = 2) #Makes 2 split points
```
out : ['I', 'love', 'you vary much']
<br/><br/>

ex) Change the international phone numbers to domestic phone numbers
```python
phone_number = "+82-10-2345-6789"
my_num = phone_number.split("-", maxsplit = 1)

print (my_num)
print ("S.Korea domestic phone #: 0{0}".format(my_num[1]))
```
out1 : ['+82', '10-2345-6789']\
out2 : S.Korea domestic phone #: 010-2345-6789
#
## 2. To remove strings `.strip()`
+ `.strip()` method removing the string from front and back, both sides.
+ It deletes string until assigned parameter `character(chars)` appears.
+ `Space` and `newline` will be removed, if no assigned character.

ex) remove `space` and `newline`
```python
my_str = "   python\n     "
my_str.strip()
```
out : 'python'
<br><br>
ex) remove a string 
```python
my_str = "ooopythonooooooo"
my_str.strip('o')
```
out : 'python'
<br><br>
ex) remove several strings
```python
my_str = "##!!aaapythonaaa!a!a#a"
my_str.strip('#!a') # the order is not matter.
```
out : 'python'
<br><br> 
+ One-side removing passible; `.rstrip()` for right side, `.lstring()` for left side.

ex) remove the string left or right side.
```python
my_str = "ooopythonooooooo"
my_str.lstrip('o') # delete left-side 'o'
my_str.rstrip('o') # delete right-side 'o'
```
out1 : 'pythonooooooo'\
out2 : 'ooopython'
<br><br>
+ Can use more complicated tasks

practice 1) The given data composed words, `comma(,)`, `space`, and `newline`. Save the words in a list type.
```python
data_1 = "   I ,love , you \n , so,much \n\n"

# split the words by (,)
data_list1 = data_1.split(',')

# remove all space and newline in the list
list_final = [] # define empty list
for x in data_list1 :
    wordsFinal = x.strip()
    list_final.append(wordFinal)

print(list_final)
```
out : ['I', 'love', 'you', 'so', 'much']
#
## 3. To join strings