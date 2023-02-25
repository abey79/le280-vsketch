import itertools
import math

import vpype as vp
import vsketch


class Sketch079(vsketch.SketchClass):
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        r = 0
        f = 250
        pts = []
        while r < f:
            r += 35
            a = 0
            while a < math.tau:
                a += math.pi / r
                t = r + vsk.random(18)
                pts.append(complex(f + t * math.cos(a), f + t * math.sin(a)))

        for p1, p2 in itertools.product(pts, pts):
            if p1 != p2 and abs(p1 - p2) < 20:
                vsk.line(p1.real, p1.imag, p2.real, p2.imag)

        vsk.vpype("color black crop 0 0 500 500")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 014 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linemerge linesort"
        )


if __name__ == "__main__":
    Sketch079.display()
