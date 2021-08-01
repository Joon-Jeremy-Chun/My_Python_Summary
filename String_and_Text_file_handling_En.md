# String and Text file handling
+ It needs to read data or string types from text files. 
+ Vary of `method` options will help manipulation on the string.
+ Input text file data can save data type.
+ Can control string `split`, `strip(delete)`, and `connect`.

# String handling
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
## 2. To remove string `.strip()`
+ 