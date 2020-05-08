# Welcome to Inefficient NumPy! :slightly_smiling_face:
The goal of this project is to implement a smaller, lesser version of the popular NumPy Library.

This is a matrix class! It can handle only 2D

## Why is it inefficient? :trollface:
I have implemented the arrays as the standard **Python List [ ].**

A list has so many attributes that make it *slower* and consume more *memory*.

- Size
- Reference Counter
- Type
- Value

However, in *NumPy*, you don't have to worry about all that, it takes care of these things differently.

NumPy arrays are of **Fixed types**, meaning every element of its array has the same datatype.

**For Example:**

> a = np.array([1, 2, 3, 4, 5], dtype="int32")

The *'dtype'* parameter will set every element of the array to be of *"int32"* datatype.


If you look at Python Lists, we can have a list like:

>my_list = [1, "two", 3.0]

Here there are multiple data types, and to manage these, the attributes *mentioned above* are used. They work well in most cases, but when it comes to heavy calculation, being memory efficient, it is slower due to the extra attributes which means there is more data to process every time you access the element.

:mag: If you want to learn more about NumPy, I recommend you to watch [this video](https://www.youtube.com/watch?v=QUT1VHiLmmI) from freeCodeCamp's YouTube Channel.

## If you know it's inefficient, why implement it? :smirk:

Short answer, just to learn and test if I'm able to hack things :gear: together and make it work, even if it's probably never going to be used.

It's a fun little project and it's under construction :construction: .