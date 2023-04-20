import sys
from anvil import Region, Block

def test_get_set_block():
    print(Block)
    path = "C:\\Users\\wcherlet\\AppData\\Roaming\\.minecraft\\saves\\New World\\region\\"

    reg_file = path + "r.-1.-1.mca"

    region = Region.from_file(str(reg_file))

    dirt = Block('minecraft', 'dirt')

    region.set_block(dirt, -1, 0, -1)

    print(region.get_chunk(-1,-1).get_block(15,0,15))
    print(region.get_block(-1,0,-1))
    assert (region.get_chunk(-1,-1).get_block(15,0,15) == region.get_block(-1,0,-1))
    return

def test_save_region():
    path = "C:\\Users\\wcherlet\\AppData\\Roaming\\.minecraft\\saves\\New World\\region\\"

    reg_file = path + "r.-1.-1.mca"

    region = Region.from_file(str(reg_file))

    dirt = Block('minecraft', 'dirt')

    region.set_block(dirt, -1, 0, -1)

    region.save(str(reg_file))

    region2 = Region.from_file(str(reg_file))

    assert (region.get_block(-1,0,-1) == region2.get_block(-1,0,-1))
    return