# Controller API Documentation

User documentation for the controller HTTP, Javascript and Lua APIs.

## Build instructions

Assuming you have [Sphinx](http://www.sphinx-doc.org/en/stable/) installed, from the root directory of the project you can run:

    make html

This will create the html output for Pharos in the `build` directory (which will be created if building for the first time).

### Building a specific variant

To build a different variant, e.g. Mosaic, set `VARIANT` in your environment, e.g.

    VARIANT=mosaic make html

Currently supported variants are:

* `pharos` for Pharos (the default)
* `mosaic` for ETC Mosaic
