from library.Lowlevelib import *
from library.libtypes import *
from library.libgfx import *
from library.libui import *


from typing import overload
from typing import Tuple


class Rect(Vector2):
    @overload
    def __init__(self, x: float, y: float, w: float, h: float) -> "Rect":
        ...

    @overload
    def __init__(self, pos: Tuple[float, float], size: Tuple[float, float]) -> "Rect":
        ...

    def __init__(self, *args):
        self.__args_wrapper(*args)

    def __args_wrapper(self, *args):
        if len(args) == 4:
            _x = args[0]
            _y = args[1]
            self._w = args[2]
            self._h = args[3]
        elif len(args) == 2:
            _x = args[0][0]
            _y = args[0][1]
            self._w = args[1][0]
            self._h = args[1][1]
        super().__init__(_x, _y)

    def draw(self, win: Window):
        Draw.draw_rect(win, self.xy, self.wh, "red", 1)

    def collide_point(self, point: Tuple[float, float] | Vector2) -> bool:
        px, py = 0, 0
        if isinstance(point, Vector2):
            px = point.x
            py = point.y
        if isinstance(point, (list, tuple)):
            px = point[0]
            py = point[1]

        if (
            self.x < px
            and px < self.x + self.w
            and self.y < py
            and py < self.y + self.h
        ):
            return True

        return False

    def collide_rect(self, rect: "Rect", win: None = None):
        min_x = min(self.x, rect.x)
        min_y = min(self.y, rect.y)

        max_x = max(self.x + self.w, rect.x + rect.w)
        max_y = max(self.y + self.h, rect.y + rect.h)

        if win is not None:
            Draw.draw_rect(
                win,
                [min_x - 2, min_y - 2],
                [max_x - min_x + 4, max_y - min_y + 4],
                "Blue",
                2,
            )

        dist_w = distance([min_x, min_y], [max_x, min_y])
        dist_h = distance([min_x, min_y], [min_x, max_y])
        if dist_w < self.w + rect.w and dist_h < self.h + rect.h:
            return True
        return False

    @property
    def wh(self) -> Tuple[float, float]:
        return [self._w, self._h]

    @property
    def w(self) -> float:
        return self._w

    @w.setter
    def w(self, w: float):
        self._w = w

    @property
    def h(self) -> float:
        return self._h

    @h.setter
    def h(self, h: float):
        self._h = h

    @property
    def y_up(self) -> float:
        return self._y

    @y_up.setter
    def y_up(self, y: float):
        self._y = y

    @property
    def y_down(self) -> float:
        return self._y + self._h

    @y_down.setter
    def y_down(self, y: float):
        self._y = y - self._h

    @property
    def x_left(self) -> float:
        return self._x

    @x_left.setter
    def x_left(self, x: float):
        self._x = x

    @property
    def x_right(self) -> float:
        return self._x + self._w

    @x_right.setter
    def x_right(self, x: float):
        self._x = x - self._w
        
    @property
    def center(self):
        return [self._x+self._w/2, self._y+self._h/2]
    
    @center.setter
    def center(self, pos):
        self._x = pos[0]-self._w/2
        self._y = pos[1]-self._h/2

class Collider(Rect):
    def __init__(
        self,
        x: float,
        y: float,
        w: float,
        h: float,
        speed: Vector2 = Vector2(0, 0),
        gravity: Vector2 = Vector2(0, 0),
        trenie: Vector2 = Vector2(1, 1),
        air_resistance: Vector2 = Vector2(1, 1),
    ):
        super().__init__(x, y, w, h)
        self._speed = speed
        self._gravity = gravity
        self._trenie = trenie
        self._air_resistance = air_resistance
        self.colliding = True

        self.collides = {"left": False, "right": False, "up": False, "down": False}

    def __collide_list_form(self, rects):
        collide_list: Tuple[Rect, ...] = []
        for rect in rects:
            if self.collide_rect(rect) and rect.colliding:
                collide_list.append(rect)
        return collide_list

    def collide_rect_list(self, rect_tuple: Tuple[Rect, ...], moving: bool = False):
        self._speed += self._gravity
        self._speed.y *= self._air_resistance.y
        self._speed.x *= self._air_resistance.x
        self.collides = {"left": False, "right": False, "up": False, "down": False}

        self.y += self._speed.y

        
        collide_list = self.__collide_list_form(rect_tuple)

        for c_rect in collide_list:
            if self._speed.y > 0:
                self._speed.y *= 0
                self._speed.x *= self._trenie.x
                self.y_down = c_rect.y_up
                self.collides["down"] = True

            elif self._speed.y < 0:
                self._speed.y *= 0
                self._speed.x *= self._trenie.x
                self.y_up = c_rect.y_down
                self.collides["up"] = True

        self.x += self._speed.x
        
        collide_list = self.__collide_list_form(rect_tuple)

        for c_rect in collide_list:
            if self._speed.x > 0:
                self._speed.x *= -self._trenie.x
                if moving:
                    self._speed.x = 0
                # self.speed_.y *= self._trenie.y
                self.x_right = c_rect.x_left
                self.collides["right"] = True

            elif self._speed.x < 0:
                self._speed.x *= -self._trenie.x
                if moving:
                    self._speed.x = 0
                # self.speed_.y *= self._trenie.y
                self.x_left = c_rect.x_right
                self.collides["left"] = True
        # print(self.speed_)

    @property
    def collide_up(self) -> bool:
        return self.collides["up"]

    @property
    def collide_down(self) -> bool:
        return self.collides["down"]

    @property
    def collide_left(self) -> bool:
        return self.collides["left"]

    @property
    def collide_right(self) -> bool:
        return self.collides["right"]

    @property
    def sx(self):
        return self._speed.x

    @property
    def sy(self):
        return self._speed.y

    @sx.setter
    def sx(self, sx: float):
        self._speed.x = sx

    @sy.setter
    def sy(self, sy: float):
        self._speed.y = sy


class SpriteStack:
    def __init__(
        self, sprite_slices_file_name_: str, size_: Tuple[int, int], scale_: int = 1
    ) -> None:
        self.load_slices = pygame.image.load(sprite_slices_file_name_)
        self._size = size_
        self.object_pos = []
        self._pos = []
        self._scale = scale_

    def convert(self, angles_count=180, zapl=False):
        height = self.load_slices.get_height()
        self.converted_sprites = []
        self.angle_dur = 360 / angles_count

        for angle in range(angles_count):
            pre_surfs: list[pygame.Surface] = []
            for i in range(height // self._size[1]):
                sp = self.load_slices.subsurface(
                    [0, 0 + i * self._size[1]], [self._size[0], self._size[1]]
                )
                sp = pygame.transform.scale(
                    sp, [sp.get_width() * self._scale, sp.get_height() * self._scale]
                )
                sub_surf = pygame.transform.rotate(
                    sp,
                    angle * self.angle_dur,
                )
                pre_surfs.append(sub_surf)
            pre_surfs.reverse()
            surf_size = [
                pre_surfs[0].get_width(),
                pre_surfs[0].get_height() + i * self._scale,
            ]
            dummy_surf = pygame.Surface(surf_size).convert_alpha()
            dummy_surf.set_colorkey((0, 0, 0))
            for i, image in enumerate(pre_surfs):
                for k in range(int(self._scale)):
                    dummy_surf.blit(
                        image,
                        [
                            0,
                            dummy_surf.get_height()
                            - image.get_height()
                            - i * self._scale
                            - k,
                        ],
                    )
            self.converted_sprites.append(dummy_surf)

    def set_pos(self, pos):
        self._pos = copy(pos)

        self._pos[1] -= self._size[2] * self._scale / 2

    def render(self, surf: pygame.Surface, angle):
        sprite = self.converted_sprites[int((angle % 360) // self.angle_dur)]

        surf.blit(
            sprite,
            [
                self._pos[0] - sprite.get_width() / 2,
                self._pos[1] - sprite.get_height() / 2,
            ],
        )

        Draw.draw_circle(surf, self._pos, 2, "blue")
