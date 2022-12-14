from abc import ABC, abstractmethod

import pygame
from loguru import logger

from models.enums.EnumActor import EnumActor
from models.enums.EnumBuilding import EnumBuilding
from views.resources.interfaces.IResourcesFactory import IResourcesFactory


class ResourcesFactoryImperius(IResourcesFactory):

    def __init__(self):
        super().__init__()

    def create_building(self, enum_building: EnumBuilding, level: int) -> pygame.Surface:
        result = None
        try:
            if enum_building == EnumBuilding.City:
                result = pygame.image.load(f'resources/Tribes/Imperius/City/Imperius city {level}.png')
            elif enum_building == EnumBuilding.Sawmill:
                result = pygame.image.load(f'resources/Buildings/Sawmill/Sawmill level {level}.png')
        except Exception as exc:
            logger.exception(exc)

        return result

    def create_actor(self, enum_actor: EnumActor) -> pygame.Surface:
        result = None
        try:
            result = pygame.image.load(f'resources/Tribes/Imperius/Units/warrior.png')
        except Exception as exc:
            logger.exception(exc)

        return result
