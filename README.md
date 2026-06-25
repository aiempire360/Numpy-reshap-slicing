# NumPy Reshape and Array Slicing

This project demonstrates how to use NumPy's `reshape()` function and various array slicing techniques in Python.

## Topics Covered

* Creating NumPy arrays
* Reshaping one-dimensional arrays into two-dimensional arrays using `reshape()`
* Understanding array dimensions with `ndim`
* Accessing rows and columns
* Using positive and negative indexing
* Array slicing with `start:end:step`
* Selecting complete rows and columns
* Working with multi-dimensional arrays

## Examples Included

### Reshaping Arrays

Convert a 1D array into a 2D array:

```python
arr = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
arr = arr.reshape(3,4)
```

### Row Access

```python
arr1[1]
arr1[-1]
```

### Array Slicing

```python
arr1[0:2:3]
```

### Column Selection

```python
arr1[:,3]
```

### Row Selection

```python
arr1[1,:]
```

### Array Dimensions

```python
arr1.ndim
```

## Learning Objectives

By completing this project, you will learn:

* How NumPy reshapes arrays
* The relationship between array shape and dimensions
* How indexing works in multi-dimensional arrays
* How to extract specific rows and columns
* How slicing can efficiently retrieve subsets of data

## Technologies Used

* Python
* NumPy

## Output Demonstrations

The project prints:

* Array shapes
* Reshaped arrays
* Selected rows
* Selected columns
* Sliced data
* Number of dimensions (`ndim`)

This project is designed for beginners who are learning NumPy fundamentals and multidimensional array manipulation.
