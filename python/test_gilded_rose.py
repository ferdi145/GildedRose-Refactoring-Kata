# -*- coding: utf-8 -*-
import unittest

from gilded_rose import Item, GildedRose


class GildedRoseTest(unittest.TestCase):

    def test_normal_item_with_positive_quality_looses_quality(self):
        items = [Item("foo", 1, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(9 , items[0].quality)

    def test_normal_item_with_positive_quality_and_overdue_looses_quality_at_double_rate(self):
        items = [Item("foo", 0, 10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(8 , items[0].quality)

    def test_normal_item_with_positive_quality_looses_quality(self):
        items = [Item("foo", sell_in=0, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0 , items[0].quality)

    def test_aged_brie_improves_quality(self):
        items = [Item("Aged Brie", sell_in=30, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2 , items[0].quality)

    def test_aged_brie_sell_in_date_reduces(self):
        items = [Item("Aged Brie", sell_in=30, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(29 , items[0].sell_in)


    def test_aged_brie_when_overdue_improves_double_quality(self):
        items = [Item("Aged Brie", sell_in=-1, quality=1)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3 , items[0].quality)

    def test_brie_item_with_50_cant_increase_quality(self):
        items = [Item("Aged Brie", sell_in=1, quality=50)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(50 , items[0].quality)

    def test_backstage_item_with_sellIn_10_increases_quality_by_two(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=10, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(2 , items[0].quality)

    def test_backstage_item_with_sellIn_10_increases_quality_by_three(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=5, quality=0)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(3 , items[0].quality)

    def test_backstage_item_with_sellIn_0_sets_quality_to_null(self):
        items = [Item("Backstage passes to a TAFKAL80ETC concert", sell_in=0, quality=10)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(0 , items[0].quality)

    def test_normal_item_with_positive_quality_looses_quality(self):
        items = [Item("Sulfuras, Hand of Ragnaros", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80 , items[0].quality)

    def test_normal_item_with_positive_quality_looses_quality(self):
        items = [Item("conjured", 1, 80)]
        gilded_rose = GildedRose(items)
        gilded_rose.update_quality()
        self.assertEqual(80 , items[0].quality)

if __name__ == '__main__':
    unittest.main()
