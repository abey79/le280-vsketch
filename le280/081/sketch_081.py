import numpy as np
import vsketch


class Sketch081(vsketch.SketchClass):
    export_page_size = vsketch.Param("a5", choices=vp.PAGE_SIZES.keys())
    export_margin = vsketch.Param(1.5, unit="cm", step=0.5)

    def draw(self, vsk: vsketch.Vsketch) -> None:
        vsk.size("500x500", landscape=False, center=False)

        vsk.translate(250, 250)
        for t in np.arange(0, 2 * np.pi, 2 * np.pi * 0.0025):
            line = np.empty(370, dtype=complex)
            a = t
            v = 0
            for i in range(len(line)):
                a += v
                v += vsk.random(-0.0001, 0.00011)
                v *= 1.0005
                line[i] = complex(np.cos(a) * i, np.sin(a) * i)
            vsk.polygon(line)

        vsk.vpype("crop 0 0 500 500")

    def finalize(self, vsk: vsketch.Vsketch) -> None:
        vsk.vpype(
            f"rect 0 0 500 500 text -p 500 513 -s 11 -a right 014 "
            f"layout -m {self.export_margin} -v top {self.export_page_size} "
            "linesimplify linesort"
        )


if __name__ == "__main__":
    Sketch081.display()
