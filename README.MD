# ASE-to-CSS
Convert Adobe Swatch Exchange files to CSS or SCSS variables!

### Usage

CSS:
```
$ python ase-to-css.py swatches.ase css
```
generates `swatches.css` with all swatch colors defined as CSS variables on the `:root` variables.

SCSS/SASS:
```
$ python ase-to-css.py swatches.ase scss
```
generates `swatches.scss` with all swatch colors defined as SASS variables.


### Example

When converting the standard swatches in Illustrator using the CSS argument, this is the output:

```css
/* converted from swatches.ase */
:root {
	--White: RGB(255, 255, 255);
	--Black: RGB(0, 0, 0);
	--RGB_Red: RGB(255, 0, 0);
...
	--R_66_G_33_B_11: RGB(66, 33, 11);

	/* Grays */
	--R_0_G_0_B_0: RGB(0, 0, 0);
...
	--R_242_G_242_B_242: RGB(242, 242, 242);

	/* Web Color Group */
	--R_63_G_169_B_245: RGB(63, 169, 245);
...
	--R_189_G_204_B_212: RGB(189, 204, 212);
}

```


When converting the standard swatches in Illustrator using the SCSS argument, this is the output:

```scss
/* converted from swatches.ase */
	$White: RGB(255, 255, 255);
	$Black: RGB(0, 0, 0);
	$RGB_Red: RGB(255, 0, 0);
...
	$R_66_G_33_B_11: RGB(66, 33, 11);

	/* Grays */
	$R_0_G_0_B_0: RGB(0, 0, 0);
...
	$R_242_G_242_B_242: RGB(242, 242, 242);

	/* Web Color Group */
	$R_63_G_169_B_245: RGB(63, 169, 245);
...
	$R_189_G_204_B_212: RGB(189, 204, 212);

```



### todo

- also output LESS
- consider (giving an option) to prefix group names to variable names
- check for clashing variable names (note: variable names are case sensitive)
- add tests
- check for different swatch options (what if the colors haven't been specified as RGB, or as spot colors, etc.)
- option to change indentation (currently: 1 tab)
- bundle as module (+ seperate CLI?)
- add options export as RGBA (or as hexadecimal) instead of RGB
