import math

import vpype as vp
import vsketch


class Sketch122(vsketch.SketchClass):
    pen_width = vsketch.Param(0.3, unit="mm", step=0.1)
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        vsk.fill(1)
        vsk.penWidth(self.pen_width)

        shp = vsk.createShape()
        shp.rect(0, 0, vsk.width, vsk.height)
        n = 0
        for r in range(500, 0, -10):
            n += 0.2
            for i in range(20):
                shp.circle(
                    vsk.width / 2 + math.cos(math.tau / 20 * i) * r,
                    vsk.height / 2 + math.sin(math.tau / 20 * i) * r,
                    abs((math.cos(n) * r if i % 2 == 0 else math.sin(n) * r) * 0.4),
                    op="difference",
                )

        vsk.shape(shp)

        vsk.vpype("color black")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 122 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linemerge linesimplify reloop linesort"
        )


if __name__ == "__main__":
    Sketch122.display()
