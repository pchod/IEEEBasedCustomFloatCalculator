This file serves as a log for the considered programming options and issues along working with the project.

## Rounding rules
While working on the conversion from normalized form to IEEE fraction I encountered issue regarding the rounding rules. My initial approach was to calculate one bit after mantissa (guard bit),
but actually I need to revise my approach. In the first iteration I decided to use the following rounding rules:

- round to nearest;
- tie to even;

To implement this approach I am changing the implementation in the following manner:

- calculating 2 bits after the last needed for mantissa:
    - guard bit;
    - rounding bit;
    - sticky bit will be the bool flag, if the denominator after simplification is a power of 2 (i.e. will) it will be set to 0 (flag False) (not infinite extension) or 1 (flag True) for infinite extension;


