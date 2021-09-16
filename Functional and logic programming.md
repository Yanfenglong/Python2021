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

```
list0 = [1,2,3,4]  # add 4 elements  in a sequence
list1 = [1,2,3,4,"hello","world",[5,6,7],1.3,5.4]
list1
```

- List common operation

```
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

```
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



```
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

```

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

```
#generator: it is comma , not colons , start : limit number : step
b = range(10)
c = list(range(10))
print(c)
```



```
Question:
    1. is the result of range() integer？  # yes
    2. create a range with 5 element， Use type() to check its type
    3. which grammar is correct？a = range(5) ，a = range(2:6),a = range(3,7) 
    4. if  b = range(10), what is the result of b[2],b[-2],b[5] 
```

- Insert and delete 

```
#remove an element
#c.remove(5)
#del is a sentence , slice
#del c[2:4] 
#c.clear() #clear the whole list
c.insert(1,"hello") #insert(index, value),index this the position of this list
print(c)
```

- Copy list

```
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

```
m.sort()   -- modify the original list into an ordered sequence
sorted(m)  -- create a new list
```

​    2. create a list m = [1,2,4,1,1,3] , insert ["Jack"] between 4 and 1

```
m.insert(3,"Jack")
```

   3.m = [1,2,4,1,1,3] what is the difference between m.remove(2)  ,m.pop(2), del m[2]

```
m.pop() ,del m[2] is a statement, the result is same
```

  4 .what is the difference between append and extend?

```
append #  [1,2,3,[4,5,6]]  
extend #  [1,2,3,4,5,6] 
```

5. Input 3 int x,y,and z，please output these three numbers from small to large.

we need to use 2 function: input(), for i in range():

```
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

```
dic4 = {'name':'yan','home':{'location':'Jakarta','email':'yan@google.com'}}
print(dic4['home']['location'])
print(dic4.get('home').get('location')) # dict.get()
print(dic4.values(),dic4.keys()) #

```



```
dic5 = {'name':'yan','age':'18','height':'180cm','hair':'black',
        'home':{'location':'Jakarta','email':'yan@google.com'}}
#use a loop , like for cycle
for i in dic5.values(): #here we output the values, try to output the keys 
    print(i)

for k,v in dic5.items():  #(k,v)
    print(k,v)  #print(v)
```



```
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

```
basket = {"apple","orange","pear","apple","apple","apple"}  #set type
basket1 = set("pear")
print(basket1)
set1 = set("orange")# letters
set2 = {}  #it is dict type
set3 = set(("orange","pear","apple")) #words
print(set3)
```

calculate set

```
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
```




### 3.3 Cycle structure

- for cycle

```python
#For cycle is  a loop , we can get all the elements from a sequence,such as list/dict
lst = list(range(5)) # 0,1,2,3,4
for i in lst[::2]: #slicing
    print(i)
```



```python
dic1 = {'Tom':'18','Jack':'19','Alex':'20','Mary':'21'}
for i in dic1:
    print(dic1[i])
```



```python
for i in range(3):  #underline is ok
    for k in range(2):  #nest loop, circulate embedding method
        print(i,k)   #we should not use nest loop too much, no more than 3 time 
```

#practice: write a for cycle ,try to output even number which is no more than 10
#0,2,4,6,8

```
for i in range(10):
    if  i % 2 ==0:
        print(i)
print("That is the even number")
```




- while cycle

```python
# while-else
```

Practice：

1. Output all even number which is less than 10

```
i = 1
while i<10:
    i +=1
    if i%2 ==0:
        print(i)
```



   2."Narcissistic number" is a three digit number， The sum of each digit cube is equal to the number itself. 

For example , 153 is a narcissistic number，because 153=1* * 3＋5 * *3＋3**3. And 3 raised to the power of 3 is 27， 125 is the cube of 5.    

1* 1* 1 = 1  3 * 3* 3 =27 5* 5*5 = 125      1+27+125 =153

- range(start, limit, delta=1,dtype=None)

```
153 // 10
153 // 10 % 10
153 % 10
```




- Loop control statement

The **break statement** ends the current loop and jumps to the statement immediately following the loop.

**Continue** ends the current interation and jump to the top of the loop and starts the next interation.



## 4. Strings





## 5. Functions

### 5.1 Basic concept of functions



- Basic function



- return statement



- parameter



### 5.2 Local and global variables

### 5.3 Anonymous function( lambda )



## 6. Object Oriented Programming Foundation 

Object Oriented Programming(OOP) is a programming method through defining functions to simulate the real world. OOP can control data in a reasonable and automatic way, reducing code bug, reducing code quantity,  and easier to maintain.

### 6.1 Define a class



#### 6.1.1 Class Properties



#### 6.1.2 Member methods and static methods of class



#### 6.1.3 Extends

### 6.2 Module creation and introduction



### 6.3 Package



### 6.4 Closure function



## 7. File and Exception

### 7.1 Document declaration and basic operation

excel/csv

### 7.2 System module path 

### 7.3 Files reading and writing 



-  Files reading
- Files writing 

- with statement

### 7.4 pickle

## 8. Common packages

### 8.1 Numpy

​	 Numpy is the basic python programming library .  It provides advanced mathematical operations, it also has a very efficient vector matrix operation function 。



### 8.2 Pandas

```

```



### 8.3 Matplotlib



<img src="./image/Matplotlib1.png" alt="pig" style="zoom:80%;" />

## 9. Application

### 9.1 Medical CT Image Data Analysis

​	Computed Tomography（CT）plays an important role in clinical diagnosis. It has the characteristics of high speed, high accuracy and good repeatability . Doctors can make a diagnosis of the patient's condition and give a treatment plan through CT images. Most of the current medical detection research tasks are designed for single task learning, of which the detection function is often only for a specific part of lesion detection. 

<img src="./image/information.png" alt="pig" style="zoom:80%;" />

​	There are 8 kinds of lesions: lung, abdomen, mediastinum, liver, pelvis, soft tissue, kidney and bone

<img src="./image/medical.png" alt="pig" style="zoom:80%;" />

​	Most complex learning problems are usually decomposed into simple and independent sub-problems, and then the results are combined to get the results of the original problem. In this way, the association information between problems is ignored and the generalization effect of the model is weakened . In the actual clinical diagnosis, it will be found that many lesions are actually related, and the detection of a single part is not conducive for the doctor's comprehensive diagnosis. The detection of multi-site lesions can detect the metastasis of lesions earlier. At the same time, it can excavate the relationship between different lesions .

​	<img src="./image/2对比分析3 .png" alt="pig" style="zoom:70%;" />

​	<img src="./image/densitymap.png" alt="pig" style="zoom:60%;" />

​       We choose the combination of siloette coefficient and SSE to select the optimal K value. The specific method is to let K value from 1 to the appropriate upper limit of 16, and cluster each k value and record the corresponding SSE.



![pig](./image/SSE.png)![pig](./image/Silhouette.png)

### 9.2 User behavior analysis

```
# 引入必要的包
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn import preprocessing
```

```
# 多变量关系
sns.pairplot(sample_data, hue='Attrition', vars=['Age', 'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike',
                                               'TotalWorkingYears', 'TrainingTimesLastYear', 'YearsAtCompany', 'YearsInCurrentRole',
                                               'YearsSinceLastPromotion', 'YearsWithCurrManager'])
```

![pig](./image/an.png)

```
# 数值型数据
num_cols = ['Age', 'MonthlyIncome', 'NumCompaniesWorked', 'PercentSalaryHike', 'TotalWorkingYears', 'TrainingTimesLastYear',
           'YearsAtCompany', 'YearsInCurrentRole', 'YearsSinceLastPromotion', 'YearsWithCurrManager']
# 类别型数据
# 所有类别型数据
# cat_cols = ['BusinessTravel', 'Department', 'EducationField', 'Gender', 'JobRole', 'MaritalStatus', 'Over18', 'OverTime']
```



## 10. Assessment and Evaluation

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