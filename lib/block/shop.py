import pygame


from . import Block
from . import block_list
from ..plants import plants_list
from .. import shopGui


class Shop(Block.Block):
    is_shop_opne: bool = False
    name: str = "shop"
    price: int = 999999999

    def init(self):
        shopGui.init(block_list.block_list, plants_list.plants_list)

    def interact(self):
        self.is_shop_opne = not self.is_shop_opne
        print(self.is_shop_opne)
    
    def update(self):
        if self.is_shop_opne:
            shopGui.shop_open()
