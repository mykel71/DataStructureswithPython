"""
Calculate the Product Sum from a Special Array.
Pyhton doctests can be run with the following commands:
python -m doctest -v ProductSum.py

Calculate the product sum of a "special" array which can contain integers or nested arrays.
The product sum is obtained by adding all elements and multiplying by their respective depths.

For Example, in array [x, y], the product sum is (x + y). In the array [x, [y, z]],
the product sum is x + 2 * (y + z). In the array [x, [y, [z]]],
the product sum is x + 2 * (y + 3z).

Example input:
[5, 2, [-7, 1], 3, [6, [-13, 8], 4]]
Output: 12

"""