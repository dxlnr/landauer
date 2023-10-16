# Data Compression == AI

**The Task**: Losslessly compress the 1GB file enwik9 to less than 114MB. (Current Benchmark)

This compression contest ([Hutter Prize](http://prize.hutter1.net/)) is motivated by the fact that being able to compress well is closely related to acting intelligently, thus reducing the slippery concept of intelligence to hard file size numbers.

## Landauer's principle

[Landauer's principle](https://en.wikipedia.org/wiki/Landauer%27s_principle) is a physical principle pertaining to the lower theoretical limit of energy consumption of computation. It holds that an irreversible change in information stored in a computer, such as merging two computational paths, dissipates a minimum amount of heat to its surroundings. 

Landauer's principle states that the minimum energy needed to erase one bit of information is proportional to the temperature at which the system is operating. More specifically, the energy needed for this computational task is given by

$E \geq k_B T \ln 2$

where $k_B$ is the [Boltzmann constant](https://en.wikipedia.org/wiki/Boltzmann_constant). At room temperature, the Landauer limit represents an energy of approximately $0.018 eV$ ($2.9 \times 10−21 J$). Modern computers use about a billion times as much energy per operation. 

**How close is the brain?** And what is the opposite of the Landauer limit? And therefore, the limit of intelligence? How far off are we as the human species?

## Program

```bash
# configs
#
# -a <algorithm> Options: 'huffman'
# -d <input file>
python boiler.py -d data/enwik4 -a huffman
```

## Testing

Within and after development, there is a test script for evaluating the correctness of the different algorithms.
```bash
python -m unittest
```

## Additional Information
- [Hutter Prize](http://prize.hutter1.net/hfaq.htm): Frequently Asked Questions & Answers
- [Huffman Coding](https://en.wikipedia.org/wiki/Huffman_coding): Decent starting point for [lossless compression](https://en.wikipedia.org/wiki/Lossless_compression).
- [Arithmetic Coding](https://en.wikipedia.org/wiki/Arithmetic_coding) (AC) is a form of entropy encoding used in lossless data compression.
