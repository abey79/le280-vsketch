import math

import numpy as np
import vpype as vp
import vsketch


class Sketch181(vsketch.SketchClass):
    line_count = vsketch.Param(8)
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        vsk.translate(250, 250)
        t = 2000
        an = math.tau / t

        for _ in range(self.line_count):
            vsk.rotate(math.pi / 90)
            i = np.arange(t + 1)
            n = an * i
            j = vsk.map(i % 200, 0, 200, 0, math.tau)
            line = np.cos(n) * 180 + np.cos(j) * 50 + 1j * (np.sin(n) * 180 + np.sin(j) * 50)
            vsk.polygon(line)

        vsk.vpype("color black")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 181 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linesimplify reloop linesort"
        )


if __name__ == "__main__":
    Sketch181.display()
