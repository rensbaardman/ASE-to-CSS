import swatch as swatch_parser
import sys
import re

def parse_swatches(filepath):
	return swatch_parser.parse(filepath)

def swatches_to_css(swatches, style, filepath='', declarations_only=False):

	# this might not be Windows-compatible
	filename = filepath.split('/')[-1]
	css = ''

	# root variable for using css vars
	if(style == 'scss'):
		prefix = '/* converted from {0} */\n'.format(filename)
	else:
		prefix = '/* converted from {0} */\n:root {{\n'.format(filename)

	if(style == 'scss'):
		postfix = '\n'
	else:
		postfix = '}\n'

		#set prefix to -- for css and $ for sass
	if(style == 'scss'):
		varprefx = '$'
	else:
		varprefx = '--'

	# check for valid CSS identifiers (custom property names - a.k.a. variables - are identifiers)
	# In CSS, identifiers (including element names, classes, and IDs in selectors) can contain only the characters [a-zA-Z0-9] and ISO 10646 characters U+0080 and higher, plus the hyphen (-) and the underscore (_)
	pattern = re.compile(r"[^a-zA-Z0-9-_]")

	for swatch in swatches:

		# this means it is a (palette) group
		if 'swatches' in swatch:
			
			# only output extra newline if not the first entry
			if css == '':
				newline = ''
			else:
				newline = '\n'

			group_prefix = '{0}\t/* {1} */\n'.format(newline, swatch['name'])
			group_postfix = '\n'
			group_declarations = swatches_to_css(swatch['swatches'], style, declarations_only=True)
			css += group_prefix + group_declarations + group_postfix

		else:
			values = swatch['data']['values']
			color = [round(255 * value) for value in values]
			css_color = 'RGB({0}, {1}, {2})'.format(*color)

			# replace all invalid characters with '_'
			name = swatch['name']
			css_name = re.sub(pattern, '_', name)

			css += '\t{0}{1}: {2};\n'.format(varprefx, css_name, css_color)

	if declarations_only:
		return css
	else:
		# suppress extra newline after group if last entry
		if css[-2:] == '\n\n':
			css = css[:-1]
		return prefix + css + postfix

def save_css(swatch_filepath, style, css):
	#set file extention based on desired output
	if(style == 'scss'):
		ext = '.scss'
	else:
		ext = '.css'

	if swatch_filepath.split('.')[-1] == 'ase':
		css_filepath = '.'.join(swatch_filepath.split('.')[:-1]) + ext
	else:
		css_filepath = swatch_filepath + ext

	with open(css_filepath, 'w') as file:
		file.write(css)

def main():
	swatch_filepath = sys.argv[1]
	swatches = parse_swatches(swatch_filepath)
	style = sys.argv[2]

	css = swatches_to_css(swatches, style, filepath=swatch_filepath)
	
	save_css(swatch_filepath, style, css)

main()
