![logo](./image/logo.jpg)

## 1. Functional and logic programming

- Free（open source GPL）

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

Version selected :  Python2 VS Python3 

IDE: integrated development environment

```
IDE needed:Anaconda Version:Python 3.8 • 64-Bit Graphical Installer 
Software download link：
https://www.anaconda.com/products/individual
```

<font color = 'red'>**Anaconda**</font>：An open source Python distribution，which contains a large number of tools.  And spyder、jupyterNotebook

Spyder：Run the script here

jupyterNotebook： A web applications that allow creation and sharing. Support multiple programming languages such as Julia、R、Python、Octave

interactive programming ：Run the code in cmd

Script programming：Run the script after switching paths ,python a.py

Jupter NoteBook

​           - code sharing by email/Git

​          - big data integration：spark、scala、scikit-learn、R、python

- export/import ipython

- annotations 



### 1.2 Overview of data types

Python standard data type

- String

- Numbers include int and float

- Bool :True/False，it is useful to make judgments

- List

- Tuple 

- Dict

- Type conversion


### 1.3 Basic knowledge

- 1.variable

> Variable value is not fixed，the equal sign is used to assign values to variables。The rules of variable name：
>
> 1.The first character of a variable name must be a letter Or underline，It cannot start with a number
>
> 2.Variable name cannot be a keyword



- 2. operator

```python
#operator + - * /  **power//Take the integer division  %Modular operation -Returns the remainder of division

#compare/logic calculation ---and or not
#The result of cmp/logic is True/False

#member operator in /not in, usually used in dict and list
```


```python
#Directional ,It's not that the value of X has changed, but that the position pointed by X has changed
```



## 2. Python container

### 2.1List

​	x = 1 means x is a variable, and its value is unique. When x = [1,2,3,4], it is a list. There are four elements in this list. Each element has a index, that is the element position. 

- List common operation

- List and generator(range)

-  Insert and delete 

- Copy list

- Sort



### 2.2  Tuple 



### 2.3 Dict

- Built-in functions in dict

- Content reading in dict

### 2.4 Set



## 3. Control flow 



### 3.1 Sequential structure

### 3.2 Branching structure

- if statement


### 3.3 Cycle structure

- for cycle


- while cycle

```python
# while-else
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