import math

import vpype as vp
import vsketch


class Sketch126(vsketch.SketchClass):
    pen_width = vsketch.Param(0.3, unit="mm", step=0.1)
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        vsk.strokeWeight(2)
        vsk.penWidth(self.pen_width)

        for i in range(2500):
            x = i % 50
            y = i // 50
            with vsk.pushMatrix():
                vsk.translate(5 + x * 10, 5 + y * 10)
                vsk.rotate(math.tau * vsk.noise(x * 0.03, y * 0.03))
                vsk.line(-5, 0, 5, 0)

        vsk.vpype("color black crop 0 0 500 500")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 126 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linemerge linesimplify reloop linesort"
        )


if __name__ == "__main__":
    Sketch126.display()
