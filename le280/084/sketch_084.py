import math

import vpype as vp
import vsketch


class Sketch084(vsketch.SketchClass):
    line_count = vsketch.Param(1000, step=50)
    sub_line_count = vsketch.Param(100, step=10)
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        vsk.translate(250, 250)
        for a in range(self.line_count):
            a1 = vsk.map(a, 0, self.line_count, 0, math.tau)
            a2 = vsk.map(a % self.sub_line_count, 0, self.sub_line_count, 0, math.tau)
            vsk.line(
                math.cos(a1) * 250, math.sin(a1) * 250, math.cos(a2) * 100, math.sin(a2) * 100
            )

        vsk.vpype("color #0004")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 084 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linesort"
        )


if __name__ == "__main__":
    Sketch084.display()
