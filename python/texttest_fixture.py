# -*- coding: utf-8 -*-
from __future__ import print_function

from gilded_rose import *

EXPECTED = """
OMGHAI!-------- day 0 --------name, sellIn, quality+5 Dexterity Vest, 10, 20Aged Brie, 2, 0Elixir of the Mongoose, 5, 7Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 15, 20Backstage passes to a TAFKAL80ETC concert, 10, 49Backstage passes to a TAFKAL80ETC concert, 5, 49Conjured Mana Cake, 3, 6Aged Brie, -1, 49-------- day 1 --------name, sellIn, quality+5 Dexterity Vest, 9, 19Aged Brie, 1, 1Elixir of the Mongoose, 4, 6Sulfuras, Hand of Ragnaros, 0, 80Sulfuras, Hand of Ragnaros, -1, 80Backstage passes to a TAFKAL80ETC concert, 14, 21Backstage passes to a TAFKAL80ETC concert, 9, 50Backstage passes to a TAFKAL80ETC concert, 4, 50Conjured Mana Cake, 2, 5Aged Brie, -2, 50
""".strip()

buffer = ""

def print_to_buffer(given_text):
    global buffer
    buffer += given_text

if __name__ == "__main__":
    
    print_to_buffer("OMGHAI!")
    items = [
             Item(name="+5 Dexterity Vest", sell_in=10, quality=20),
             Item(name="Aged Brie", sell_in=2, quality=0),
             Item(name="Elixir of the Mongoose", sell_in=5, quality=7),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=0, quality=80),
             Item(name="Sulfuras, Hand of Ragnaros", sell_in=-1, quality=80),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=15, quality=20),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=49),
             Item(name="Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=49),
             Item(name="Conjured Mana Cake", sell_in=3, quality=6),  # <-- :O
             Item(name="Aged Brie", sell_in=-1, quality=49),
            ]

    days = 2
    import sys
    if len(sys.argv) > 1:
        days = int(sys.argv[1]) + 1
    for day in range(days):        
        print_to_buffer("-------- day %s --------" % day)
        print_to_buffer("name, sellIn, quality")
        for item in items:
            print_to_buffer(str(item))
        print_to_buffer("")
        GildedRose(items).update_quality()

    print('------------------BUFFER--------------------------')
    print(buffer.strip())
    print('-----------------EXPECTED-------------------------')
    print(EXPECTED)
    print('--------------------------------------------------')
    assert buffer.strip() == EXPECTED