import os
import codecs
import markdown
import sys

reload(sys)
sys.setdefaultencoding('UTF8')

with open('scripts', 'r') as s:
    eval(compile(s.read(), '<stdin>', 'exec'))

def md_to_html(text):
    text = fancy_quotes(text)
    #text = prep_apostrophes(text)
    # Markdown extensions 'codehilite' and 'meta' also available.
    text = markdown.markdown(text, ['tables', 'footnotes', 'toc'])
    text = prep_latex(text)
    return text

def fancy_quotes(text):
    text = text.split("\n")
    for line in text:
        if not '    ' in line and not '`' in line:
            while "\"" in line:
                line = line.replace("\"", '&ldquo;', 1)
                line = line.replace("\"", '&rdquo;', 1)
            # fix quotes inside <div> tags
            while '=&ldquo;' in line:
                line = line.replace('=&ldquo;', "=\"", 1)
                line = line.replace('&rdquo;>', "\">", 1)
    text_out = ''
    for line in text:
        text_out += line.encode('utf-8') + "\n"
    return text_out

def prep_apostrophes(text):
    text = text.replace("'", '&rsquo;')
    return text

def prep_latex(text):
    text = text.replace('<p>$$', '<center class="donthyphenate">$$')
    text = text.replace('$$</p>', '$$</center>')
    return text

def is_comment(line):
    if '<!--' and '-->' in line:
        return 1
    return 0

def add_scripts(body, source):
    script_mark = '\n{{scripts}}'
    if '$$' in body or '\\(' in body or '\begin{align}' in body:
        source = source.replace(script_mark, mathJax + script_mark)
    if '<code>' in body:
        source = source.replace(script_mark, highlightjs + script_mark)
    source = source.replace(script_mark, '')
    return source

def add_content(body, template):
    return template.replace('{{content}}', body)

def diver(depth):
    up = ''
    for i in range(0, depth):
        up += '../'
    if depth == 0:
        up = './'
    return up

def add_side(source, categories, articles, category, depth):
    folder_mark = '{{folders}}'
    up = diver(depth)
    for cat in categories:
        if cat != category:
            source = source.replace(folder_mark, '<a href="' + up
                                    + cat + '"><div id="sub">' + cat + '</div></a>' + "\n"
                                    + folder_mark)
        else:
            source = source.replace(folder_mark,
                                    '<a href="' + up
                                    + cat + '"><div id="sub" class="sel">' + cat + '</div></a>' + "\n"
                                    + folder_mark)
            for title, parent in articles.iteritems():
                if parent == cat:
                    up = diver(depth-1)
                    source = source.replace(folder_mark, '<a href="' + up + title + '">'
                                            + '<div id="sub" class="indent">'
                                            + '&#x21B3; ' + title + '</div></a>' + "\n" + folder_mark)
                    up = diver(depth)
    source = source.replace(folder_mark, '')
    source = source.replace('</div></a>\n\n', '</div></a>\n', 1)
    return source

def make_source(template, title, body, depth, categories, articles, category):
    body = md_to_html(body)
    source = add_content(body, template)
    source = add_scripts(body, source)
    source = add_side(source, categories, articles, category, depth)
    source = source.replace('{{top-path}}', diver(depth))
    source = source.replace('{{folder}}', category)
    source = source.replace('{{title}}', title)
    return source

def get_body(filename):
    with codecs.open(filename, 'r', encoding='utf-8') as f:
        return f.read()

def write_source(path, source):
    with codecs.open(path, 'w', encoding='utf-8') as out:
        out.write(source)

"""http://stackoverflow.com/questions/1392413/
   calculating-a-directory-size-using-python"""
def get_folder_size(p):
   from functools import partial
   prepend = partial(os.path.join, p)
   return sum([(os.path.getsize(f) if os.path.isfile(f) else get_folder_size(f))
               for f in map(prepend, os.listdir(p))])

def print_tree(root, categories, tree_content):
    print root
    for cat in categories:
        print '   %s' % cat
        for key, value in tree_content.iteritems():
            if value == cat:
                print '      %s' % key
