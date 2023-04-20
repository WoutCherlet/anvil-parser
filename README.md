# anvil-parser

Simple parser for the [Minecraft anvil file format](https://minecraft.gamepedia.com/Anvil_file_format), updated to work with new chunk and region formats.
# Installation
The original project is available on [PyPI](https://pypi.org/project/anvil-parser/) and can be installed with pip
```
pip install anvil-parser
```
To write chuncks and regions in 1.16 and up, install from github
```
pip install git+https://github.com/WoutCherlet/anvil-parser.git
```
# Usage
## Reading
```python
import anvil

region = anvil.Region.from_file('r.0.0.mca')

# You can also provide the region file name instead of the object
chunk = anvil.Chunk.from_region(region, 0, 0)

# If `section` is not provided, will get it from the y coords
# and assume it's global
block = chunk.get_block(0, 0, 0)

print(block) # <Block(minecraft:air)>
print(block.id) # air
print(block.properties) # {}
```
## Making own regions
```python
import anvil
from random import choice

# Create a new region with the `EmptyRegion` class at 0, 0 (in region coords)
region = anvil.EmptyRegion(0, 0)

# Create `Block` objects that are used to set blocks
stone = anvil.Block('minecraft', 'stone')
dirt = anvil.Block('minecraft', 'dirt')

# Make a 16x16x16 cube of either stone or dirt blocks
for y in range(16):
    for z in range(16):
        for x in range(16):
            region.set_block(choice((stone, dirt)), x, y, z)

# Save to a file
region.save('r.0.0.mca')
```
# Note
Tested for version 1.19

# TODO's 

- Biome encode/decode
- Read/Write regions
- RW chunk
- RW section (already there?)
