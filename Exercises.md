# Chapter 0. Number System

## 🔢 **Introduction to Number Systems**

In any number system, we use a set of digits (symbols) to represent numbers. The number of unique digits we use depends on the **base**.
For example:

* **Base 10 (Decimal)**: Uses digits 0 to 9
* **Base 2 (Binary)**: Uses digits 0 and 1
* **Base 8 (Octal)**: Uses digits 0 to 7

In this exercise sequence, you'll get to pick any base between **3 and 13**, and learn how to:

1. Count in that base
2. Add and subtract
3. Write multiplication tables
4. Multiply multi-digit numbers

---

### ✅ **Step 1: Choose Your Base (Between 3 and 13)**

👉 **Exercise 1:**
Pick a base between **3 and 13** (inclusive).
Let’s call it **Base `b`**.

For example:

* If you choose base 5, your digits will be: 0, 1, 2, 3, 4
* If you choose base 12, your digits will be: 0 to 9, then A (for 10), B (for 11)

> For bases higher than 10, we use letters like A=10, B=11, C=12, etc.

✍️ **Write down the digits used in your base.**
For example, in base 6: `0 1 2 3 4 5`

---

### ✅ **Step 2: Write Numbers up to 3 Digits in Your Base**

👉 **Exercise 2:**
Write **all numbers** from `0` to the largest **3-digit number in your base**.

**Explanation:**
In base `b`, a 3-digit number is of the form:

```
A * b² + B * b¹ + C * b⁰
```

Where A, B, C are digits from 0 up to `b-1`.

✅ **Example in base 4**:
Digits: 0, 1, 2, 3
Write all 3-digit numbers (from 000 to 333):

```
000, 001, 002, 003, 010, 011, 012, 013, ..., 333
```

✍️ **Your Task:**
Write down at least 15 3-digit numbers in your base.

---

### ✅ **Step 3: Add and Subtract Single-Digit Numbers in Your Base**

👉 **Exercise 3A: Add all pairs of single-digit numbers in your base**

**Explanation:**
Add two digits and express the result in your base. If the sum is ≥ base, carry over.

✅ **Example in base 5**:

```
3 + 4 = 7 → In base 5: 7 = 1 * 5 + 2 → Answer = 12 (1 carry, 2 below)
```

👉 **Exercise 3B: Subtract all possible pairs of digits**

**Explanation:**
Make sure the result is never negative.
If the first digit is smaller, skip or indicate "not allowed without borrowing".

✅ **Example in base 6**:

```
5 - 2 = 3 → In base 6: still 3
2 - 5 → Not allowed without borrowing
```

✍️ **Your Task:**
Create two tables:

* Addition table: all combinations of digits
* Subtraction table: only where first digit ≥ second digit

---

### ✅ **Step 4: Add and Subtract Multi-Digit Numbers**

👉 **Exercise 4A: Add two 2-digit numbers in your base**

**Example in base 6**:

```
35₆ + 24₆
Step-by-step:
5 + 4 = 9 → 9 = 1 * 6 + 3 → Write 3, carry 1
3 + 2 + 1 (carry) = 6 → 6 = 1 * 6 + 0 → Write 0, carry 1
Result: 103₆
```

👉 **Exercise 4B: Subtract two 2-digit numbers**

**Example in base 7**:

```
52₇ - 34₇ → Convert digits, subtract with borrowing if needed
```

✍️ **Your Task:**
Solve at least 3 addition and 3 subtraction problems involving two-digit numbers.

---

### ✅ **Step 5: Write Multiplication Table in Your Base**

👉 **Exercise 5:**
Create the **multiplication table** for your base up to (b - 1) × (b - 1)

**Explanation:**
Multiply each pair of digits, then convert the result to your base.

✅ **Example in base 4**:

```
2 × 3 = 6 → In base 4: 6 = 1 * 4 + 2 → Answer = 12
```

✍️ **Your Task:**
Make a full multiplication table (rows and columns from 0 to b-1)

---

### ✅ **Step 6: Multiply Two-Digit Numbers in Your Base**

👉 **Exercise 6:**
Multiply two 2-digit numbers in your base

**Example in base 5**:
Multiply 13₅ × 21₅
Steps:

1. Multiply digits as in long multiplication
2. Convert intermediate products to base 5
3. Add all rows (in base 5)

✅ **Step-by-step (summary)**:

* Multiply ones place
* Multiply tens place and shift one place left
* Add rows in base

✍️ **Your Task:**
Multiply at least 2 pairs of 2-digit numbers in your base.


# Chapter 1. Python Expressions and Functions:

## Calculate Interest

### **Topic:** *Calculate Interest*

#### **Explanation:**

When someone deposits or borrows money, the amount often grows over time due to *interest*. There are two common types of interest: **Simple Interest** and **Compound Interest**.

In this exercise, we'll focus on **Simple Interest**.

* **Principal (P):** The original amount of money deposited or borrowed.
* **Rate of Interest (R):** The percentage charged or earned on the principal each year.
* **Time (T):** The number of years the money is deposited or borrowed for.

The formula to calculate **Simple Interest** is:

```
Interest = (Principal × Rate × Time) / 100
```

This gives us the amount of money earned or paid as interest after the given time.

#### **Problem Statement:**

Write a function named `calculate_interest` that takes the following three arguments:

* `principal` (amount of money deposited or borrowed),
* `rate` (rate of interest per year, as a percentage),
* `time` (duration in years),

and returns the simple interest calculated using the formula above.

#### **Example Usage:**

```python
calculate_interest(1000, 5, 2)   # Output: 100.0
calculate_interest(1500, 4.3, 3) # Output: 193.5
calculate_interest(500, 10, 0)   # Output: 0.0
```


## Calculate Hypotense

### 🧠 Topic: **Calculate Hypotenuse**

#### 📘 Understanding the Terms (in simple language):

When you have a right-angled triangle (a triangle where one of the angles is exactly 90 degrees), the longest side of the triangle is called the **hypotenuse**. It’s the side that is **opposite the right angle**.

The other two sides (the ones that make the right angle) are usually called the **base** and the **height** (or **perpendicular**).

To calculate the length of the hypotenuse, we use something called the **Pythagorean Theorem**.

The formula is:

```
hypotenuse² = base² + height²
```

To find the hypotenuse, we need to take the square root of the sum of the squares of the base and height:

```
hypotenuse = √(base² + height²)
```

#### 🔧 Task:

Write a function named `calculate_hypotenuse` that takes two arguments:

* `base`: the length of the base (a number)
* `height`: the length of the height/perpendicular side (a number)

It should return the length of the hypotenuse (a number).

Use the formula:

```
hypotenuse = (base² + height²) ** 0.5
```

#### 💡 Examples:

```python
Input: calculate_hypotenuse(3, 4)
Output: 5.0
```

Why?
Because √(3² + 4²) = √(9 + 16) = √25 = 5.0

---

```python
Input: calculate_hypotenuse(5, 12)
Output: 13.0
```

Why?
Because √(25 + 144) = √169 = 13.0

---

```python
Input: calculate_hypotenuse(0, 0)
Output: 0.0
```

## Find Distance 2D

**Topic:** *Find Distance in 2D*

### 🧠 Explanation:

In everyday life, when we move from one place to another, we cover a certain *distance*. In math, especially in geometry, we often want to calculate the distance between two points on a flat surface (called a 2D plane).

Each point on this plane can be represented by two numbers:

* the **x-coordinate** (horizontal position)
* the **y-coordinate** (vertical position)

Come up with the formula to calculate the distance between two points $(x1, y1)$ and $(x2, y2)$ based on the **Pythagorean Theorem**, just like finding the hypotenuse of a right triangle.

---

### ✍️ Exercise:

Write a function `find_distance_2d(x1, y1, x2, y2)` that returns the distance between the two points. Use the formula mentioned above. You can use the `math.sqrt` function to calculate the square root.

---

### 💡 Examples:

```python

find_distance_2d(0, 0, 3, 4)     # Output: 5.0
find_distance_2d(1, 2, 4, 6)     # Output: 5.0

```

## Find Distance 3D

**Topic:** *Find Distance in 3D*

---

### 🧠 **Explanation:**

In everyday life, we often measure the distance between two points—like how far your house is from school. In **3D space**, we do the same, but we also consider height or depth in addition to length and width.

A point in 3D space is defined using three coordinates:

* `x` (horizontal)
* `y` (vertical)
* `z` (depth)

To calculate the **distance between two points** in 3D, say:

* Point A: `(x1, y1, z1)`
* Point B: `(x2, y2, z2)`

Come up with 3D distance formula using the Pythagorean theorem into three dimensions.

---

### 🧪 **Exercise:**

Write a function called `calculate_distance_3d(x1, y1, z1, x2, y2, z2)` that returns the distance between two 3D points.

* The function should return the result as a float.
* You can use the built-in `math.sqrt()` function to calculate the square root.

---

### ✅ **Examples:**

```

calculate_distance_3d(0, 0, 0, 1, 1, 1)  # Output: 1.7320508075688772
calculate_distance_3d(2, 3, 5, 2, 3, 5)  # Output: 0.0
calculate_distance_3d(1, 2, 3, 4, 6, 9)  # Output: 7.810249675906654

```


## Find Manhattan Distance

### **Topic:** *Find Manhattan Distance*

---

### **Explanation:**

When you want to measure the distance between two points on a grid (like in a city with square blocks), you don’t move diagonally. Instead, you move only **horizontally** and **vertically**, like a taxi driving along streets and avenues. This kind of distance is called the **Manhattan Distance**.

The formula to calculate the Manhattan Distance between two points $(x1, y1)$ and $(x2, y2)$ is:

$$
\text{Manhattan Distance} = |x1 - x2| + |y1 - y2|
$$

Here, $|a|$ means the absolute value of $a$ — in other words, how far the number is from zero.

For example:

* From (2, 3) to (5, 1):
$|2 - 5| = 3$ and $|3 - 1| = 2$, so distance = $3 + 2 = 5$

---

### **Exercise:**

Write a function `manhattan_distance(x1, y1, x2, y2)` that takes the coordinates of two points and returns their Manhattan Distance.

---

### **Example:**

```python
manhattan_distance(2, 3, 5, 1)  # Output: 5
manhattan_distance(0, 0, 0, 0)  # Output: 0
manhattan_distance(-1, -1, 1, 1)  # Output: 4
```


## Write a function to return value of y given x on a straight line in 2D. It should take three arguments: m, c, x. 

### **Topic:** *Predict Y on a Straight Line (2D)*

---

### **Simple Explanation:**

In math, a straight line in 2D is usually written in this form:

```
y = m * x + c
```

Here’s what the terms mean:

* `x` is the input (like a point on the horizontal axis).
* `y` is the output (like a point on the vertical axis).
* `m` is the *slope* of the line, which tells us how steep the line is.
* `c` is the *intercept*, or where the line crosses the y-axis.

For example:
If `m = 2`, `c = 3`, and `x = 4`, then:

```
y = 2 * 4 + 3 = 8 + 3 = 11
```

So, the value of `y` is `11`.

---

### **Exercise:**

Write a function `predict(m, c, x)` that returns the value of `y` based on the formula:

```
y = m * x + c
```

#### **Arguments:**

* `m` – slope of the line (a number)
* `c` – y-intercept of the line (a number)
* `x` – the x-coordinate (a number)

#### **Return:**

* The value of `y` calculated from the formula `y = m * x + c`

---

### **Example Usage:**

```python
predict(2, 3, 4)     # Output: 11
predict(-1, 5, 2)    # Output: 3
```


## Given two points, write a function fit() to learn slope and intercept of the line going through them

### **Topic:** *Learn Line Equation from Two Points*

### **Explanation:**

A straight line in a 2D plane can be described by the equation:

$$
y = mx + c
$$

Where:

* `m` is the **slope** of the line.
* `c` is the **intercept** — the value of `y` when `x = 0`.

If you're given **two points** on the line, say `(x1, y1)` and `(x2, y2)`, you can calculate the **slope** `m` like this:

$$
m = \frac{y2 - y1}{x2 - x1}
$$

Once you have the slope, you can use one of the points (say `(x1, y1)`) to calculate the intercept `c` using:

$$
c = y1 - m \times x1
$$

For example, if your two points are (1, 2) and (3, 6):

* Slope: `(6 - 2)/(3 - 1) = 4/2 = 2`
* Intercept: `2 - (2 × 1) = 0`
* So, the equation of the line is: `y = 2x + 0`

---

### **Exercise:**

Write a function `fit(x1, y1, x2, y2)` that returns a tuple `(m, c)` representing the slope and intercept of the line passing through the two points `(x1, y1)` and `(x2, y2)`.

---

### **Function Signature:**

```python
def fit(x1, y1, x2, y2):
    # Your code here
```

---

### **Example:**

```python
fit(1, 2, 3, 6)       # Output: (2.0, 0.0)
fit(0, 5, 2, 9)       # Output: (2.0, 5.0)
```

> 💡 **Hint:** Make sure `x1` is not equal to `x2`, otherwise the slope would be undefined (vertical line). You may handle this case as you see fit.


## find first derivate of a function that takes only one argument. 

### **Topic:** *Find First Derivative of a Function*

#### **Simple Explanation:**

In mathematics, the *derivative* of a function tells us how fast the function's value is changing at a particular point.

Think of it like this: if you’re driving a car and your distance changes every second, then your speed is the derivative of your distance. Similarly, for any function, the derivative gives the *rate of change*.

We’ll use a simple numerical technique called the **difference method**:

$$
f'(x) \approx \frac{f(x + h) - f(x)}{h}
$$

This is called the **forward difference method**, where `h` is a very small number.

---

### **Exercise:**

Write a function `approx_derivative(func, x, h)` that:

* Takes a function `func` that accepts a single argument,
* A value `x` where we want to find the derivative,
* And a small number `h` (like `0.0001`),
* Returns the approximate derivative of `func` at `x`.

---

### **Example Usage:**

```python
def square(x):
    return x * x

def cube(x):
    return x * x * x

print(approx_derivative(square, 3, 0.0001))  # Output: Approx. 6
print(approx_derivative(cube, 2, 0.0001))    # Output: Approx. 12
```

---

### **Note to Learner:**

Try different values of `x` and different functions (like `math.sin`, `math.exp`, etc.) to see how the derivative changes.

Make sure to import any libraries (like `math`) if needed.


# Chapter 2. if - else
## Huber Distance

### **Topic:** *Compute Huber Distance Between Two Points in 2D*

---

### **Explanation:**

The **Huber distance** is a robust way to measure the difference between two points. It combines the benefits of:

* **Squared distance** for small differences (smooth and differentiable near zero).
* **Linear distance** for large differences (less sensitive to outliers).

For two points in **2D space**:

* Represent each point as `(x, y)`.
* First, compute the **Euclidean distance** between the points.
* Apply the Huber idea:

  * If the distance $d \le \delta$, use a **quadratic function** of $d$.
  * If the distance $d > \delta$, use a **linear function** of $d$, but make sure the function is **continuous** at $d = \delta$.

**Important:**
At $d = \delta$, both formulas should return the **same value**. This ensures a smooth transition.

---

### **Exercise:**

Write a function `compute_huber_distance_2d(p1, p2, delta)` that:

* Inputs:

  * `p1`: first point as `(x1, y1)`
  * `p2`: second point as `(x2, y2)`
  * `delta`: threshold where the formula switches from quadratic to linear
* Returns:

  * The **Huber distance** between the two points.

---

#### **Steps to guide you:**

1. Compute the **Euclidean distance**:

   $$
   d = \sqrt{(x_1 - x_2)^2 + (y_1 - y_2)^2}
   $$
2. If $d \le \delta$, compute:

   $$
   \text{distance} = 0.5 \times d^2
   $$
3. If $d > \delta$, compute:

   $$
   \text{distance} = \delta \times (d - 0.5 \times \delta)
   $$

   **Hint:** This formula ensures continuity because at $d = \delta$, both formulas give:

   $$
   0.5 \times \delta^2
   $$

---

### **Example Usage:**

```python
compute_huber_distance_2d((0, 0), (1, 1), 1.5)   # Expected: ~1.0 (quadratic region)
compute_huber_distance_2d((0, 0), (3, 4), 1.5)   # Expected: > linear region
compute_huber_distance_2d((2, 3), (2, 3), 2)     # Expected: 0.0
```


## Check if a point P is closer to point A or point B in 2D

### **Topic:** *Check if a Point is Closer to A or B in 2D*

### **Explanation:**

In a 2D plane, a **point** is defined by its coordinates, usually written as (x, y). The **distance** between two points tells us how far apart they are.

For example, if we have:

* Point A = (x₁, y₁)
* Point B = (x₂, y₂)
* Point P = (x, y)

We want to find out which point — A or B — is **closer** to point P.

To figure this out, we calculate the distance from P to both A and B and then compare them. You don't need to use square roots — just compare the **squared distances** (it’s faster and gives the same result for comparison).

---

### **Exercise:**

Write a function `closer_point(p, a, b)` that takes:

* `p`: a tuple representing the coordinates of point P
* `a`: a tuple representing the coordinates of point A
* `b`: a tuple representing the coordinates of point B

The function should return:

* `'A'` if P is closer to A
* `'B'` if P is closer to B
* `'Equal'` if the distances are the same

---

### **Example:**

```python
closer_point((1, 2), (0, 0), (5, 5))     # Output: 'A'  
closer_point((4, 4), (0, 0), (8, 8))     # Output: 'Equal'  
closer_point((7, 3), (2, 3), (10, 3))    # Output: 'B'
```


## Is point on line?

### **Topic:** *Is Point P on Line in 1D?*

---

### **Simple Explanation:**

In one-dimensional space (like a number line), a line segment is just the portion between two points — for example, between point A and point B.

We want to check whether a third point P lies *on* this segment. That means P should be:

* Greater than or equal to the smaller of A and B, **and**
* Less than or equal to the larger of A and B.

In simple terms, P is “between” A and B — or equal to one of them.

For example:

* If A = 2, B = 5, and P = 3 → P is between 2 and 5 → ✅
* If A = -5, B = -2, and P = -3 → P is between -5 and -2 → ✅
* If A = -5, B = -2, and P = -6 → P is outside the range → ❌
* If A = 2, B = 5, and P = 2 → P is between 2 and 5 → ✅

It doesn’t matter whether A is smaller than B or the other way around — we always check the range between them.

---

### **Exercise:**

Write a function `is_point_on_line_1d(a, b, p)` that returns `True` if point `p` lies on the line segment between `a` and `b`, and `False` otherwise.

---

### **Example Usage:**

```python
is_point_on_line_1d(2, 5, 3)      # Output: True  
is_point_on_line_1d(5, 2, 3)      # Output: True  
is_point_on_line_1d(2, 5, 6)      # Output: False  
is_point_on_line_1d(4, 4, 4)      # Output: True  (A single point segment)
is_point_on_line_1d(4, 4, 5)      # Output: False

# With negative numbers:
is_point_on_line_1d(-5, -2, -3)   # Output: True  
is_point_on_line_1d(-5, -2, -6)   # Output: False  
is_point_on_line_1d(-2, -5, -4)   # Output: True  
is_point_on_line_1d(-1, 3, 0)     # Output: True
```

## Are two lines overlapping or touching in 1D

### **Topic:** *Are Two Lines Overlapping or Touching in 1D*

---

### 🧠 **Simple Explanation:**

Imagine a number line — just a straight line with numbers going from negative to positive. You can draw a line segment between two points, like from -3 to 2. This segment includes every number between -3 and 2.

Now, suppose you have **two such line segments**. You want to check:

* Do they **overlap** (share some part)?
* Do they **touch** (meet at exactly one point)?
* Or are they **completely separate**?

For example:

* Line A: from -3 to 1
* Line B: from 0 to 4
  They **overlap**, because they both include 0 and 1.

Or:

* Line A: from -5 to -2
* Line B: from -2 to 3
  They **touch** at -2.

---

### 📘 **Exercise:**

Write a function `are_lines_touching_or_overlapping(start1, end1, start2, end2)` that returns `True` if the two 1D line segments are overlapping or touching, and `False` if they are completely separate.

📌 Make sure your function works correctly even if the start is greater than the end — the order shouldn't matter.

---

### 🔍 **Example Usage:**

```python
are_lines_touching_or_overlapping(1, 4, 3, 6)        # Output: True   (Overlap from 3 to 4)
are_lines_touching_or_overlapping(1, 3, 3, 5)        # Output: True   (Touch at point 3)
are_lines_touching_or_overlapping(1, 2, 3, 4)        # Output: False  (Completely separate)

# Examples with negative numbers
are_lines_touching_or_overlapping(-3, 1, 0, 4)       # Output: True   (Overlap from 0 to 1)
are_lines_touching_or_overlapping(-5, -2, -2, 3)     # Output: True   (Touch at point -2)
are_lines_touching_or_overlapping(-10, -6, -5, -1)   # Output: False  (No touch or overlap)
are_lines_touching_or_overlapping(-2, -7, -4, -3)    # Output: True   (Overlap from -4 to -3, even with reversed inputs)
```

## Is a point inside a rectangle?

**Topic:** *Is a Point Inside a Rectangle (with Sides Parallel to the Axes)?*

---

### 🧠 **Explanation:**

In geometry, a **rectangle** is a shape with four sides and four right angles. When the sides of a rectangle are **parallel to the x and y axes**, it means the edges of the rectangle are either **horizontal or vertical**—not slanted.

To describe such a rectangle, we only need two opposite corners:

* The **bottom-left corner** (`x1`, `y1`)
* The **top-right corner** (`x2`, `y2`)

A **point** has two values: `x` and `y`—its horizontal and vertical positions.

To check if a point lies **inside** (or on the border of) the rectangle, we see if:

* The `x` value of the point is between `x1` and `x2`, and
* The `y` value of the point is between `y1` and `y2`.

This assumes `x1 < x2` and `y1 < y2` (which means the first point is bottom-left and the second is top-right).

---

### ✅ **Exercise:**

Write a function `is_point_inside_rectangle(x1, y1, x2, y2, px, py)` that returns `True` if the point `(px, py)` lies inside or on the boundary of the rectangle defined by corners `(x1, y1)` and `(x2, y2)`, and `False` otherwise.

---

### 🔍 **Example Usage:**

```python
is_point_inside_rectangle(0, 0, 10, 5, 3, 2)   # Output: True
is_point_inside_rectangle(0, 0, 10, 5, 10, 5)  # Output: True  (point on the corner)
is_point_inside_rectangle(0, 0, 10, 5, 11, 5)  # Output: False (outside the rectangle)
is_point_inside_rectangle(-5, -5, 5, 5, 0, 0)  # Output: True  (inside a rectangle with negative coordinates)
```

Note: **try with negative numbers** and **boundary points** to test your understanding.


## Are rectangles (with sides parallel to axes) intersecting?

### **Topic:** *Are Rectangles Intersecting?*

---

### **Explanation:**

A **rectangle** on a 2D plane can be defined by its two opposite corners — the bottom-left and the top-right. For example, suppose a rectangle has its bottom-left corner at (1, 2) and top-right corner at (4, 5). This rectangle stretches from x = 1 to x = 4 and from y = 2 to y = 5.

Two rectangles are said to **intersect** if they share **any area** — even a single point on their boundary counts. If one is completely to the left, right, above, or below the other, then they **do not intersect**.

---

### **Exercise:**

Write a function `are_rectangles_intersecting(rect1, rect2)` that takes two rectangles and returns `True` if they intersect, otherwise returns `False`.

Each rectangle is represented as a tuple of two points:
`((x1, y1), (x2, y2))`, where

* `(x1, y1)` is the **bottom-left corner**
* `(x2, y2)` is the **top-right corner**

#### **Function Signature:**

```python
def are_rectangles_intersecting(rect1: tuple, rect2: tuple) -> bool:
```

---

### **Example Usage:**

```python
# Rectangles overlap partially
are_rectangles_intersecting(((0, 0), (3, 3)), ((2, 2), (5, 5)))  
# Output: True

# One rectangle is completely to the right of the other
are_rectangles_intersecting(((0, 0), (1, 1)), ((2, 2), (3, 3)))  
# Output: False

# Touching at corner
are_rectangles_intersecting(((0, 0), (2, 2)), ((2, 2), (4, 4)))  
# Output: True

# One rectangle inside another
are_rectangles_intersecting(((0, 0), (5, 5)), ((1, 1), (2, 2)))  
# Output: True
```

---

### ✅ **Note to Learners:**

Try to reason geometrically:
Two rectangles **do not intersect** if:

* One is entirely to the **left** of the other
* One is entirely to the **right** of the other
* One is entirely **above** the other
* One is entirely **below** the other

If none of these cases apply, the rectangles must intersect!

## Device impurity formula for a set with only two classes given the counts of each class.
**Topic:** *Devise Your Own Impurity Formula*

---

### **Explanation (Simple Terms)**

When we try to split data into two groups in machine learning (especially in decision trees), we want to know how “mixed” a set is — meaning how many items from different classes are in the same set. This “mixed-ness” is called *impurity*.

* If all the items are from the **same class**, the set is **pure** — impurity is **0**.
* If the items are **equally split between two classes**, the set is **maximally impure** — impurity is **high**.

You might have heard of common impurity measures like **Gini Index** or **Entropy**, but in this exercise, you will **create your own** formula for impurity using the counts of the two classes.

---

### **Exercise**

Write a function `my_impurity(c1, c2)` that calculates the impurity of a set containing two classes:

* `c1` is the number of examples from **class 1**
* `c2` is the number of examples from **class 2**

You should **devise your own formula** to calculate impurity. Your formula must meet these conditions:

1. If all items are from one class (`c1 = 0` or `c2 = 0`), impurity should be `0`.
2. The impurity should increase as the classes become more evenly balanced.
3. The impurity should be **maximum** when `c1 == c2`.

You may use arithmetic operators like `+`, `-`, `*`, `/`, and functions like `abs()` if needed.

---

### **Function Signature**

```python
def my_impurity(c1, c2):
    # your formula here
    return impurity_value
```

---

### **Example Usage**

Assuming you devise this impurity formula:
`impurity = (2 * min(c1, c2)) / (c1 + c2)`

Then:

```python
my_impurity(0, 5)     # Output: 0.0
my_impurity(5, 5)     # Output: 1.0
my_impurity(7, 3)     # Output: 0.6
my_impurity(9, 1)     # Output: 0.2
```

Try a few formulas. Test and compare their outputs. Pick one that makes sense to you and meets the conditions above.

---

**Bonus Challenge:**
Can you design a formula that gives values between 0 and 1 **and** changes smoothly with the ratio of the classes?


---

# Chapter 3. If - Else + Recursion:

## Factorial using recursion

**Topic:** *Factorial using Recursion*

---

### **Simple Explanation:**

A **factorial** of a number is the result of multiplying all whole numbers from that number down to 1.

For example:

* The factorial of 5 is: `5 × 4 × 3 × 2 × 1 = 120`
* The factorial of 3 is: `3 × 2 × 1 = 6`
* The factorial of 1 is: `1`

The factorial of 0 is defined as **1** (by convention).

Now, there's a smart way to compute factorials using something called **recursion**. In recursion, a function calls itself with a smaller input to eventually solve a problem.

Example logic:

* factorial(5) = 5 × factorial(4)
* factorial(4) = 4 × factorial(3)
* ...
* factorial(1) = 1 (this is called the *base case*)

So it keeps breaking the problem into smaller parts until it reaches 1.

---

### **Exercise:**

Write a function `factorial_recursive(n)` that takes one argument `n` (a non-negative integer) and returns the factorial of that number using recursion.

If `n` is 0, the function should return 1.

---

### **Example:**

```python
factorial_recursive(5)  # Output: 120  
factorial_recursive(3)  # Output: 6  
factorial_recursive(0)  # Output: 1  
factorial_recursive(1)  # Output: 1  
```

> 💡 *Hint for learners:* Think about how you can express `factorial(n)` using `factorial(n-1)`. Also, make sure to stop when `n` reaches 0 or 1 — that's your base case.


## Compute HCF using Euclid's Method with Recursion*

**Topic:** *Compute HCF using Euclid's Method with Recursion*

---

### **Explanation:**

HCF stands for **Highest Common Factor**, also known as **GCD (Greatest Common Divisor)**. It is the largest number that evenly divides two numbers.

For example:

* The HCF of 12 and 18 is 6, because 6 is the biggest number that divides both 12 and 18 without a remainder.

**Euclid’s Method** is a smart and efficient way to compute the HCF. It works like this:

* If `b` is 0, the HCF is `a`.
* Otherwise, HCF of `a` and `b` is the same as the HCF of `b` and `a % b`.

This method keeps reducing the problem until it finds the HCF. We can use **recursion** to apply this method repeatedly until we get the answer.

---

### **Exercise:**

Write a function named `compute_hcf(a, b)` that takes two positive integers `a` and `b` and returns their HCF using Euclid's method with recursion.

* You should **use recursion** to solve this problem.
* The function should return an integer.

---

### **Example Usage:**

```python
compute_hcf(12, 18)     # Output: 6
compute_hcf(100, 25)    # Output: 25
compute_hcf(17, 13)     # Output: 1
compute_hcf(0, 5)       # Output: 5
```

> 💡 *Hint: Try to express the logic using the rule: HCF(a, b) = HCF(b, a % b)*
> Remember that recursion means your function will call itself with smaller values until it reaches a stopping point.


## Multiplication using recursion

### **Topic:** *Multiplication using Recursion*

#### **Simple Explanation:**

Multiplication means adding a number to itself a certain number of times.
For example, 4 multiplied by 3 means:
`4 + 4 + 4 = 12`.

Recursion means a function that calls itself to solve smaller versions of the same problem.
Instead of using the `*` (multiplication) operator directly, you can use recursion to repeatedly add a number.

So, to multiply `a` and `b`, you can add `a` to the result of multiplying `a` and `b-1`.

Also, consider that:

* If `b` is 0, the result is 0 (anything multiplied by 0 is 0).
* If `b` is negative, handle it by converting to positive, and then negating the result.

---

### **Exercise:**

Write a function `multiply_recursive(a, b)` that multiplies two integers using recursion (without using the `*` operator).

* `a`: the first number (int)
* `b`: the second number (int)

Return the product of `a` and `b`.

---

### **Example Usage:**

```python
multiply_recursive(4, 3)     # Output: 12
multiply_recursive(5, 0)     # Output: 0
multiply_recursive(7, -2)    # Output: -14
multiply_recursive(-3, -3)   # Output: 9
```


## Division using recursion to find quotient and remainder

### **Topic:** *Division using Recursion to Find Quotient and Remainder*

#### **Simple Explanation:**

Division is the process of finding how many times one number (called the **divisor**) fits into another number (called the **dividend**).
For example, in `17 ÷ 5`, the number 5 fits into 17 **three** times (that’s the **quotient**) and there are **2** left over (that’s the **remainder**), because:

```
5 + 5 + 5 = 15, and 17 - 15 = 2  
So, 17 ÷ 5 gives quotient = 3 and remainder = 2
```

**Recursion** means solving a problem by breaking it into smaller versions of the same problem. In this case, we repeatedly subtract the divisor from the dividend and count how many times we do it until what’s left is smaller than the divisor (that’s the remainder).

---

### **Exercise:**

Write a function `recursive_divide(dividend, divisor)` that returns a tuple `(quotient, remainder)` using recursion.
You **must not** use the `//` or `%` operators.

* `dividend`: a non-negative integer
* `divisor`: a positive integer

**Return:** A tuple of two integers: `(quotient, remainder)`

---

### **Example Usage:**

```python
recursive_divide(17, 5)   # Output: (3, 2)
recursive_divide(20, 4)   # Output: (5, 0)
recursive_divide(7, 3)    # Output: (2, 1)
recursive_divide(0, 1)    # Output: (0, 0)
```

## Tower of hanoi

# Chapter 4. Loops and Array

## Compute mean
## Compute SD
## Compute root mean square error in n-dimensions
## Compute mean absolute error  in n-dimensions
## Compute huber loss in n-dimensions
## Check if a point P is closer to point A or point B in N-Dimension
## Compute Sqrt
## Compute CubeRoot
## Compute nth Root
## Compute Log base 10, you can use ** for power.
## Compute log base n, you can use ** for power.

# Chapter 6. Dictionary and Sets

# Chapter 5. Objects and Classes

# Chapter 7. Binary Search

# Chapter 8. Sorting

# Chapter 9: Regression

    ## Solve Equations - Gaussian Elimination

        ### Build a fit() & predict() for two points with one feature. Manually.
            y = mx + c, (x1, y1) and (x2, y2)
        
        ### Solve equations - One variable Equation, A*x = B
            solve([[a b]])
        ### Solve equations -  two variables Equation. First eliminate one variable and then use the previous function. 
            - a*x + b*y = c
            - a1*x + b1*y = c1
        
        ### Solve n Equations.
        ### Solve Equations - y = a*x1 + b*x2 + c*x3 + d using above method.

        ### Build a fit() & predict() for n points with n features.
        ### Build a fit() & predict() with y = a*x*x + b*x + c. One feature and three equations

    ## Approximations
    ### What is the minimum value of y = 2*x^2 - 5x + 10 ? try using hit and trial
    ### Write an algorithm to find minimum of second degree polynomial with coeffs [a, b, c].


