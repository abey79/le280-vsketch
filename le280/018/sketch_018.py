import math

import vsketch


class Sketch018(vsketch.SketchClass):
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        vsk.translate(250, 250)

        for t in range(1, 380, 2):
            vsk.rotate(vsk.random(0, math.tau))
            vsk.arc(
                0, 0, t, t, vsk.random(0, math.tau), vsk.random(0, math.tau), mode="radius"
            )
        vsk.vpype("crop 0 0 500 500")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 014 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linesimplify linesort"
        )


if __name__ == "__main__":
    Sketch018.display()
