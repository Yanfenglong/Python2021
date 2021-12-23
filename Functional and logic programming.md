![logo](./image/logo.jpg)

## 1. Functional and logic programming

- Free（Open source GPL）

- Cross platform

- Powerful(It can be embedded in C / + + programs which is often called glue language)

- Clear and elegant（zen of Python）

  ##### Application
  
  - Image recognition：Pig、Horse、bug、ship、face
  
    ![pig](./image/AI/pig.gif)
    
    <video src="./image/AI/horse.mp4" height="300" controls="controls">
    您的浏览器不支持 video 标签。
    </video>
    <img src="./image/AI/bug.png" alt="index" style="zoom:25%;margin-left:400px" /><img src="./image/AI/ship.png" alt="index" style="zoom:75%;margin-left:100px" />
    
    <video src="./image/AI/jiewu1.mp4" height="300" controls="controls">
    您的浏览器不支持 video 标签。
    </video>
    
  - Face generation、Face synthesis
  
    ```
    https://aistudio.baidu.com/aistudio/projectdetail/2189795
    ```
  
    
  
    <video src="./image/AI/driving_video.mp4" height="200" controls="controls">
    您的浏览器不支持 video 标签。
    </video>
  
    <video src="./image/AI/result_with_music.mp4" height="200" controls="controls">
    您的浏览器不支持 video 标签。
    </video>
  
    
  - Generative Adversarial Networks: Create a new image or video which is not exist
  
    <img src="./image/AI/mn.gif" alt="index" style="zoom:25%;" />
    
    
    
    ```
    「 anime」：create cartoon pic
    http://www.thiswaifudoesnotexist.net/
    https://thisanimedoesnotexist.ai/
    「cat」：create cats pic
    http://thesecatsdonotexist.com/
    「 Airbnb 」：create room pic
    https://thisairbnbdoesnotexist.com/
    ```
    
  - music create
  
    ```
    https://aistudio.baidu.com/aistudio/projectdetail/2191339
    https://www.xfyun.cn/services/online_tts
    ```
  
  

### 1.1Environment installation

In Anaconda there are 2 version, 2.x   and 3.7. Python3  is better, it is more power

Version selected :  Python2 VS Python3 

IDE: integrated development environment

```
IDE needed:Anaconda Version:Python 3.8 • 64-Bit Graphical Installer 
Software download link：
https://www.anaconda.com/products/individual
```

<font color = 'red'>**Anaconda**</font>：An open source Python distribution，which contains a large number of tools.  And spyder、jupyterNotebook

![anaconda](C:\Users\everi\Desktop\Code\Python\Py2021\image\anaconda.png)

Spyder：Run the script here, like Eclipse

jupyterNotebook： A web applications that allow creation and sharing. Support multiple programming languages such as Julia、R、Python、Octave.

First click Jupter Notebook label, and it will jump a website page. In this website ,we  select a path in our computer. In my computer I select Desktop/Code/Python/Py2021. You can select any path at will.

And select New/Python3 button/ then rename it --Lesson-1

interactive programming ：Run the code in cmd

Script programming：Run the script after switching paths ,python a.py

in cmd

```
for i in range(10):
    print(i)
    #double click enter
type quit()/exit() to exit interactive programming
```

Jupter NoteBook

​           - code sharing by email/Git

          - big data integration：spark、scala、scikit-learn、R、python

```
print("Hello world1")  
The difference between ctrl + enter, shift + enter and alt + enter
#ctrl + enter :the function is run the code 
#shift + enter :first run the code, in the same time, jump to the next code block
#alt + enter :insert a new block to write the python code
```

- export/import ipython file

```
export:share the file. Click File/ Download as / and then choose ipython file/ py
import: upload button/ find the file from others
```

- annotations 

```
#  If i want the code donot run for a signle line, we add annotation like this #

'''
If there are many line of content, we need add annotation. Multiline string
'''
```

Practice ：put out a Christmas tree

```
print("   *","  ***","*******","   |",sep="\n")
```



### 1.2 Overview of data types

Python standard data type

- String 

  ```python
  #1. The basic data type :String
  name = '123_abc' # signle line, the number ,letters,under score is ok to definite the string
  # '' signle quotation     ""double quotation,for multiline we use three quotation
  name2 =  '''
  david
  fly
  Russell
  '''          # multiline
  print(name, name2)
  # We can use type() function to check the data type
  print(type(name))  # str = string
  name3 = "His name is 'fly'"
  ```

  

- Numbers include int( 1,2) and float(1.0, 3.1415926)

  ```python
  #2. The basic data type :Number
  x1 = 1
  x2 = 10.0 #number
  #the defination of float is not the real number , it is much closer to this number
  print(type(x2))
  print((0.1 + 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1)== 0.9)     #False
  #if we want to make a judgement (0.1 + 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1) and 0.9
  print(0.9-(0.1 + 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1+ 0.1) < 10 **-9 )  #True
  ```

- Bool :True/False，it is useful to make judgments

  ```
  #3. The basic data type :BOOL
  x3 = False == 1 # the real value of False is 0 in number(False == 0 )
  x4 = True == 0  # the real value of True is 1 in number(True ==1 )
  print(x3,x4)
  print(x3 * 5, type(x4))  # calculation
  ```

- List

  ```python
  #4. The basic data type :List
  #List is a range of data, inside of there are many kinds of data type,
  #such as string,number,list
  lst = [1,2,3,4]
  lst1 = ["a","b","c"]
  lst2 = [["Jack","Bob","Kite"],1,2,3,"a","b","c",[1,2,3]]
  print(lst2)
  #In list we can get the number by position, we call the position as index,
  #If we want to get 3, we can write like lst[2]
  print(lst[2]) 
  print(lst2[0][2])  #we need add another square bracket []
  ```

- Tuple 

  ```
  #5. The basic data type :Tuple
  #Tuple is also a range of data, but we can not change the value inside of it. 
  #So Tuple is a special kind of List
  tup = (1,2,3,4)  # not square bracke
  tup1 = 1,2,3
  tup2 = 1, 
  lis3 = [1,2,3,4]
  lis3[2] = 100
  #tup[2] = 100
  print(lis3)  # ctrl +enter
  print(type(tup))
  ```

- Dict

  ```
  #6. The basic data type :Dict
  #Dict  is a pair of value, it is  key and  value.
  #the key and value is unordered, we can not sort it
  dic1 = {"name":"Jack","age":19,"city":'peak',"hair":"black"}
  print(dic1,type(dic1)) 
  ```

- Type conversion(change int\float\ string are included, others will discussed later)

  ```
  val1 = 5 # int
  val2 = float(val1) #float
  val3 = str(val2)  #string  
  val4 = 5.5
  val5 = int(val4)  #change float to int
  print(type(val1),type(val2),type(val3),type(val5))
  ```

  Lesson 1 review:
  
  ```
  1.please describe the basic data type.
   a = 1.0   #number float
   a = 'my name is yan'  #String  ''signle quotation ""double quotation
   a = [1,2,3]   #  list  []square bracket 
   a = (1,2,3)   #  tuple () parentheses
   a = {"name":"Jack"} #dict {} curly brACE 
   
  2.what is the meaning of these function? 
    print()\  type()
    
  3.How to import/export/create a jupterNoteBook 
  ```
  
  


### 1.3 Basic knowledge

- 1.variable

> Variable value is not fixed，the equal sign is used to assign values to variables。The rules of variable name：
>
> 1.The first character of a variable name must be a letter Or underline(Upper case or lower case is ok)，It cannot start with a number
>
> 2.Variable name cannot be a keyword

```
#word = 4
#hello = 5
hello, world = 5,4  #add comma , maltivariable assignment
a = b = c = 1   # a =1; b=1; c=1
print(a,b,c,hello)
```

- 2. operator

```python
#operator +addition -substraction *multiplication / division
#+addition -substraction *multiplication / division
print(3+4-2*6/3)  #
# ** is the power of a value  2**3 = 2*2*2 =8 
print(5**3)
#// back slash Take the integer division  
print(8//3)   #
#% precent sign.   Modular operation -Returns the remainder of division
a = 21
b = 10
print(a%b)   #20 = 10 * 2 +1 
# calculate the equation 40 - 3 ** 2 +8/2**3 *10
print(8/2**3 *10)
#in 8/2**3 *10 , which part runs first? 8/2 or  2**3 or 2 *10

#**power//Take the integer division  %Modular operation -Returns the remainder of division

#Question: if i want to get 1,7,5 from 175, How to do?  
a = 175
print(a//100)       #1
print(a //10 % 10)    #print(int(135 /10 % 10))   print(135//10 -10)    #
print(a % 10) 

#compare calculation: > greater < lower <= greater equal 
# >= lower equal == equal  != not equal
print(5 != 3)

#logic calculation ---3 keyword:and or not
print( 3 > 2 and  4 <= 3 )  # both of them is true ,the result is true
print( 3 > 2 or  4 <= 3 )  # one of them is true ,the result is true
print(not 3 > 2)

#member operator: -- keyword: in / not in ,it is useally used in list and dict
ls = [1,2,3,4]
print(2 not in ls)
dict1 = {"name":"yan","age":18}
print("name" not in dict1)
```


```python
#Directional data ,It's not that the value of X has changed, but that the position pointed by X has changed
x = 1 # store 1 in c disk
print(x)
x = "hello world" #store "hello world" in d disk
print(x)
```



## 2. Python container

### 2.1 List

​	x = 1 means x is a variable, and its value is unique. When x = [1,2,3,4], it is a list. There are four elements in this list . Inside of a list there are many kind of data type, such as string/number/list etc.

```python
list0 = [1,2,3,4]  # add 4 elements  in a sequence
list1 = [1,2,3,4,"hello","world",[5,6,7],1.3,5.4]
list1
```

- List common operation

```python
#Link and repeat
x = [1,2,3]
y = [4,5,6]
#print(x+y, x*2)  #  link and repeat
# 2 function to control list : append, extend
x.append(y)  #append add a new element
print(x) #[1, 2, 3, [4, 5, 6]]
x.extend(y)
print(x)  #[1, 2, 3, 4, 5, 6]
#append modifiy the original list itself, whileise +create a new one [1,2,3]+['Jack']
```

​       Each element has a index, that is the element position. Get an element by specifying a subscript(index), or by specifying a range, you get elements for a set of sequences. This way of accessing sequences is called slicing.

```python
list2 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
list3 = [1,2,3,4,"hello","world",[5,6,7],1.3,5.4]
list4 = [1,2,[5,6,7],1,2,3,4,"hello","world",[5,6,7],1.3,5.4]
#print(list3[6][2])  #use position/subscript/index get the element
#print(list4[-2]) 
# if we use negative number , it count from right to  left, -1 is the last element
#slicing:add some colons , start : stop(limit) number : step
#the stop number is not included in this range
#print(list2[0:80:3]) 
#print(list2[2::])   # list2[0:10:1]
print(list2[-1::-1]) # count from right to left,parameters can be set as negative number
```



```python
#some build-in function  len --length of a list
list2 = [1, 2, 3, 4, 5, 6, 7, 8,3] # '' is string
#print(len(list2),list2.count(3) )
#max , min , sum 
# these function are defined for the list of neumber only
print(max(list2), min(list2), sum(list2))
#index 
print(list2.index(3))
#The basic global function in list, it return the max,min,sun value of list 
#These function are defined for the list of numbers only
# .index(obj)：Find the index position of the first match of a value from the list
```

> ```
> Note：1.end_index is actually the index of the first object you don't want to get，so ls3[0:-1] can not get ls3[-1]. So if you want to get the element include end_index location，you donnot need to write end_index(ls3[::])，or enter a value that is outside the end_index range.
> 2.When the step is positive, indicating left to right.If step is negative, the range count from right to left 
> ```

```python

#Question
x = [1,2,3,1,[1],[1,1],'1']
#what is the different between type(x[1]) and type(x[1:2])？ int vs list
#what is the value of x.index(1),x.count(1)？ # 0 , 2
```



```python
a = [1,2,3,['my','name'],'1']
print(a[3][1]) # print(a[-2][1])

#practice :  You can change the length at will，+ *
#1.a = [1,2,3] a = ['1','2','3'] different
 
#2.change a to [1,2,3,'Jack']  

#3. create a list m = [3,1,5,5,4,3,77,8] print the second and fourth element.
```



- List and generator(range)

```python
#generator: it is comma , not colons , start : limit number : step
b = range(10)
c = list(range(10))
print(c)
```



```python
Question:
    1. is the result of range() integer？  # yes
    2. create a range with 5 element， Use type() to check its type
    3. which grammar is correct？a = range(5) ，a = range(2:6),a = range(3,7) 
    4. if  b = range(10), what is the result of b[2],b[-2],b[5] 
```

- Insert and delete 

```python
#remove an element
#c.remove(5)
#del is a sentence , slice
#del c[2:4] 
#c.clear() #clear the whole list
c.insert(1,"hello") #insert(index, value),index this the position of this list
print(c)
```

- Copy list

```python
f = list(range(8))
#g = f
g = f.copy()  
#copy points to another new list
#the direct assignment points to the same list
g[1] = 100
print(f,g)
```



- Sort

```python
j = [3, 5, 100, 45, 4, 78, 56 ] # unordered list
k = ['abc','hello','solo','world']
#j.sort(reverse = False)  # ordered, numbers are arranged sequentially
k.sort() #letters are arranged in alphabetical order
m = sorted(j,reverse = True) 
#sort and copy a list, so j is not changed
print(j,m,k)
```

Lesson-2 review Question:

      1. what is the difference between sort and sorted?

```python
m.sort()   -- modify the original list into an ordered sequence
sorted(m)  -- create a new list
```

​    2. create a list m = [1,2,4,1,1,3] , insert ["Jack"] between 4 and 1

```python
m.insert(3,"Jack")
```

   3.m = [1,2,4,1,1,3] what is the difference between m.remove(2)  ,m.pop(2), del m[2]

```python
m.pop() ,del m[2] is a statement, the result is same
```

  4 .what is the difference between append and extend?

```python
append #  [1,2,3,[4,5,6]]  
extend #  [1,2,3,4,5,6] 
```

5. Input 3 int x,y,and z，please output these three numbers from small to large.

we need to use 2 function: input(), for i in range():

```python
#first we define an empty list, when we insert a value, we append this value into the list, and then use sort function  
i = []
for k in range(3):
    a =  int(input("Please input the number here"))
    i.append(a)
i.sort(reverse = True) # try to output the value from large to small
print(i)
 
```



### 2.2  Tuple 

Tuple is a special list, of which  the value can not be changed

```python
a = (1,2,3,4)
b = 1,
c = [1,2,3]
del c[2]
#del a[2]  #'tuple' object doesn't support item deletion
#del a
#build in functions is ok : such as max , min , len,
print(max(a),min(a),len(a))
d = list(a)
d.insert(1,'abc')
print(d)
```



### 2.3 Dict

  Dictionary is another variable container model. it  can store any type of object. Keys must be unique, but values do not. In dict. In dict , key value pair is separated by colon, and each pair is separated by comma, whereas the dict is enclosed in curly braces.

```python
#dit In dict , key value pair is separated by colon, 
#and each pair is separated by comma, whereas the dict is enclosed in curly braces.
e = {'name':'yan','name12':['Jack'],(1,2):["hello"]}
#the key can be string/Tuple, but not be list,the value is string/list/dict
f = {'name':'yan','home':{'location':'Jakarta','email':'yan@google.com'}}
g = {'name':'yan'}
g['age']  = '30' #insert
g['name'] = 'Jack'  #update
del g['age']  #delete
g #query, find information inside of it , we just type its name
```

- Built-in functions in dict

```python
#Built-in functions in dict
dic1 = {'a':'1','b':'2'}
dic2 = {'c':'3','d':'4'}
dic3 = dic1.copy() #copy a new dict
dic1.update(dic2) #add the content, merge two dict together
print(dic1,dic2,dic3)
print(len(dic1)) #len
print('hello' in dic1) # in :determine if a dict contains this key
```

- Content reading in dict

```python
dic4 = {'name':'yan','home':{'location':'Jakarta','email':'yan@google.com'}}
print(dic4['home']['location'])
print(dic4.get('home').get('location')) # dict.get()
print(dic4.values(),dic4.keys()) #

```



```python
dic5 = {'name':'yan','age':'18','height':'180cm','hair':'black',
        'home':{'location':'Jakarta','email':'yan@google.com'}}
#use a loop , like for cycle
for i in dic5.values(): #here we output the values, try to output the keys 
    print(i)

for k,v in dic5.items():  #(k,v)
    print(k,v)  #print(v)
```



```python
#practice: use input function, try to input 1,2,3    
#if you input 1  , the system output : 'you have input 1'
#if you input 2  , the system output : you have input 2
#if you input 3  , the system output : you have input 3
#if you input other number , the system output : you have input wrong number
info = {'1':"you have input 1",'2':"you have input 2",'3':"you have input 3"}
a = input("please input value here")
print(info.get(a)) #if user input other number,we need do judgement
```



### 2.4 Set

  Set is an unordered sequence of non repeating elements. You can create a set using braces {} or the set() function. 

```python
basket = {"apple","orange","pear","apple","apple","apple"}  #set type
basket1 = set("pear")
print(basket1)
set1 = set("orange")# letters
set2 = {}  #it is dict type
set3 = set(("orange","pear","apple")) #words
print(set3)
```

calculate set

```python
set4 = {"a","b","c","d"}
set5 = {"e","f","c","taobao"}
#print(set4 ^set5) # | or & and ^ only in set 4 or in set5 
set5.add("google")#add element
set5.remove("c")#remove element
set5.discard("c")#remove element,even the element does not exist, there is no error
set5.pop() #randomly delete an element,takes no arguments
print(set5)
```



## 3. Control flow 

### 3.1 Sequential structure

Sequential structure means that the code is executed from top to the bottom without branches or loop  

### 3.2 Branching structure

- if statement

```python
#multi conditions we use or/ and 
age = 29
if (age >18 and age < 22) or (age >24 and age < 30): 
    print("you are old enough to be an university student")
else:
    print("you are old enough")
  # if statement must be followed by a colon ： 
  # automatically indent: For consistency, we always use four spaces to indent a block
  # when if statement finished. Code return to the original indent, continue writing
  # Indentation rules in Python：Code with the same indentation is considered the same block
```

Question： Find the prime number in 1-15

Rule: Find a number, divide 2 to sqrt (this number) by a number. If it can be divided by an integer, it indicates that this number is not a prime number. Otherwise it is a prime number.

for example: 6 can be divide by 3

```python
from math import sqrt
leap =1　
for i in range(1,15):
    k = int(sqrt(i+1))
    for j in range(2,k+1):
        if(i % j == 0):
            leap =0
            break
    if(leap ==1):
        print(i)
    leap =1 
```




### 3.3 Cycle structure

- for cycle

```python
#For cycle is  a loop , we can get all the elements from a sequence,such as list/dict
lst = list(range(5)) # 0,1,2,3,4
#1 in range:range(start,stop,step)   default value for start is 0;if there is only 1 parameterx the int list value sorted from o to x-1; step is the growth value of each cycle sequence
# 2 in list
for i in lst[::2]: #slicing
    print(i)
```



```python
# 3in dic
dic1 = {'Tom':'18','Jack':'19','Alex':'20','Mary':'21'}
for i in dic1:
    print(dic1[i])
```



```python
for i in range(3):  #underline is ok
    for k in range(2):  #nest loop, circulate embedding method
        print(i,k)   #we should not use nest loop too much, no more than 3 time 
```

#practice: 

1.write a for cycle ,try to output even number which is no more than 10
#0,2,4,6,8

```python
for i in range(10):
    if  i % 2 ==0:
        print(i)
print("That is the even number")
```

2."Narcissistic number" is a three digit number， The sum of each digit cube is equal to the number itself. 

For example , 153 is a narcissistic number，because 153=1* * 3＋5 * *3＋3**3. And 3 raised to the power of 3 is 27， 125 is the cube of 5.

Please get all the "Narcissistic number" from 100 - 1000

```python
for i in range(100,1000):  #IF I = 153
   a = i // 100  #1
   b = i %10 // 10 #5
   c = i%10 #3
   if(a**3 + b**3 + c**3 == i):
       print(i)
```


- while cycle

while cycle construct a structure similar to an infinite loop or use it in a loop with an uncertain times.

```python
count = 0
while count < 10:
    print("The count is ",count)
    count = count+1
print("Good bye",count)
#  count < 10is a judgement statement, when the result is true. 
#It will get into the function body and countinue to run
```



```python
# Infinite loop：if a judgement statement never change to false，The loop will execute indefinitely
# we must aviod infinite loop
var =1
while var == 1:
    num = input('enter the number here')
    print('you entered ',num)
    
# while-else
#while-else === the same as if-else
count = 11
while count < 10:
    print("The count is ",count)
    count = count+1
else:
    print("The count is greater than 10",count)
```



Practice：

1. Output all even number which is less than 10

```python
i = 1
while i<10:
    i +=1
    if i%2 ==0:
        print(i)
```




- Loop control statement

The **break ** statementends the current loop and jumps to the statement immediately following the loop.

**Continue** ends the current interation and jump to the top of the loop and starts the next interation.

**pass** is an empty statement, it keep the integrity of the program structure 

```python
# 1.break statement:So break will terminate a loop
s = 0
n = 1
while n > 0:
    s = s+n
    n = n+1
    if(n == 5):
        break
        print('abc')
print(n,s) 
# nested loop
s = 0
for  i in range(10): #i
    for j in range(5):
        print(i,j)
        s = s + (i*j)
    if s > 20:
        break #break statement stop execution of the deepest loop
        #and start executing the next line of code
#2 continue
i = 1
while i<10:
    i +=1 # i =4
    if i%2 ==0:
        print("it is even number",i)
    else:  
        continue#i =3
# countinue tell the programme to skip the remaining statement of the current loop
#and then proceed to the next cycle
        print("it is odd number",i)
#3 pass
for  letter in 'welcome':
    if letter == 'm':
        pass # it neither break nor skip the loop
        print("the current letter is m")
    print("the current letter is ",letter)
print("Goodbye")
```

practice:

1. run the code below on your computer, and see the result  

```python
s = 0
for i in 'helloworld,hello Jakarta':
    if i == 'w':
        pass #try to continue to see what happened
        print('now it is w，but I pass')
    elif i == 'd':
        print('now it is d，but I break')
        break
    print('now it is %s'%i)
print('The end')
```

2.Try to find all the even number in 1-20, and calculate the sum of all the even number

```python

```
#break continue pass
s = 0
for i in range(20):
    if i%2 == 0:
        s += i
    else:
        continue
    print('%i'%(i/2))
print('result is %i'%s)
  ```

  ```

### 3.4  Flow chart 

PyFlowchart is a package to：

- write flowchart in Python,
- translate Python source codes into flowchart.

https://github.com/seflless/diagrams#flowchart

https://gitee.com/cdfmlr/pyflowchart#https://github.com/francoislaberge/diagrams/#flowchart

**step1**: install the third-part package:pip3 install pyflowchart

![1](C:\Users\everi\Desktop\Code\Python\Py2021\image\222.png)

**step2:** define python code ,store it on the desktop change py into flow chart syntax  ,  

```sh
python -m pyflowchart test.py
```

```flow
op2=>operation: s = 0
cond5=>condition: for i in range(10)
cond38=>condition: for j in range(5)
sub47=>subroutine: print(i, j)
op49=>operation: s = (s + (i * j))
cond54=>operation: break if  (s > 20)

op2->cond5
cond5(yes)->cond38
cond38(yes)->sub47
sub47->op49
op49(left)->cond38
cond38(no)->cond54
cond54->cond5
```

**step3:** change language type into flow

```flow
st=>start: Start
op=>operation: Your Operation
cond=>condition: Yes or No?
e=>end

st->op->cond
cond(yes)->e
cond(no)->op
```



## 4. Strings

```python
#signle quotation/ double quotation
#Escape character
# \" double quotation, \' single quotation, 
#\n create a new line,the cursor move to the head of new line
# \\ back slash        \t tab key,auto-indents 
print(r"D:\Course")  # means remov escape character
a = "hello world"
print(len(a))
```



```python
#replace
a =  'I\'m perfect good,good,good,enough'
b = a.replace('good','perfect',2) 
#replace(old,new,count) the third parameter is an optional parameter
#it indicates how many times it changes

#
#split(obj)
d = '00001_01_01_109.png '
c = d.split('_')   # change string type into list

#join(list), connect the list into string
e = '\\'.join(c)
print(c,e)
```



```python
f ='helloworld      '
print(f.rstrip())
#startswith()   #isalpha
#Judge the beginning or end:startswith，endswith
#isalnum contain 0-9 letter，upper,lower，swapcase,
#capitalize,isnumeric,isalpha,rstrip :delete trail space
```



```python
#Format character, insert variable in string
today = 9.23
tomorrow =  '9.24'
print("today is %.3f ,tomorrow is %s"%(today,tomorrow))
#   %s-  string, %i- int ,%f-  float ,%e- scientific counting method   
print("{} is perfect".format('Daniel'))
print("{0},{2},{1} is perfect".format('Daniel','David','Julina'))
```



pratice:

-  what is the output ：33+"22"; 33+int("22"); "22" + str(55);
-  m=“a,b,c”,m.split() what will happen？（without ","）
-  what is the output type of .split and .join 
-  If I need to output %f, how to do？
-  print("abc%s") % "nn"  #print("abc%s" % "nn")
-  print(245%f % 123)  # '245%f'%123
-  How to change the filename from   00001_01_01_109.png  into   00001_01_01/109.png

Lesson-review:

 3keywords, break\Continue\pass

string:split\join 000002_03_01

## 5. Functions

### 5.1 Basic concept of functions

In the process of programming, the repeated statements can be extracted and written as functions, which makes the program structure clear and easier to maintain.

- Basic function

```python
def functionName(params): #colon must be written
    block                 # function body
    return  value/expression #return is optional,return statement exit the function and get a expression. If a function donot have return statement,it will return None, that means return None/return
```

- return statement

```python
def f1(x):
    y = 2 ** x
def f2(x):
    y = 2 ** x
    return y
print(f1(2))
print(f2(2))
```

- parameter

```python
def hello(name,age):
    print(name+" is "+str(age)+" years old")
hello("Jack",18)

#default parameters
def hello(name, age= 18):
    print(name+" is "+str(age)+" years old")
hello("Jack",19) 

#practice
def mult(x, y= 2):
    return x*y
mult(2,3)
mult(2) #default parameters is 2, if you do not give a new value, 2 will previal

#variable parameters:If there are serveral parameters 
#or the number is uncertain,we can use * instead
def f(*x):
    print(x)
    return x  #tuple
f("2","2",["abc","def"])
```



```python
# Guessing numbers: The requirements are as follows：
# Randomly generate an integer in 0-100
# Guess a number and enter it,Judge whether it is big or small until you guess correctly
import random
import math
y = random.random()*100  #0-100
z = math.ceil(y)    #int type
def Guess():
    while True:
        x = int(input("please input your number x = "))
        if x ==z:
            print("Right")
            break
        else:
            if x > z:
                print("Too big")
            else:
                print("Too small")
    print("Congratulation")
Guess()
```

### 5.2 Local and global variables

variables define inside of function is local variables, it has local  scope. variables define outside of function is global variables, it has global scope. local variables can be only used inside of a function, while  global variables can be accessed throughout the program

```python
a = "abc"  #global
def f(x):
    global a  #global
    a = "hello everyone" #local
    print("local variables in function %s"%m)
f(a)
print(a)


#1Fibonacci sequence is a sequence like this：[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55....]
#That means F[a] = F[a-1] + F[a-2], Try to get the top 5 values in Fibonacci sequence 
#F0 = 0     (n=0)    #F1 = 1    (n=1)      #Fn = F[n-1]+ F[n-2](n=>2)
def fib(n):
    if n==1:
        return [1]
    if n==2:
        return [1,1]
    fibs = [1,1]
    for i in range(2,n):
        fibs.append(fibs[-1]+fibs[-2])
    return fibs
print(fib(5))

#Answer 2：
def fib(n):
    a,b =1,1
    for i in range(n-1):
        a,b = b,a+b
    return a
for i in range(1,8):   
    print(fib(i))
#Answer 3：Recursive function
def fib(n):
    if n==1 or n==2:
        return 1
    return fib(n-1)+fib(n-2)
print (fib(10))
```

### 5.3 Anonymous function( lambda )

```python
def fun(a,b,c):
    return a+b+c
print(fun(1,2,3))
#lambda expression / Anonymous function
f = lambda a,b,c:a+b+c 
#lambda is not requie function name, the body of lambda is an expression
#It only has one line, only the limited logic can be written in lambda expression
print(f(1,2,3))
```



practice:

①Create an anonymous function to find the number of elements 

```python
list1 = [1,2,3,45,7,89,0] #7    length
f1 = lambda lst:len(lst)
f1(list1)
```

② Define a function to sort all input numbers from large to small

```python
# sort   sorted
f2 = lambda lst:sorted(lst,reverse=True)
f2(list1)
```



### 5.4 Others

#### 5.4.1 Common built-in functions

```python
list1 = [1,2,3,45,7,89,0]
help(abs)  #
abs(-1) #Return the absolute value of the argument.
print(max(list1),min(list1),sum(list1))
sorted(list1) # 
len(list1)
round(3.1415926,4) #get the float number in fixed length
divmod(12,3) #return the division and remainer  (x//y, x%y) 
```

#### 5.4.2 Line function

 Line function is also called list parsing or list comprehension，the structure is as followed:

```
[expression1 for k in if expression2]
```

```python
#line function  [expression1 for k in if expression2]
list2 = [1,2,3,4,5]
a = [k+2 for k in list2 if k%2==0]
print(a)
[(x,y) for x in range(3) for y in range(3)] #more limitation
```

#### 5.4.3 filter

filter(function(),s) 

```python
#filter get each of element in list and assign to function, 
#it can be used to filter list then return the result as a new list
def is_odd(n):
    return n%2 ==1
list(filter(is_odd,[1,2,4,5,6,9,15]))
```

#### 5.4.4 Map

Map get each of element in list and assign to function,  And then return the result as a new list

```python
def is_odd(n):
    return n%2 ==1
list(map(is_odd,[1,2,4,5,6,9,15]))
```

map return the result, however filter get out data for scope

####  5.4.5 reduce

```
reduce(f,[x1,x2,x3,x3]) =f(f(f(x1,x2),x3) ,x4)
```

```python
from functools import reduce
def add(x,y):
    return x+y
reduce(add,[1,2,3,4]) # add(1,2) = add(3,3) = add(6,4)
```



pratice:

```python
#Q1：In 1, 2, 3 and 4 . How many different two digits can be formed without repeated numbers, like 12\23\13\34...? How much is it?

#Q2:Input three integer x, y and Z. please output these three numbers from small to large. 
#limitation:You need to  use input\isdigit function. (judge whether the input data is a number)
```



## 6. Object Oriented Programming Foundation 

Object Oriented Programming(OOP) is a programming method through defining functions to simulate the real world. OOP can control data in a reasonable and automatic way, reducing code bug, reducing code quantity,  and easier to maintain.

### 6.1 Define a class

We can use classes to define and represent models with the **same** **attributes** and **capabilities**, the structure is as followed:

```python
class <ClassName>:
```

We call  **attributes** as property/attribute and **capabilities** are method/function.  for example,  a person has properties like height, age, name, and he can run/eat/smile.

The methods in the class are basically the same as the functions in lesson 5. But there are some differences：

1. The first parameter of the method must be ’self ‘，and cannot be omitted(when we use method we do not need to provide the self parameter)；
2. Method calls need to instantiate a class.  And in the form of instance name. method name (parameter list);
3. The overall indentation indicates the content belonging to the class.

```python
class MyClass:
    def info(self):
        print('The class I defined')
    def mycalc(self,x,y):
        return x+y
mc = MyClass()
mc.info()
print(mc.mycalc(3,5))
```

#### 6.1.1 Class Properties

There are two types of properties：

- Instance properties ：Different instances values  of the same class are not associated，'self. attribute name' is used when defining and when calling.
- Class properties ：common to all instances

```python
class Demo_property:
    class_name = "Demo_property"     #Class properties,as long as an instance modifies it, it will affect all other instances
    def __init__(self,x=0):          #__init__ is a special function, we can call it init function/constructor. When a instance is created, it will be called automaticlly
        self.x = x                   #Instance properties，it will not affect others
    def info(self):
        print(Demo_property.class_name) #Class properties value
        print(self.x)                   #Instance properties value
    def change1(self,x):
        self.x = x
    def change2(self,name):
        Demo_property.class_name = name
    def change3(cls):
    	print('change3 %s'%cls.bar)
    	cls().info()    #call info function
dpa = Demo_property()
dpb = Demo_property()
dpa.info()
dpa.change2("3")
dpa.info()
```

- Python built-in class properties

  - __ name__ is  class name
  - __ module__ is  class module

  - __ dict__  is  class properties

```python
class Demo_property:
    class_name = "Demo_property"     #Class properties,as long as an instance modifies it, it will affect all other instances
    def __init__(self,x=0):          #__init__ is a special function, we can call it init function/constructor. When a instance is created, it will be called automaticlly
        self.x = x                   #Instance properties，it will not affect others
    def info(self):
        print(Demo_property.class_name) #Class properties value
        print(self.x)                   #Instance properties value
    def change1(self,x):
        self.x = x
    def change2(self,name):
        Demo_property.class_name = name
    def change3(cls):
        print('change3 %s'%cls.bar)
        cls().info()    #call info function
print(Demo_property.__name__)          #
print(Demo_property.__module__)
print(Demo_property.__dict__ )
```

practice：

1. What is the following code output,why

```python
class People(object):
   def __init__(self):
       print("__init__")
   def __new__(cls, *args, **kwargs):   #__ new__ () usually returns an instance of this class,   change name to new1 
       print("__new__")
       return object.__new__(cls, *args, **kwargs)
People()
```

2. supplementary code to performs the following methods class_foo/static_foo

```python
class A(object):
   def foo(self, x):
       print("executing foo(%s, %s)" % (self,x))
   @classmethod
   def class_foo(cls, x):
       print("executing class_foo(%s, %s)" % (cls,x))
   @staticmethod
   def static_foo(x):
       print("executing static_foo(%s)" % (x))
a = A()
a.class_foo('data1')  #result：executing class_foo(<class '__main__.A'>, data1)
A.class_foo('data2')  #result：executing class_foo(<class '__main__.A'>, data2)
```

3. Write a Student Class that requires counter attribute . It can count the total number of students instantiated

```python
class Student:
    count = 0
    @classmethod
    def __init__(cls):
        cls.count += 1
a1 = Student()
a2 = Student()
a3 = Student()
a4 = Student()
print(Student.count)
```



#### 6.1.2 Extends

Subclasses cannot inherit private properties and private methods of the parent class（Prefixed with two underlines）， Subclasses can overload the methods of the parent class , it can  achieve different  representations or capabilities of the parent class. 

```python
class Dog:
    def __init__(self,x=0,y=0,color='yellow'):  #constructor
        self.x = x
        self.y = y
        self.color = color
    def crawl(self,x,y):
        self.y = y 
        print('The current position:(%d,%d)' % (self.x,self.y))
    def attack(self):
        print('Use teetch')
class Haski(Dog):                         #Extends
    def attack(self):                     #Method overloading
        print('Use teetch and Smile')
haski = Haski(color='white')
haski.crawl(3,8)
haski.attack()
```

Multiple inheritance ：class Sub(Dog, Haski)

#### 6.1.3 Member methods and static methods

- Instance method, All previous class methods are instance methods
- Class method，It can be called directly by the class name or by an instance.  annotation @classmethod
- **classmethod** functions do not need to be instantiated，do not need self . However, the first parameter needs to be the cls , representing its own class, which can call the properties, methods and instantiated objects. 

```python
class Demo_property:
    class_name = "Demo_property"     #Class properties,as long as an instance modifies it, it will affect all other instances
    def __init__(self,x=0):
        self.x = x                   #Instance properties，it will not affect others
    def info(self):
        print(Demo_property.class_name) #Class properties value
        print(self.x)                   #Instance properties value
    def change1(self,x):
        self.x = x
    def change2(self,name):
        Demo_property.class_name = name
    @classmethod
    def change3(cls):
        print('change3 %s'%cls.class_name)
        cls().info()    #call info function
Demo_property.change3()
```



- Static method，It can be called directly by the class name @staticmethod
- This method does not force parameters to be passed

```python
class Demo_property:
    class_name = "Demo_property"     #Class properties,as long as an instance modifies it, it will affect all other instances
    def __init__(self,x=0):
        self.x = x                   #Instance properties，it will not affect others
    def info(self):
        print(Demo_property.class_name) #Class properties value
        print(self.x)                   #Instance properties value
    def change1(self,x):
        self.x = x
    def change2(self,name):
        Demo_property.class_name = name
    @staticmethod
    def change3(arg1):
        print('change3 %s'%arg1)
        
Demo_property.change3('hello')
```

practice：

1. What is the following code output,why

```python
class Parent(object):
  	x = 1
class Child1(Parent):
    pass
class Child2(Parent):
    pass
print(Parent.x, Child1.x, Child2.x) 
Child1.x = 2
print(Parent.x, Child1.x, Child2.x)
Parent.x = 3
print(Parent.x, Child1.x, Child2.x)
```



### 6.2 Module creation and introduction

- When the program is simple,we can write the code in a file
- When the code is too long or too large, you need to put the project into different files according to function.  Different code files are different modules（Each py file is a module）
- When the  code complexity get increased, you need to put different codes into different folders, and they can refer to each other, that is package.

Module is a python file end with .py，it contains Python object definitions and statements

```python
def f1(n):
    y = 1
    for i in range(1,n+1):
        y = y * i
    return y
# Create factorial function f1(n)

def f2(lst,x):
    while x in lst:
        lst.remove(x)
    return lst
# Create a function can delete element in list,  f2(lst,x)

def f3(a,d,n):
    an = a
    s = 0
    for i in range(n-1):
        an = an + d
        s = s + an
    return s
# Create a summation function f3(a,d,n)
# Create a module 'testmodel2'，it include three functions
```

- Call module

```python
import testmodel2
# Call the module directly with import   print(testmodel2.f1(5))   
print(testmodel2.f2([2,3,4,5,5,5,6,6,4,4,4,4],4))
print(testmodel2.f3(10,2,10))

```

Simplified module name ：import...as..(import testmodel2 as tm2)

Call some module statements ：From…import (Some functions of modules are imported separately, but other functions are not imported)

```python
# python standard module —— random number
import random
x = random.random()
y = random.random()
print(x,y*10)
# random.random() [0:1) 
m = random.randint(0,10)
print(m)
# random.randint()  [0:10] 
st1 = random.choice(list(range(10)))
st2 = random.choice('abcdnehgjla')
print(st1,st2)
# random.choice() Randomly get an element in (), which must be an ordered type
lst = list(range(20))
sli = random.sample(lst,5)
print(sli)
# random.sample(a,b)   Randomly obtain a fragment with the of b in a, without changing the original sequence
lst = [1,3,5,7,9,11,13]
random.shuffle(lst)
print(lst)
# random.shuffle(list)Scramble elements in a list
```

### 6.3 Package

A package is a folder or directory ，it must contain a  _init _.py file，However, any part of the import package will execute the file, and the variables and functions will be imported automatically

### 6.4 Closure function

- Closure is the object obtained by packaging the function  statements and the execution environment of these statements. 
- Using closures can flexibly implement other functions that are not easy to implement in syntax

Practice： change image to text file

```python
#!/usr/bin/env python
# coding: utf-8

import numpy as np
from PIL import Image

if __name__ == '__main__':
    image_file = '3.jpg'
    height = 100#change image height to 100

    img = Image.open(image_file)
    img_width, img_height = img.size
    width = 2 * height * img_width // img_height    
    img = img.resize((width, height), Image.ANTIALIAS)#change image size
    pixels = np.array(img.convert('L')) 
    print(pixels.shape)
    print(pixels)
    chars = "MNHQ$OC?7>!:-;. " #256 color,M means 0-15，N means 16-31
    N = len(chars)
    step = 256 // N
    print(N)
    result = ''
    for i in range(height):
        for j in range(width):
            result += chars[pixels[i][j] // step]                          
        result += '\n'
    with open('text.txt', mode='w') as f:
        f.write(result)
```



## 7. File and Exception

excel /CSV/txt

### 7.1 Document declaration and basic operation

```python
import os   #operating system
#    \t    escape character
path1 = r"C:\Users\everi\Desktop\Code\Python\Py2021"         #We use r to prevent character escape
path2 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021"    #2 back slashes \\
path3 = os.path.dirname(os.path.abspath('__file__'))          #directory 
print(path3)
```

- read / write something in the txt file

```python
path4 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\hello.txt"    #2 back slashes \\
f = open(path4, 'r')  #mode:  r means read, w means write,  encoding ='utf8'
#print(type(f))
#print(f)
print(f.read())#output the content, after this cursor is in the end of file 
print("reading completed")
f.seek(0)  #move the cursor to the begining of the file
print(f.read())
f.close()  #close the IO operation
```



### 7.2 System module path 

```python
import os   #operating system
path5 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021"         #directory 
#print(os.name)  #nt means windows, Linux/unix 'posix'
#print(os.listdir())  #file and directory name
#print(os.getcwd())  #current work directory
#os.remove('a.txt')
print(path5)
os.chdir(r'C:\Users\everi\Desktop\Code\Python')  #change the directory to a target directory
print(os.getcwd())  #current work directory
print(os.path.exists(r"C:\Users\everi\Desktop\Code\Python\Py2021\hello.txt")) 
print(os.path.split(r"C:\Users\everi\Desktop\Code\Python\Py2021\hello.txt"))
# return the directory name,and file name
```

### 7.3 Files reading and writing 

-  Files reading
   -  read()  output the content, after this cursor is in the end of file
   -  readlines()  get the content line by line

```python
#File reading 
path6 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\hello.txt" #2 back slashes \\
f = open(path6, 'r')  #mode:  r means read, w means write,  encoding ='utf8'
f.seek(0)
#print(f.readline(4))  #first 4 characters of a line
#print(f.readlines())
for line in f.readlines():
    print(type(line),line)
```

-  Files writing 
   -  write()  write string into the file
   -  writelines()  list into the file 

```python
#File writing 
path7 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\test.txt"    #2 back slashes \\
#create an empty file 'test.txt',and add the content "hello world" inside of it
f = open(path7, 'w',encoding ='utf8')  #change the mode
f.write("hello world")
f.close() #close writing operation
print("finished")
```



```python
path8 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\test.txt"   
f = open(path8, 'w',encoding ='utf8')  
lst = ['a','b','c','d','e']
f.writelines(lst)
f.close() #close writing operation
print("finished")
```

practice:

1. write a file. the style is line by line. 

    ['a\n','b\n','c\n','d\n','e\n'] this kind is a little complex, we can use for loop to write the content line by line

```python
path9 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\test.txt"   
f = open(path9, 'w',encoding ='utf8')  
lst = ['a','b','c','d','e','f'] 
for i in range(len(lst)):  #0 to 4
    lst[i] = lst[i]+'\n'  # change style from ['a','b','c','d','e']  to ['a\n','b\n','c\n','d\n','e\n']  
f.writelines(lst)
f.close() #close writing operation
print("finished")
```

2. There are 2 list [1 to 10 ], [a to j]. Please write a out.txt file to make the content format like this:

```
1,a
2,b
3,c
.....
10,j
```

```python
path10 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\out.txt"   
f = open(path10, 'w',encoding ='utf8')  
lst1 =  list(range(1,11))  #
lst2 =  ['a','b','c','d','e','f','g','h','i','j']
for i in range(len(lst1)):  #10 elements
    out = [str(lst1[i]),',',lst2[i],'\n'] 
    f.writelines(out)
f.close() #close writing operation
print("finished")
```

- with statement

With statement can ensure the clear up IO operation, it will automatically close the IO operation

```python
os.chdir(r'C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\')  #change the directory to a target directory
with open('test.txt') as file:
    data = file.read()
    print(data)  #automaticlly close the IO operation
#style 2
try:
    f = open()
except:
    exit(-1)
finally:
    f.close()
```

### 7.4 pickle

- store

```python
import pickle
data = {'a':[1,2,3,4],'b':('hello','world'),'c':'word'}
path11 = "C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\data.pkl"   
f = open(path11, 'wb') #mode: w  wb  , write binary
pickle.dump(data,f)
f.close()
#dump
```

- read

```python
#load function
f = open(path11, 'rb') #mode:rb   read binary
st = pickle.load(f)
print(st)
print('finished')
```

## Project:Lesson-8

```python
'''
【Project 1】  Shop data loading and storage

Requirment：
1、read csv file “shop1.csv”
2、Data cleaning：
① cleaning comment and price into number style:
	
② commentlist can be splited into three float fields，return [flavor,environment,service]

③ Clear missing data
3、Parse data，Save as list dictionary format[{'var1':value1,'var2':value2,'var3':values,...},...,{}]
    [{'classify': 'food', 'name': 'HARSON', 'comment': 'No  comments', 'star': 'no star', 'price': 125},
    {'classify': 'food', 'name': 'BeLLE', 'comment': '74', 'star': 'four star', 'price': 48},
    {'classify': 'food', 'name': 'achette', 'comment': '265', 'star': 'four star', 'price': 21},
    ......
    ]
4、Store the new data into data.pkl file.

'''
```



```python
#Step1. Open the file, and get all the columns information
f= open(r'C:\Users\everi\Desktop\shop1.csv','r',encoding='gbk')
for i in f.readlines()[:5]:
     print(i.split(',')[2]) # 5/-1 commentlist information ,star 
#     print(i.split(',')) #top 4 lines , all the data information
#cursor return to the first line

```



```python
#Step2 :cleaning comment into number style
def fcm(s):
    if 'comments' in s:
        return s.split('                    ')[0] #[400 ,comments]
    else:
        return ('ABCNo comments')
#cleaning price into number style    # [average-spend,291]
def fpr(s):
    if '￥' in s: #291
        return s.split('￥')[-1]
    else:
        return ('ABCNo  average-spend ')
#cleaning commentlist information
def fco(s):
    if len(s)==3:
#         flavor, environment,service=  s[0],s[1],s[2]
#         production = float(s[0][6:]) #flavor is not the correct, there are other types
        environment = float(s[1][11:])
        service = float(s[2][7:])
        return [environment,service]  #['flavor8.3', 'environment8.4', 'service8.5\n']
    else:
        return ('ABCNo commentlist')
f.seek(0)
for i in f.readlines()[:5]:
    cm = fcm(i.split(',')[2])
    pr = fpr(i.split(',')[4])
    co = fco(i.split(',')[-1].split('                                '))
    print(co) 
```



```python
#Step3 Clear missing data,Parse data，Save as list dictionary format
datalist = []
sum = 0
f.seek(0)
for i in f.readlines()[1:]:  #all the data in csv file, 1264 items
    data = i.split(',')
    classify,name,comment = data[0],data[1],fcm(data[2])
    star,price = data[3],fpr(data[4])
    commentlist = fco(i.split(',')[-1].split('                                '))
    environment = commentlist[0]
    service = commentlist[1]
    if 'ABC' not in [comment,price,commentlist]:
        sum += 1
        #write sth
        new_data = [
            ["classify",classify],
            ["name",name],
            ["comment",comment],
            ["star",star],["price",price],["environment",environment],
            ["service",service]
        ]
        datalist.append(dict(new_data))
    else:
        continue
print(datalist)
print(sum)
```



```python
# Step4:Store the new data into data.pkl file.
import pickle
f= open(r'C:\Users\everi\Desktop\data.pkl','wb')
pickle.dump(datalist,f) #store
f.close()
f= open(r'C:\Users\everi\Desktop\data.pkl','rb') #read binary
st = pickle.load(f)
print(st)
```



## 8. Common packages



![package](D:/Course/Python/PythonDoc/image/package.png)

https://pypi.org/

### 8.1 Numpy

​	 Numpy is the basic python programming library .  It provides advanced mathematical operations, it also has a very efficient vector matrix operation function 。

#### 8.1.1 Random number

```python
import numpy as np
#rand(d0,d1,d2....dn)  generate a random number or an n dimensions array, 
#all the element value is between[0,1] 
a = np.random.rand()  #float number ,between [0,1]
b = np.random.rand(4)  # 1 dimension, Array with 4 elements
c = np.random.rand(2,3)# 2 dimensions with 2 rows and 3columns
d = np.random.rand(2,3,4)#3 dimensions 
print(d)
```



```python
samples1 = np.random.rand(1000) #uniformly distributed sample value
samples2 = np.random.rand(1000)
#print(samples1)
import matplotlib.pyplot as plt
plt.scatter(samples1,samples2)
```



```python
#randint(size)
print(np.random.randint(3)) # from 0 to 2, but 0 is ok 2 is not included
print(np.random.randint(3, size=5))
print(np.random.randint(2,6, size=5)) #low =2, high = 6(not included),  5 element
print(np.random.randint(2,6, size=(2,3)))    #2 dimensions array, with 2 rows and 3columns
```

#### 8.1.2 Basic

```python
# ar = np.array(range(10))
# lst1 = list(range(10))
# print(ar) #array is similar with list. but list has comma
# print(lst1)
ar1 = np.array([1,2,3,4,5.5, 6.3,7,8.9]) #float
ar2 = np.array([[1,2,3],["a","b","c"]])  #2-D array
ar3 = np.array([[1,2,3],["a","b","c","d"]])  #elements number is different
print(ar2.shape) #(2, 3)  2 rows  and 3 cols
print(ar2.size)  # total number 2*3 elements = 6
print(ar1.dtype) # dtype is similar with type, type is a function, dtype is property
print(type(ar1))
```

- linspace

```python
#linspace(start,stop,num=50,endpoint=True,dtype = None) return evenly space sample
ar1 = np.linspace(2,3,num=5,endpoint=False)
#endpoint=False means stop value is not included
print(ar1)
```

- zeros/zeros_like / ones/ones_like

```python
#zeros(shape,dtype= float),return a zero array of given shape and type
ar1 = np.zeros(5)
ar2 = np.zeros((2,3), dtype = np.int)
print(ar2.dtype)

#zeros_like
ar3= np.array([list(range(5)),list(range(5,10))])  #2d  array
ar4 = np.zeros_like(ar3)
print(ar4)
#ones and ones_like
ar5 = np.ones(9)
ar6 = np.ones_like(ar3)
print(ar6)
```

- eye

```python
#eye return a square unit matrix
print(np.eye(5))
```



Practice： 

1. Create an Array that starts with 5 and end with 14, 10 elements in this array. like:[ 5  6  7  8  9 10 11 12 13 14]

```

```

2. Create an Array

```python
[[0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]
 [0. 0. 0. 0.]]    2d  zeros
 -------------------------------------------------------
 [[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]  3d
  ------------------------------------------------------
 [[1. 0. 0.]
 [0. 1. 0.]
 [0. 0. 1.]]       2d
```

#### 

#### 8.1.3 General function

```python
# Transpose
ar1 = np.arange(10)  
ar2 = np.zeros((5,2)) #Transpose change the shape (5,2) to (2,5)
print(ar2, '\n',ar2.T)
print("-------------------Transpose---------------------------")
ar3 = ar1.reshape(2,5)  #1.chang the existing array into another shape
ar4 = np.zeros((4,6)).reshape(3,8) #2.create a new array and directly change into new shape
ar5 = np.reshape(np.arange(10),(2,5)) #3 change the initial array into target shape
print(ar5)
print("----------------------reshape-------------------------")
# resize
ar6 = np.resize(ar1,(3,5))
print(ar6)
#Transpose\reshape\resize  all of these 3 function will create new array
```

- copy array

```python
ar1 = np.arange(10)  
ar2 = ar1 #should not copy the array directly
#ar2[0] = 19
ar3 = ar1.copy() #generate a new array , the data and elements will completely copyed
ar3[0] = 19
print(ar1,ar3) 
```

-  calculation

```python
ar = np.arange(6).reshape((2,3))
#print(ar**2) #+ - *  / ** power
#print(ar.max())  #mean= average value, max, min,sum
print(ar)
print(np.sum(ar,axis =1))  #0 means calculate the sum by columns
print(np.sort(np.array([1,4,2,3,7,100,8])))
```



Practice： 

```python
1.create an array:
a = [[0 1 2 3]
 [4 5 6 7]
 [8 9 10 11]
 [12 13 14 15]] 
-------------------------------------------------
ar1 = np.reshape(np.arange(16), (4,4))
print(ar1)
2.create b each element value b[i][j] = a[i][j] * 10 +100，
b = [[100 110 ...]
...
 [220 230 ...]] 
 ----------------------------------------
 # #practice
# ar1 = np. arange(16)
# ar6 = np.resize(ar1,(4,4))
# ar7 = ar6*10+100
# print(ar7)
3.calculate the average value and sum/min/max--  average pooling /max pooling
4.create an array with 20 element, resize it into (4,5), or (5,6)
[[0 1 2 3 4]
 [5 6 7 8 9]
 [10 11 12 13 14 ]
 [15...19]] 
 ------------------------------------
 arr = np.arange(20)
print(np.resize(arr, (4, 5)))
print(np.resize(arr, (5, 6)))
```

#### 

#### 8.1.4 Numpy index and slice

```python
ar = np.arange(16).reshape(2,4,2)
#print(ar[0]) #the 1st element in 3d array -----2d
print(ar[0][0]) #1d array 
print(ar[0][0][0]) # value
ar = np.arange(20)
print(ar)
print(ar[4])
print(ar[3:6])
print('-----')
# 1D

ar = np.arange(16).reshape(4,4)
print(ar[2][1]) # Gets a value in a one-dimensional array
print(ar[2,2])  # Third Row, third column→ 10
print(ar[:2,1:])  # 1,2Row、2,3,4 column → 2d ARRAY
print('-----')
# 2D

ar = np.arange(8).reshape(2,2,2)
print(ar)   # 2*2*2
print(ar[0])  # The 1th element in 3d array → 2d
print(ar[0][0])  
print(ar[0][0][1])  #value
```

- change value

```
ar = np.arange(10)
print(ar)
ar[5] = 100
ar[7:9] = 200
print(ar)
```



### 8.2 Pandas

Pandas ：Use python like excel

- Compatible with database/ Analysis algorithm

- "1D array "Serise， "2D array "Dataframe  

#### 8.2.1 Series

- Series is a 1D array with labels that can hold any data type

- Create Series

```python
#Series:1D array+ index
# 1.Series can be created by the dict. The key of the dict is index
dic = {'a':1,'b':2,'c':3,'4':4,'5':5}
s = pd.Series(dic)  #keyword 
print(s,s['a'])
print(s[['a','c']])  #multi label index has 2 bracket
```



```python
# 2.Series can be created by array
arr = np.random.rand(5)
#s = pd.Series(arr)
s = pd.Series(arr,index=["a","b","c","d","e"],dtype = np.object)
print(arr,'\n',s)
```



```python
# 3.Series can be created by scalar /number
s = pd.Series(10,index=range(4)) #index must be provided
print(s)
```

- data operation

```python
arr = np.random.rand(5)
s = pd.Series(arr,index=["a","b","c","d","e"],dtype = np.object)
print(s,'\n','-----------------')
#print(s[1:3]) #slicing
#print(s.head(2),s.tail()) #top /tail 5 line
#print(s[s>0.5]) #filter / value judgement
print(s.isnull(), s.notnull()) # value judgement
```



- Practice : 

  >  1.Create a Series(name is s1) that contains 10 elements, each with a uniformly distributed random value of 0-100 and an index of a-j. 
  >
  >  2. please filter b，c value out in s1 
  >  3. What are the 4th to 6th values in s1 
  >  4. What are values greater than 50 in s1

```python
s1 = pd.Series(np.random.rand(10)*100,index=list("abcdefghij"))
print(s1[s1>50]) #s1[["b","c"]],s[3:6]
```



- Series alignment

In series, all the elements will add together automatically aligned according to labels

```python
s1 = pd.Series(np.random.rand(3),index=["a","b","c"])
s2 = pd.Series(np.random.rand(3),index=["b","c","d"])
print(s1,"\n",s2)
print(s1+s2)
```

- delete：.drop

```python
s1 = pd.Series(np.random.rand(3),index=["a","b","c"])
s2 = s1.drop(['a','c'])  #tab +shift  inplace = True
print(s2)
```

- Add

```python
s1 = pd.Series(np.random.rand(3),index=["a","b","c"])
s1[0] = 100 #change value
s1['d'] = 99  #add element
s2 = pd.Series(np.random.rand(3),index=["e","f","g"])
s3 = s1.append(s2) #append add an array directly, do not change the previous array
print(s3)
```

- concat

```python
# concat
s1 = pd.Series([1,2,3],index=["a",'c','b'])
s2 = pd.Series([2,3,4],index=['e','f',"d"])
#print(pd.concat([s1,s2])) #row +row
print(pd.concat([s1,s2],axis=1).sort_index()) #Dataframe

# join，join_axes
s1 = pd.Series([1,2,3],index=["a",'b',"c"])
s2 = pd.Series([2,3,4],index=['b','c',"d"])
print(pd.concat([s1,s2],axis=1,join = "outer")) 
#"inner is intersection without NAN, outer is the union
```



#### 8.2.2 Dataframe

Dataframe is a tabular data structure that contains a set of ordered columns whose value types can be numeric, string, Boolean, etc

- create

```python
# 1 Dataframe can be created by dict(array /list)
data1 = {"a":[1,2,3],"b":[4,5,6],"c":[7,8,9]}
data2 = {"one":np.random.rand(3),"two":np.random.rand(3)}
pd.DataFrame(data1,columns=["c","a","b","d"],index = ["e","f","g"])
# 2 Dataframe can be created by Series dict
data1 = {"one":pd.Series(np.random.rand(2)),
         "two":pd.Series(np.random.rand(3))} #without index
data2 = {"one":pd.Series(np.random.rand(2),index = ["a","b"]),
         "two":pd.Series(np.random.rand(2),index = ["c","d"])}
pd.DataFrame(data2)
# 3 Dataframe can be created by 2d array
ar = np.random.rand(9).reshape(3,3)
pd.DataFrame(ar)
# 4 Dataframe can be created by array[dict]
data1 = [{"a":1,"b":2},{"a":5,"b":6,"c":8}]
pd.DataFrame(data1)
```

- Practice:Use four different methods to create a dataframe (ensure that columns and index are consistent, and the value is not required)

  > ```
  >  four  one  three  two
  > a     4    1      3    2
  > b     5    2      4    3
  > c     6    3      5    4
  > d     7    4      6    5
  > e     8    5      7    6
  > ```

```python
df1 = pd.DataFrame({'one':[1,2,3,4,5],
                   'two':[2,3,4,5,6],
                   'three':[3,4,5,6,7],
                   'four':[4,5,6,7,8]},
                  index = list('abcde'))
df2 = pd.DataFrame({'one':pd.Series([1,2,3,4,5],index = list('abcde')),
                   'two':pd.Series([2,3,4,5,6],index = list('abcde')),
                   'three':pd.Series([3,4,5,6,7],index = list('abcde')),
                   'four':pd.Series([4,5,6,7,8],index = list('abcde'))})
df3 = pd.DataFrame(np.arange(20).reshape(5,4), 
                   index = list('abcde'),
                  columns = ['one','two','three','four'])
df4 = pd.DataFrame([{'one':1,'two':2,'three':3,'four':4},
                   {'one':2,'two':3,'three':4,'four':5},
                   {'one':3,'two':4,'three':5,'four':6},
                   {'one':4,'two':5,'three':6,'four':7},
                   {'one':5,'two':6,'three':7,'four':8}],

```



- Dataframe：index

  Dataframe has both row and column indexes



- df.iloc







Practice : 

> 1.  Create a dataframe (4row * 4 cols, random number with value of 0-100)
> 2.  Gets all the values of in 2th and 3th columns 
> 3.  Gets all the values of in 2th and 3th rowa
> 4.  Gets all value greater than 50

#### 8.2.3 numerical calculation and statistics

```
# axis、skipna
import numpy as np
import pandas as pd
df = pd.DataFrame({'key1':[4,5,3,np.nan,2],# np.nan ：Null value
                 'key2':[1,2,np.nan,4,5],
                 'key3':[1,2,3,'j','k']},
                 index = ['a','b','c','d','e'])
print(df['key1'].dtype,df['key2'].dtype,df['key3'].dtype)
print('-----')

m1 = df.mean()# .mean()Calculate the mean, only number can be calculated
print(m1,type(m1))
print(df['key2'].mean()) #statistics column
print('-----')

m2 = df.mean(axis=1)# default axis= 0，means calculating in columns，axis=1
print(m2)
print('-----')

m3 = df.mean(skipna=False) # skipna ignore Nan ，default True
print(m3)
print('-----')
```



```
print(df.count(),'→ count Na number\n')
print(df.min(),'→ min\n',df['key2'].max(),'→ max\n')
print(df.quantile(q=0.75),'→ quantile\n')
print(df.sum(),'→ sum\n')
print(df.mean(),'→ mean\n')
print(df.median(),'→ median，50%\n')
print(df.std(),'\n',df.var(),'→ std,var\n')
print(df.skew(),'→ skew\n')
print(df.kurt(),'→ kurt\n')
```



#### 8.2.4 File operation

read_table, read_csv, read_excel

```python
#read txt file
import pandas as pd
import numpy as np
import os
os.chdir('C:\\Users\\everi\\Desktop\\')
data1 = pd.read_table('data1.txt')
print(data1)
```

Generate descriptive statistics.Descriptive statistics include those that summarize the central tendency, dispersion and shape of a dataset's distribution, excluding ``NaN`` values.Analyzes both numeric and object series, as well as ``DataFrame`` column sets of mixed data types. The output will vary depending on what is provided. 

```python
data2 = pd.read_csv('train.csv') #read_excel
#data2.head(6)
data2.describe() #shift+tab
```

> DataFrame.count: Count number of non-NA/null observations.
> DataFrame.max: Maximum of the values in the object.
> DataFrame.min: Minimum of the values in the object.
> DataFrame.mean: Mean of the values.
> DataFrame.std: Standard deviation of the observations.
> DataFrame.select_dtypes: Subset of a DataFrame including/excluding
>  columns based on their dtype.

```PYTHON
#0 is still in the company,1 means the person leave the company/Attrition
neg_data = data2[data2['Attrition']==0] #DataFrame
pos_data = data2[data2['Attrition']==1]
print("Positive sample number:{},proportion{}"
      .format(len(pos_data),len(pos_data)/len(data2)))
print("Negative sample number:{},proportion{}"
      .format(len(neg_data),len(neg_data)/len(data2)))
print(len(pos_data)/len(data2)+len(neg_data)/len(data2))
```



### 8.3 Matplotlib

Matplotlib is a comprehensive library for creating static, animated, and interactive visualizations in Python.

```
https://matplotlib.org/stable/index.html
```

#### 8.3.1 Basic chart drawing

```python
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
x = [1,2,3,4,5]
y = [2.3,3.4,1.2,6.6,7.0]  #1 d data
plt.figure(figsize=(12,6)) #Figsize specifies the width and height(inches) of the figure object
#divide the picture into 2*3 small ones
plt.subplot(231) #231 means: the 1st chart in 2rows and 3cols figure
plt.plot(x,y)     #line chart
plt.subplot(232)
plt.scatter(x,y) #scatter chart, dot
plt.subplot(233)
plt.pie(y)      #pie chart
plt.subplot(234)
plt.bar(x,y)   #histogram
import numpy as np
x=y=np.arange(-3,3,0.025)
x,y = np.meshgrid(x,y) #chang 1d array into mesh (2d )
z = x**2 + y**2 # ** is power. 2**3 = 8,3**2 =9
plt.subplot(235)
plt.contour(x,y,z) #rectangular contour
import matplotlib.image as mpimg
img = mpimg.imread('image\\c9.jpg')
plt.subplot(236)
plt.imshow(img) 
```

<img src="D:/Course/Python/PythonDoc/image/Matplotlib1.png" alt="pig" style="zoom:80%;" />

- -1 can not display

```
plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False
```

#### 8.3.2  Magic function

```
#magic function 
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
# plt.plot(np.random.rand(10)) #generate the chart directly
# plt.show()
#inline: normal style  /notebook: interactive window/ qt5 : pop up console
%matplotlib qt5
plt.scatter(np.random.rand(1000),np.random.rand(1000)) 
```



#### 8.3.3 Basic elements of chart

```python
df = pd.DataFrame(np.random.rand(10,2),columns=['A','B'])
fig = df.plot(figsize=(6,4))
plt.title("Define the title") #title
plt.xlabel("Plot number")  #xlabel
plt.ylabel("Random value") #ylabel
plt.legend(loc='upper right') #position
plt.xlim([0,12]) #boundary of x axis
plt.ylim([0,1.5])
plt.xticks(range(10)) #set the scale
plt.yticks([0,0.2,0.4,0.6,0.8,1.0,1.2])
# fig.set_xticklabels("%.1f" %i for i in range(10)) #label
x boundary 0-12,x scale label 0-9 with 0.1 step
print(fig)
```

> ```
> # loc= location
> # 'best'         : 0, (only implemented for axes legends)
> # 'upper right'  : 1,
> # 'upper left'   : 2,
> # 'lower left'   : 3,
> # 'lower right'  : 4,
> # 'right'        : 5,
> # 'center left'  : 6,
> # 'center right' : 7,
> # 'lower center' : 8,
> # 'upper center' : 9,
> # 'center'       : 10,
> ```

- Visibility of other elements

> ```
> # linestyle：
> # color：
> # linewidth：
> # axis：x，y，both
> ```

- Style of chart：linestyle、style、color、marker

```python
x = [1,2,3,4,5]
y = [2.3,3.4,1.2,6.6,7.0]  #1 d data
plt.plot(x,y,linestyle='--')              #line chart
# '-'       solid line style
# '--'      dashed line style
# '-.'      dash-dot line style
# ':'       dotted line style
```



```python
# marker
df = pd.DataFrame(np.random.rand(20,2),columns=['A','B'])
df.plot(linestyle='--',marker ='v')  
# '.'       point marker
# ','       pixel marker
# 'o'       circle marker
# 'v'       triangle_down marker
# '^'       triangle_up marker
# '<'       triangle_left marker
# '>'       triangle_right marker
# '1'       tri_down marker
# '2'       tri_up marker
# '3'       tri_left marker
# '4'       tri_right marker
# 's'       square marker
# 'p'       pentagon marker
# '*'       star marker
# 'h'       hexagon1 marker
# 'H'       hexagon2 marker
# '+'       plus marker
# 'x'       x marker
# 'D'       diamond marker
# 'd'       thin_diamond marker
# '|'       vline marker
# '_'       hline marker
```



```python
x = np.random.rand(100)
plt.hist(x, color ='k',alpha = 0.7)
#common color:  r :red,b:blue, g:green,b:black,y:yellow
df = pd.DataFrame(np.random.rand(40,4),columns=['A','B','C','D'])
df.plot(linestyle='-.',colormap='gist_earth_r')
# colormap：
# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r,
# Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, 
# PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, 
# RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, 
# YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, 
# cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r,
# gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, 
# gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, 
# nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, 
# spectral_r ,spring, spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r
```

- Annotation

```python
df = pd.DataFrame(np.random.rand(40,4),columns=['A','B','C','D'])
df.plot(linestyle='-.',colormap='gist_earth_r')
plt.text(15,0.9,'Text here',fontsize=10)# add text info , annotation
```

- Chart output

```python
df = pd.DataFrame(np.random.rand(40,4),columns=['A','B','C','D'])
df.plot(linestyle='-.',colormap='gist_earth_r')
plt.text(15,0.9,'Text here',fontsize=10)# add text info , annotation
plt.savefig('C:\\Users\\everi\\Desktop\\Code\\Python\\Py2021\\pic.png',
           dpi=400,
           bbox_inches='tight',
           facecolor='g',
           edgecolor='b') #tab+shift
# save format: png，pdf，svg，ps，eps
# dpi resolution ratio
# bbox_inches：‘tight’try to cut out the white space around the chart。
# facecolor，edgecolor： Background color，default ‘w’
```

#### 8.3.4 Chart in detail

- subplot

```
# plt.figure() Drawing object
# plt.figure(num=None, figsize=None, dpi=None, facecolor=None, edgecolor=None, 
# frameon=True, FigureClass=<class 'matplotlib.figure.Figure'>, **kwargs)

fig1 = plt.figure(num=1,figsize=(4,2))
plt.plot(np.random.rand(50).cumsum(),'k--')
fig2 = plt.figure(num=2,figsize=(4,2))
plt.plot(50-np.random.rand(50).cumsum(),'k--')
# num：Chart serial number
# figsize：Chart size
# When we call plot, if we set plot.figure (), a figure will be generated automatically
```



```
# create subplots  2 - create a figure，then return a subplot object array  → plt.subplot

fig,axes = plt.subplots(2,3,figsize=(10,4)) #Generate an array of chart objects
ts = pd.Series(np.random.randn(1000).cumsum())
print(axes, axes.shape, type(axes))

ax1 = axes[0,1]
ax1.plot(ts)
```



- histogram and kde

```python
x = pd.Series(np.random.rand(1000))
x.hist( bins = 20,
      histtype='bar',
      align = 'left',
       orientation = 'vertical',
       alpha = 0.5,
       density =True,stacked =True
      )  #bar barstacked step stepfilled,align = 'mid'/left/right,orientation = 'horizontal'
x.plot(kind='kde')  #Kernel Density Estimation
```

- scatter

```python
x = np.random.rand(100)
y = np.random.rand(100) #1 d data
plt.scatter(x,y,
            s=np.random.rand(100)*100,
            c=y,
            marker='.',
            cmap='Reds',
            norm=None,
            vmin=None,
            vmax=None,
            alpha=0.8       
           ) #scatter chart, dot
```

- box

```python
df = pd.DataFrame(np.random.rand(40,5),columns=['A','B','C','D','E'])
color = dict(boxes='Green',whiskers='Orange',medians='Blue',caps='Gray')
df.plot.box(
  grid = True,
    color =color
)
```

### 8.4 Seaborn

i t is an update of plt based on Matplotlib. It is powerful 

#### 8.4.1 Histogram

- distplot

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
%matplotlib inline

import warnings
warnings.filterwarnings('ignore') 
```

> bins → Number of boxes
> hist、ked → Is the box / density curve displayed
> norm_hist → Is the histogram displayed according to density
> rug → Display data distribution
> vertical →  color → label → axlabel

```
#histogram
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
s = pd.Series(np.random.randn(100)*100)
sns.distplot(s,bins=20,hist=True,
    kde=True,norm_hist = False,rug =True, vertical= False,color = 'r',rug_kws = {'color':'g'} 
            )  
#fit value, density curve
```

<img src="./image/sb1.png" alt="pig" />

- 
- histtype includes：'bar', 'barstacked', 'step', 'stepfilled'

```
sns.distplot(s,rug = True, 
            rug_kws = {'color':'g'} ,   
            # Set data frequency distribution color
            kde_kws={"color": "k", "lw": 1, "label": "KDE",'linestyle':'--'},   
             #Set density curve color, line width, dimension and line shape
            hist_kws={"histtype": "step", "linewidth": 1,"alpha": 1, "color": "g"}) 
```

<img src="./image/sb2.png" alt="pig" />

Data density distribution of single sample

```
# 2、 - kdeplot()
# Data density distribution of single sample

sns.kdeplot(s,shade = False,  #  fill or not
           color = 'r',  
           vertical = False)

sns.kdeplot(s,bw=5, label="bw: 0.2",
            linestyle = '-',linewidth = 1.2,alpha = 0.5)
# bw → Control the degree of fit,  similar with number of boxes in histogram

sns.rugplot(s,height = 0.1,color = 'k',alpha = 0.5)
# Data frequency distribution
```

Data density distribution of single sample

```
# 2、 - kdeplot()
# Data density distribution of two samples


rs = np.random.RandomState(2)  # Seed random number
df = pd.DataFrame(rs.randn(100,2),
                 columns = ['A','B'])
sns.kdeplot(df['A'],df['B'],
           cbar = True,    # Show color legend
           shade = True, 
           cmap = 'Reds',  # Settings palette
           shade_lowest=False,  # Is the outermost color displayed
           n_levels = 10   # Number of curves
           )

sns.rugplot(df['A'], color="g", axis='x',alpha = 0.5)
sns.rugplot(df['B'], color="r", axis='y',alpha = 0.5)
```

Multiple density maps

```
# Multiple density maps
rs1 = np.random.RandomState(2)  
rs2 = np.random.RandomState(5)  
df1 = pd.DataFrame(rs1.randn(100,2)+2,columns = ['A','B'])
df2 = pd.DataFrame(rs2.randn(100,2)-2,columns = ['A','B'])

sns.kdeplot(df1['A'],df1['B'],cmap = 'Greens',
            shade = True,shade_lowest=False)
sns.kdeplot(df2['A'],df2['B'],cmap = 'Blues',
            shade = True,shade_lowest=False)
```

#### 8.4.2 jointplot()

```
# 1、Comprehensive scatter diagram - jointplot()
rs = np.random.RandomState(2)  
df = pd.DataFrame(rs.randn(200,2),columns = ['A','B'])
# 创建数据

sns.jointplot(x=df['A'], y=df['B'],  # Show columns name
              data=df,   
              color = 'k',  
              s = 50, edgecolor="w",linewidth=1,  
              kind = 'scatter',   # type：“scatter”、“reg”、“resid”、“kde”、“hex”
              space = 0.2,  # 设置散点图和布局图的间距
              size = 8,   # 图表大小（自动调整为正方形）
              ratio = 5,  # 散点图与布局图高度比，整型
              marginal_kws=dict(bins=15, rug=True)  # 设置柱状图箱数，是否设置rug
              )  
```



```
rs = np.random.RandomState(15)
df = pd.DataFrame(rs.randn(300,2),columns = ['A','B'])
g = sns.jointplot(x=df['A'], y=df['B'],data = df,
                  kind="kde", color="r",
                  shade_lowest=False)

g.plot_joint(plt.scatter,c="w", s=30, linewidth=1, marker="+")
```

#### 

## 9. Application

### 9.1 Medical CT Image Data Analysis 

#### 	9.1.1  Project description：Deep leision

​      Computed Tomography（CT）plays an important role in clinical diagnosis. It has the characteristics of high speed, high accuracy and good repeatability . Doctors can make a diagnosis of the patient's condition and give a treatment plan through CT images. Most of the current medical detection research tasks are designed for single task learning, of which the detection function is often only for a specific part of lesion detection. 

> These data is from here: DeepLesionGraphsintheWild: RelationshipLearningandOrganizationofSignificantRadiologyImage FindingsinaDiverseLarge-scaleLesionDatabase

There are 8 kinds of lesions: lung, abdomen, mediastinum, liver, pelvis, soft tissue, kidney and bone

  <img src="./image/Medical1.png" alt="pig" style="zoom:80%;" />

The **DeepLesion** dataset contains 32,120 axial computed tomography (CT) slices from 10,594 CT scans (studies) of 4,427 unique patients. There are 1–3 lesions in each image with accompanying bounding boxes and size measurements, adding up to 32,735 lesions altogether. 	 

#### 9.1.2 Data Meaning

​	Most complex learning problems are usually decomposed into simple and independent sub-problems, and then the results are combined to get the results of the original problem. In this way, the association information between problems is ignored and the generalization effect of the model is weakened . In the actual clinical diagnosis, it will be found that many lesions are actually related, and the detection of a single part is not conducive for the doctor's comprehensive diagnosis. The detection of multi-site lesions can detect the metastasis of lesions earlier. At the same time, it can excavate the relationship between different lesions . 

<img src="./image/medical.png" alt="pig" style="zoom:80%;" />

In DL_info.csv, each row is the information of a lesion in DeepLesion. The meaning of the columns are:

> 1. File name. Please replace the last underscore with / or \ to indicate sub-folders.
>2. Patient index starting from 1. 
> 3. Study index for each patient starting from 1. There are 1~26 studies for each patient.
>4. Series ID.
> 5. Slice index of the key slice containing the lesion annotation, starting from 1.
> 6. 8D vector, the image coordinates (in pixel) of the two RECIST diameters of the lesion. [*x*11, y11, *x*12, *y*12, *x*21, *y*21, *x*22, *y*22]. The first 4 coordinates are for the long axis. 
>7. 4D vector, the bounding-box [*x*1, *y*1, *x*2, *y*2] of the lesion (in pixel) estimated from the RECIST diameters.
> 8. 2D vector, the lengths of the long and short axes. The unit is pixels.
>9. The relative body position of the center of the lesion. The z-coordinates were predicted by the self-supervised body part regressor.  The coordinates are approximate and just for reference.
> 10. The type of the lesion. Types 1~8 correspond to bone, abdomen, mediastinum, liver, lung, kidney, soft tissue, and pelvis, respectively. See our paper for details. The lesion types are coarsely defined and just for reference. Only the lesions in the val and test sets were annotated with others denoted as -1.
>11. This field is set to 1 if the annotation of this lesion is possibly noisy according to manual check. We found 35 noisy annotations out of 32,735 till now.
> 12. Slice range. Context slices neighboring to the key slice were provided in this dataset. For example, in the first lesion, the key slice is 109 and the slice range is 103~115, meaning that slices 103~115 are provided. For most lesions, we provide 30mm extra slices above and below the key slice, unless the long axis of the lesion is larger than this thickness (then we provide more) or the beginning or end of the volume is reached.
>13. Spacing (mm per pixel) of the *x*, *y*, and *z* axes. The 3rd value is the slice interval, or the physical distance between two slices.
> 14. Image size.
>15. The windowing (min~max) in Hounsfield unit extracted from the original DICOM file.
> 16. Patient gender. F for female and M for male.
>17. Patient age.
> 18. Official randomly generated patient-level data split, train=1, validation=2, test=3.

```
import pandas as pd
import numpy as np
import seaborn as sns  #update matplotlib,provide more useful function to draw pic
import matplotlib.pyplot as plt
%matplotlib inline
```



```
import os
os.chdir(r'C:\Users\everi\Desktop\Code\Python\Py2021') #change directory
df01 = pd.read_csv('DL_info_deletelargeno.csv',engine='python') #read csv file
df01.dropna(inplace =True) #Remove missing values.
df01.head(10)
```

not only study, but also a kind of research. You can do the data analysis well, you can publish paper

​	<img src="./image/information.png" alt="pig" style="zoom:80%;" />

- Patient_age column

```
data_age = df01['Patient_age']  
data_age.head(10)
print('The total number of patient is %i'%len(data_age)) #9786
```

- 3 cols

```
data = df01[['Coarse_lesion_type','Patient_gender','Patient_age']]
data.head()
```



```
df = pd.DataFrame({'a':df01['Coarse_lesion_type'],'b':df01['Patient_gender']},columns=['a','b'])
df.plot.hist(stacked=True,bins=10, alpha=0.5,colormap='RdYlGn',grid=True)
#df.plot(linestyle='--',marker ='v')  
plt.title('Coarse_lesion_type')
```

<img src="./image/medic1.png" alt="pig"  />

```
data_age.head()
data_age.plot.box(vert=False,colormap='RdYlGn',grid=True,figsize=(10,4)) #Make a box plot of the DataFrame columns.
plt.xlabel('age',fontsize=18)
plt.ylabel('value',fontsize =20)
plt.title('Patient_age')
```

<img src="./image/medic2.png" alt="pig"  />

```
plt.scatter(df01['Lesion_diameters_long'],df01['Lesion_diameters_short'],1,'r') #scatter chart, dot
plt.xlabel('width',fontsize=16)
plt.ylabel('height',fontsize =16)
plt.title('Disease_size')
```

<img src="./image/medic3.png" alt="pig"  />

- kde

```
# df01['Lesion_diameters_long'],df01['Lesion_diameters_short']
plt.figure(figsize=(15,10))
sns.kdeplot(df01['Lesion_diameters_long'],df01['Lesion_diameters_short']
            ,shade=True,cmap='Reds',cbar=True,n_levels=10) #2 samples
sns.rugplot(df01['Lesion_diameters_long'],color ='g',axis='x',alpha=0.5)
sns.rugplot(df01['Lesion_diameters_short'],color ='r',axis='y',alpha=0.5)
```





<img src="./image/densitymap.png" alt="pig" style="zoom:60%;" />

> ​       

We choose the combination of siloette coefficient and SSE to select the optimal K value. The specific method is to let K value from 1 to the appropriate upper limit of 16, and cluster each k value and record the corresponding SSE.

#### 9.1.3 Clustering

A data set is divided into different classes or clusters.  the cluster objects similarity is the same , and the difference  is as large as possible in different clusters .

link: Desktop/Code/数据分析/练习06_房价影响因素挖掘/练习06房价影响因素挖掘.ipynb



![pig](./image/cluster.gif)

AI ----Machine learning--- Deep learning  - -   Size

KMeans algorithm：

> 1. Randomly initialize their respective center points
>
> 2. Calculate the distance between the point and the center of each group for classification, then the point is classified to the closest group.
>
> 3. Recalculate Group Center
>
> 4. back to step 1

![pig](./image/cluster2.gif)

 

k-means

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline

import warnings
warnings.filterwarnings('ignore')
from sklearn.datasets.samples_generator import make_blobs
x,y_true = make_blobs(n_samples=300,n_features=4, cluster_std=0.5,random_state=0)
print(y_true[:10])
print(x[:10])
plt.scatter(x[:,0],x[:,1],cmap='Reds',s=10,alpha=0.8)
#A scatter plot of *y* vs. *x* with varying marker size and/or color.
#Generate isotropic Gaussian blobs for clustering.
```

![pig](./image/141.png)

Evaluate:

```
from sklearn.cluster import KMeans
kmeans = KMeans(n_clusters=5,random_state=5)
kmeans.fit(x) #Compute k-means clustering.
y_kmeans = kmeans.predict(x) #Predict the closest cluster each sample in X belongs to.
plt.scatter(x[:,0],x[:,1],c=y_kmeans, cmap='Dark2',s=10,alpha=0.8,marker='*')  #array-like or list of colors or color
# print(x[:,0])
```

![pig](./image/142.png)

- clustering medical data

```
import os
import xlrd
from sklearn.cluster import KMeans
os.chdir("C:/Users/everi/Desktop/Code/Python/Py2021")
df01 = xlrd.open_workbook('DL_info_kmeans.xls')
table = df01.sheets()[0]
data = []
for i in range(table.nrows):
    if i == 0:
        continue
    else:
        data.append(table.row_values(i)[1:])
featureList = ['Lesion_diameters_long', 'Lesion_diameters_short']
mdl = pd.DataFrame.from_records(data, columns=featureList)
mdl_new = np.array(mdl[['Lesion_diameters_long', 'Lesion_diameters_short']])  #2d
# result = pd.Series.from_records(data, columns=['Coarse_lesion_type'])
# result =data['Coarse_lesion_type']
print(mdl_new[:,0])
kmeans = KMeans(n_clusters=5,random_state=5)
kmeans.fit(mdl_new) #Compute k-means clustering.
y_kmeans = kmeans.predict(mdl_new) #Predict the closest cluster each sample in X belongs to.
plt.scatter(mdl_new[:,0],mdl_new[:,1],c=y_kmeans, cmap='Dark2',s=10,alpha=0.8,marker='*')  #array-like or list of colors or color

```

![pig](./image/143.png)

- SSE

```
import os
import xlrd
from sklearn.cluster import KMeans
os.chdir("C:/Users/everi/Desktop/Code/Python/Py2021")
df01 = xlrd.open_workbook('DL_info_kmeans.xls')
table = df01.sheets()[0]
data = []
for i in range(table.nrows):
    if i == 0:
        continue
    else:
        data.append(table.row_values(i)[1:])
featureList = ['Lesion_diameters_long', 'Lesion_diameters_short']
mdl = pd.DataFrame.from_records(data, columns=featureList)
mdl_new = np.array(mdl[['Lesion_diameters_long', 'Lesion_diameters_short']])  #2d
SSE = []
for k in  range(1,17):
    group = KMeans(n_clusters=k)
    group.fit(mdl[['Lesion_diameters_long', 'Lesion_diameters_short']])
    SSE.append(group.inertia_)
X=range(1,17)
plt.xlabel('k')
plt.ylabel('SSE')
plt.plot(X, SSE, linestyle='-.',marker ='v')
plt.show()  #group number is greater than 8
```

![pig](./image/144.png)

![pig](./image/SSE.png)

```
import os
import xlrd
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
os.chdir("C:/Users/everi/Desktop/Code/Python/Py2021")
df01 = xlrd.open_workbook('DL_info_kmeans.xls')
table = df01.sheets()[0]
data = []
for i in range(table.nrows):
    if i == 0:
        continue
    else:
        data.append(table.row_values(i)[1:])
featureList = ['Lesion_diameters_long', 'Lesion_diameters_short']
mdl = pd.DataFrame.from_records(data, columns=featureList)
mdl_new = np.array(mdl[['Lesion_diameters_long', 'Lesion_diameters_short']])  #2d
Scores = []  
for k in range(2, 17):
    estimator = KMeans(n_clusters=k)      
    estimator.fit(np.array(mdl[['Lesion_diameters_long', 'Lesion_diameters_short']]))
    Scores.append(silhouette_score(np.array(mdl[['Lesion_diameters_long', 'Lesion_diameters_short']]), estimator.labels_, metric='euclidean'))
X = range(2, 17)
plt.xlabel('k')
plt.ylabel('Silhouette Coefficient')
plt.plot(X, Scores, 'ro-')
plt.show()#group number 15 = 3*5   
#select 3 kind of radio 2:1, 1:2 ,1:1 ,select 5 kinds of width value 
```

![pig](./image/145.png)

### 9.2 User behavior analysis

#### 9.2.1 Project description：
In recent years, the problem of employee turnover puzzles managers. Resignation become a significant problem for company development. In this project, we need to do some data analysis in employee. Try to pridect whether a person still work or leave the company in the near future.

  We know there are many possible factors for an employee leaving company. It mainly contains salary\Department\EnvironmentSatisfaction etc.We will get these data and do some data analysis

  Data is here:https://challenge.datacastle.cn/v3/cmptDetail.html?id=342

#### 9.2.2 Dataset description:
* DataCastle[Link](http://www.pkbigdata.com/common/cmpt/%E5%91%98%E5%B7%A5%E7%A6%BB%E8%81%8C%E9%A2%84%E6%B5%8B%E8%AE%AD%E7%BB%83%E8%B5%9B_%E7%AB%9E%E8%B5%9B%E4%BF%A1%E6%81%AF.html)
* We have 2 files. train.csv and test.csv. it contains 1100 items(each item means an employee)，and 31 cols
* Dict
    * Age：Employee age
    * Attrition：1 means the employee has resigned，0 means the employee is still in company
    * BusinessTravel： Non-Travel means they have no business trip，Travel_Rarely means he don't travel often，Travel_Frequently；
    * Department: include SalesDepartment，Research & Development，Human Resources Department；
    * DistanceFromHome：from 1 to 29，1 is the nearest
    * Education：Education level of employees，from 1 to 5，5 is the highest level；
    * EducationField：include Life Sciences\Medical\Marketing\Technical DegreeHuman Resources\Other；
    * EnvironmentSatisfaction：1 is minimum satisfaction，4 is the highest satisfaction
    * Gender：Male Female
    * JobInvolvement：Employee engagement，1 is the lowest engagement，4 is the highest investment
    * JobLevel：1 is the lowest，5  is the highest
    * JobRole：Sales Executive\Research Scientist\Laboratory Technician\Manufacturing Director\Healthcare Representative\Manager\Sales Representative\Research Director\Human Resources
    * JobSatisfaction：1 represents the lowest degree of satisfaction，4 is the highest satisfaction
    * MaritalStatus：Single\Married\Divorced
    * MonthlyIncome： total revenue from 1009 to 19999
    * NumCompaniesWorked：Number of companies where employees have worked
    * OverTime：Yes，No means he never work overtime
    * PercentSalaryHike：Percentage increase in salary；
    * PerformanceRating：performance evaluation；
    * RelationshipSatisfaction：1 is minimum satisfaction，4 is the highest satisfaction
    * StandardHours：standard working hours；
    * TrainingTimesLastYear：The training time. 0 means no training and 6 means the longest training time；
    * WorkLifeBalance：balance between work and life ，1 is the lowest，4 is the highest 
    * Others：YearsAtCompany、YearsInCurrentRole、YearsSinceLastPromotion、YearsWithCurrManager、StockOptionLevel、TotalWorkingYears、Over18、EmployeeNumber

#### 9.2.3 Project tasks

-  data checking

```python
import pandas as pd
import numpy as np
import seaborn as sns  #update matplotlib,provide more useful function to draw pic
import matplotlib.pyplot as plt
from sklearn import preprocessing  #mathine learning
%matplotlib inline
#import the data
sample_data = pd.read_csv('train.csv')
sample_data.head()
sample_data.info()
```

![pig](./image/9.21.png)

```
sample_data.describe()  #basic data calculation 
```

![pig](./image/9.22.png)

- Proportion of Positive sample and Negative sample

```
pos_data = sample_data[sample_data['Attrition']==1]
neg_data = sample_data[sample_data['Attrition']==0]
print('Positive sample number:{}'.format(len(pos_data)))
print('Negative sample number:{}'.format(len(neg_data)))
print('Proportion:{}'.format(len(neg_data)/len(sample_data)))
#Proportion of Positive sample & Negative sample
```

-  Relationship between resignation and age

```
plt.figure()
#sns.countplot(x='Attrition',data=sample_data,hue ='Education')
plt.subplot(131) 
sns.boxplot(x='Attrition',data=sample_data,y ='YearsWithCurrManager') 
#JobInvolvement,YearsAtCompany,YearsWithCurrManager
plt.subplot(132) 
sns.boxplot(x='Attrition',data=sample_data,y ='YearsAtCompany') 
plt.subplot(133) 
sns.boxplot(x='Attrition',data=sample_data,y ='YearsWithCurrManager') 
plt.figure()
sns.countplot(x='Attrition',data=sample_data,hue ='Education')
```



![pig](./image/9.23.png)

![pig](./image/9.24.png)

![pig](./image/9.25.png)

```python
sns.pairplot(sample_data,hue ='Attrition',
             vars=['PercentSalaryHike','PerformanceRating',
                   'RelationshipSatisfaction','StandardHours',
                   'StockOptionLevel','TotalWorkingYears',
                   'TrainingTimesLastYear','WorkLifeBalance',
                   'YearsAtCompany']) 
#multi variable relationship 
```

![pig](./image/an.png)

- data cleaning
- data analysising

```python
# Numerical data
num_cols = ['Age', 'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
           'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
# Category data
# cat_cols = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'Over18', 'OverTime']
# In this case, only 3 are selected as examples
cat_cols = ['Gender', 'MaritalStatus', 'OverTime']
# Ordered category data
ord_cols = ['DistanceFromHome', 'Education', 'EnvironmentSatisfaction', 'JobInvolvement', 'JobLevel', 'JobSatisfaction',
           'PerformanceRating', 'RelationshipSatisfaction', 'StockOptionLevel', 'WorkLifeBalance']

# target_col
target_col = ['Attrition']

# All feature columns
#total_cols = num_cols + cat_cols + ord_cols
total_cols = num_cols 
used_data = sample_data[total_cols + target_col]

print('All feature contain {} columns'.format(len(total_cols)))
print(total_cols) #used_data,total_cols
```

 Split training and testing data，80% for training，20% for testing

```python
pos_data = used_data[used_data['Attrition'] == 1].reindex()
train_pos_data = pos_data.iloc[:int(len(pos_data) * 0.8)].copy()# proportion is the same in pos and neg data
test_pos_data = pos_data.iloc[int(len(pos_data) * 0.8) :].copy()

neg_data = used_data[used_data['Attrition'] == 0].reindex()
train_neg_data = neg_data.iloc[:int(len(neg_data) * 0.8)].copy()
test_neg_data = neg_data.iloc[int(len(neg_data) * 0.8) :].copy()

train_data = pd.concat([train_pos_data, train_neg_data])
test_data = pd.concat([test_pos_data, test_neg_data])
```

- train_data

```python
print('training sample number', len(train_data))
print('pos and neg proportion', len(train_pos_data) / len(train_neg_data))
train_data.head()
```

- test_data

```python
print('testing sample number', len(test_data))
print('pos and neg proportion', len(test_pos_data) / len(test_neg_data))
test_data.head()
```

![pig](./image/9.29.png)

```python
# Integrate all features
train_feats = train_data[num_cols].values
train_targets = train_data[target_col].values

test_feats = test_data[num_cols].values
test_targets = test_data[target_col].values

print('Training data：', train_feats.shape)
print('Testing data：', test_feats.shape)
```

![pig](./image/9.28.png)

```python
from sklearn.linear_model import LogisticRegression
lr_clf = LogisticRegression()
lr_clf.fit(train_feats, train_targets)
```



```python
#Model verification
from sklearn import metrics

print('Positive number in testing data', len(test_pos_data))
print('Negative number in testing data', len(test_neg_data))

# LogisticRegression
test_pred = lr_clf.predict(test_feats)
print(metrics.confusion_matrix(test_targets, test_pred, labels=[1, 0]))
print('metrics accuracy：', metrics.accuracy_score(test_targets, test_pred)) # 0.837
```

### 9.3 Course Review

Words are not as good as table，table is not as good as the picture

![pig](./image/r1.png)

#### 9.3.1 Review

- L1-Basic knowledge: Overview of data types, String/list/tuple/dict/ variable/opreator
- L2-Python container: List/ Tuple/Dict/Set
- L3- Control flow : Sequential /Branching /Cycle /Flow chart
- L4-Strings
- L5-Functions: keywords(return/pass/break/continue\)
- L6-OOP:
- L7-File / Exception
- L8- Shop data loading and storage
- L9-Numpy: Random/Transpose/Copy/ Calculation
- L10-Pandas: Series/ DataFrame
- L11- Matplotlib
- L12- Seaborn
- L13- User behavior analysis
- L14- Medical CT Image Data Analysis

#### 9.3.2 Next Step research direction

- 1. Computer Vision

  Multi object recognition

  ![pig](./image/r2.png)

3 D reconstruction

![pig](./image/r3.gif)



- 2. Natural Language Processing == NLP

  ```
  knowledge graph ：neo4j.bat console
  https://grapheco.github.io/InteractiveGraph/dist/examples/example1.html
  
  Speech synthesis:
  https://www.xfyun.cn/services/online_tts
  ```

  ![pig](./image/kg.png)

  

- 3. Recommendation system

  ```
  Application: mobile app/ notification is you are interested in
  Website 
  ```

#### 9.3.3 Practice: Multi files operation

```
Talk is cheap, show me the code  -- Linus Torvalds
```

Sales data of products A and B of a company in January, February and March 2018. The format is xlsx .

We need to read data in batches from different files and out put data_counts\columns\nan_counts

```
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import os
%matplotlib inline
```

- Task1: output data_counts\columns\nan_counts

```

#os.chdir(r'C:\Users\everi\Desktop\Code\Python\Py2021\Lesson-15\') 
path = 'C:/Users/everi/Desktop/Code/Python/Py2021/Lesson-15/'
folder = os.walk(path)
files = list(folder)[0][2]
n = 1
for i in files:
    file = path + i
    data = pd.read_excel(file) #read_excel
    data_counts = len(data)  #data number
    columns = data.columns.tolist() #output column
    nan_counts = len(data[data.isnull().values == True])  # missing data ==nan
    print('The data_counts of  %i th data is：%i' % (n, data_counts))
    print('The columns of %i data is：' % n,columns)
    print('The nan_counts %i  data is：：%i' % (n, nan_counts))
    n += 1
print("finished")
```

- output

```
The data_counts of  1 th data is：31
The columns of 1 data is： ['date', 'productA', 'productB']
The nan_counts 1  data is：：3
The data_counts of  2 th data is：28
The columns of 2 data is： ['date', 'productA', 'productB']
The nan_counts 2  data is：：4
The data_counts of  3 th data is：31
The columns of 3 data is： ['date', 'productA', 'productB']
The nan_counts 3  data is：：3
finished
```

- task2 

```
# 1. change date to_period and output Dataframe with data1,data2,data3
def f2_1():
    path = 'C:/Users/everi/Desktop/Code/Python/Py2021/Lesson-15/'
    folder = os.walk(path)  
    files = list(folder)[0][2]
    data_files = []
    for i in files:
        file = path + i
        data = pd.read_excel(file,index_col = 0)
        columns = data.columns.tolist()  # Extract column name
        data.to_period()  # change date to time series
        data[columns[0]].fillna(data[columns[0]].mean(),inplace = True)  
        data[columns[1]].fillna(data[columns[1]].mean(),inplace = True)
        #  fill missing value with mean
        data_files.append(data)
    return(data_files)


# 2.Calculate the total monthly sales of products A and B
# 3.Draw multi series histogram & save
 
def f2_2(*data_files):
    path = 'C:/Users/everi/Desktop/Code/Python/Py2021/Lesson-15/'
    A_sale = []
    B_sale = []
    for data in data_files:
        columns = data.columns #Extract column name
        A_sale.append(data[columns[0]].sum())   # Update total sales of product A
        B_sale.append(data[columns[1]].sum())   # B
    df = pd.DataFrame({'A_sale_sum': A_sale,'B_sale_sum':B_sale},
                     index = pd.period_range('201801','201803',freq = 'M'))
    #print(df)   
    plt.figure()
    df.plot(kind = 'bar',style = '--o',color = ['r','g'],alpha = 0.8, rot = 0,figsize = (8,4))
    plt.title('Sales  histogram')
    plt.ylim([0,25000])
    plt.legend(loc = 'upper left')
    plt.grid()
    plt.savefig(path + 'Products A,B Histogram.png',dpi=400)
        
# Record the date when the sales volume exceeds 80%  
def f2_3(*data_files):
    keydates = []
    for data in data_files:
        columns = data.columns 
        data['A_sale_sum%'] = data[columns[0]].cumsum() / data[columns[0]].sum()  
        keydate = data[data['A_sale_sum%']>0.8].index[0]  
        keydates.append(str(keydate))
    print('The date that exceeds 80% in product A is\n', keydates)
    return(keydates)

f2_1()
data1, data2, data3 = f2_1()[0], f2_1()[1], f2_1()[2]
print(data1.head(),'\n-----')
f2_2(data1,data2,data3)
f2_3(data1,data2,data3)
```



![pig](./image/L15t2.png)

- task3: 

```
#1.delete missing values,Convert date to time series

def f3_1():
    path = 'C:/Users/everi/Desktop/Code/Python/Py2021/Lesson-15/'
    folder = os.walk(path)  
    files = list(folder)[0][2]
    data_files = []
    for i in files:
        file = path + i
        data = pd.read_excel(file,index_col = 0)
        columns = data.columns.tolist()  # Extract column name
        data.to_period()  # Convert to time series
        data.dropna(inplace=True)  # Delete missing values
        data_files.append(data)
    data = pd.concat([data_files[0],data_files[1],data_files[2]])  # Merge data
#     print(data)
    return(data)


#1.When the sales of product a is 1200, predict the sales volume of product B
#2.Draw scatter and store the picture
def f3_2(data):
    path = 'C:/Users/everi/Desktop/Code/Python/Py2021/'
    model = LinearRegression()
    model.fit(data['productA'][:,np.newaxis],data['productB'])  
    # build LinearRegression model
    xtest = np.linspace(0,1000,1000)
    ytest = model.predict(xtest[:,np.newaxis])
    plt.scatter(data['productA'],data['productB'],marker = '.',color = 'k')
    plt.plot(xtest,ytest,color = 'r')
    plt.grid(True)
    plt.title('Products A-B Sales LinearRegression')
#     plt.savefig(path + 'A-B sale prediction.png',dpi=400)  
    # save pic
    predict_sales = 1200
    predict_sales = np.array(predict_sales).reshape(-1, 1)
    return(model.predict(predict_sales))

f3_1()
data = f3_1()
print(' View AB product sales relationship\n-------')

f3_2(data)
```

![pig](./image/L15t3.png)

## 10. Assessment and Evaluation

### 10.0 Topics

- 1. Application

  - Chat robot （code:D:\Course\AI\knowledgeGraph\ch5-QAMedicalKG）

  - KnowledgeGraph

  - Mobile device(Android\Cross Platform--Java/HTML5/CSS3,We can use python in backend/server)

    > http://www.tuling123.com/
    >
    > 
    >
    > ![pig](./image/cb2.png) ![pig](./image/cb1.png)

  - Web Application(Framework)----- Java (SpringMVC/SpringBoot/Servlet)/PHP/ASP/Python(Django )

  ![pig](./image/cb.png)

- 2. Big Project Introduction(code&document)

- 3. Summary

### 10.1 Grade definition

​	Final grade（100）= Formative performance（50×100%）+ Summative performance（100×50%）

### 10.2 Formative assessment criteria

| **Item**              | **Score** | **Objective**                                                | **Description**                                              | **Comments**            |
| --------------------- | --------- | :----------------------------------------------------------- | ------------------------------------------------------------ | ----------------------- |
| Course project/coding | 30        | Evaluate if students can organize and  apply knowledge correctly. | Check code applications;3 times; 10 points  per check        |                         |
| Homework              | 10        | Evaluate the ability of self-study and  documentation        | 10 points for code fulfillment;                              |                         |
| Classroom interaction | 10        | Evaluate students’ attitude.                                 | 1 points /time                                               | No more than 10 points. |
| Classroom discipline  | 0         | Evaluate students’ attitude.                                 | Students who do activities not allowed  in class will be deduced 1 point one time. | No more than 20 points. |

### 10.3 Summative assessment

Exam method: Big Project   Total Score: 100 Points  

| **Total Score: 100 Points**                                  |                                                              |                                                              |                                                              |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| **Test Case Coverage **  （25 Points）                       | **Test Case Details**  （25 Points）                         | **Tool usage** （25 Points）                                 | **Reporting** （25 Points）                                  |
| Be able to understand based knowledge. Include data analysis and display. | The code implementation design is appropriate for specific requirement. The objective  and steps are clear.  And a document is required. | Be able to use Pycharm and Jupiter. Package installation and version  control correctly. | Application can be described clearly. Status, severity and other  attributes are correct. |



