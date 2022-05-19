# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            if item.name == "Sulfuras, Hand of Ragnaros":
                break

            if item.name == "Aged Brie":
                pass
                if item.quality < 50:
                    item.quality = item.quality + 1
                if item.sell_in < 1:
                    if item.quality < 50:
                        item.quality = item.quality + 1
                item.sell_in = item.sell_in - 1
                break

            if item.name == "Backstage passes to a TAFKAL80ETC concert":
                pass
                if item.quality < 50:
                    item.quality = item.quality + 1
                    if item.sell_in < 11:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 6:
                        if item.quality < 50:
                            item.quality = item.quality + 1
                    if item.sell_in < 1:
                        item.quality = 0
                item.sell_in = item.sell_in - 1
                break


            if item.quality > 0:
                pass
                #done
                item.quality = item.quality - 1

            if self.isOverdue(item):
                if item.quality > 0:
                    item.quality = item.quality - 1
          
            item.sell_in = item.sell_in - 1

    def isOverdue(self, item):
        return item.sell_in < 1


    def isBackstagePass(self, item):
        return item.name == "Backstage passes to a TAFKAL80ETC concert"


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)
