# IEEEBasedCustomFloatCalculator

The project converts the denary numbers (either in fractional or decimal point format)
into the one of the IEEE 754 float representation formats and vice versa. IEEE formats to choose:
- binary16;
- binary32;
- binary64;
- custom-length format with arbitrary exponent and mantissa length chosen by the user;

The program will handle normal and subnormal representations along with special cases.

Conversion denary numbers into IEEE 754 representation for arbitrary exponent and mantissa lengths is a common exercise for the computer science students - while
there is a lot of IEEE 754 calculators available on the web it was impossible to find the calculator to reliably check
conversion to custom-length binary strings following IEEE 754 guidelines and rules of calculation.

The UI part will be designed in flask, while the whole backend I wrote in vanilla python.

## Status

🚧 In Progress 🚧

The project is still in progress - the planned date of deploment is 31st of January 2024. Parts of the logic had underwent
unit tests and work as designed.

## Technical Overview


