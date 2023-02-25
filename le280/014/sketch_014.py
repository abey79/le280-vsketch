import itertools

import vpype as vp
import vsketch


class Sketch014(vsketch.SketchClass):
    node_count = vsketch.Param(2000, step=100)
    dist_threshold = vsketch.Param(30, step=5)
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        pts = [complex(vsk.random(0, 500), vsk.random(0, 500)) for _ in range(self.node_count)]

        for p1, p2 in itertools.product(pts, pts):
            if p1 != p2 and abs(p1 - p2) < self.dist_threshold:
                vsk.line(p1.real, p1.imag, p2.real, p2.imag)

        vsk.vpype("color black")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 014 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linemerge linesimplify linesort"
        )


if __name__ == "__main__":
    Sketch014.display()
