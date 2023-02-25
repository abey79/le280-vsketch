# le280-vsketch

## What's this?

This sketch collection is adapted from [`<=280`](http://rrose-editions.com/portfolio/jean-noel-lafargue-280/) by [Jean-Noël Lafargue](https://twitter.com/Jean_no).

The goal is to port as many sketches as possible to [vsketch](https://github.com/abey79/vsketch), so that they may be plotted. Several of the `<=280` sketch are readily adaptable thanks to the similarities between vsketch and Processing, some might be trickier to convert, while others outright impossible due to their raster nature. Regardless, let's port as many as possible, even if some degree of interpretation is occasionally needed.

Though the collection is primarily an homage to this great book, it also aims to serve as vsketch examples. As a result, keeping sketches under the 280-character limit is a non-goal. Rather, the port should favour idiomatic approaches such as using Numpy.

## To contribute

Create sketch using the template I created for this project:

```
vsk init --template https://github.com/abey79/cookiecutter-le280-vsketch le280/XXX
```

Ignore page size and landscape prompts.

To keep with the book spirit, all the sketch are set up with a 500x500px size, and pixels are kept as unit in the code (i.e. no `vsk.scale("cm")` or similar). In addition to optimisation, the sketches' `finalize()` functions also draw a frame around the sketch, and lay it out on a page with configurable page format and margins. This way, the SVG output can readily be plotted while the interactive experience mimics the book's layout.


## License

The `<=280` book states that "[its content] can be adapted, remixed, borrowed or stolen". The same goes for this repository.