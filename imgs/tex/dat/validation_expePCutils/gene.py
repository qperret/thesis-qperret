#!/usr/bin/python
import glob

def rename(f):
    l = f.replace('.dat','').replace('_','')
    l = l.replace('0','Zero')
    l = l.replace('1','One')
    l = l.replace('2','Two')
    l = l.replace('3','Three')
    l = l.replace('4','Four')
    l = l.replace('5','Five')
    l = l.replace('6','Six')
    l = l.replace('7','Seven')
    l = l.replace('8','Eight')
    l = l.replace('9','Nine')
    return l

def caption(f):
    l = f.replace('.dat','').replace('PC_','').replace('_size','').replace('_nbbufs','')
    l = l.split('_')
    l = '$' + l[0] + '$ to $' + l[1] + '$'
    return l

fs = glob.glob('*.dat')
for f in sorted(fs):
     print '\pgfplotstableread{imgs/tex/dat/validation_expePCutils/' + f + '}\\' + rename(f)

for f in [l for l in sorted(fs) if l.find('size')!=-1]:
    print '\\begin{subfigure}[b]{0.3\\textwidth} \\begin{tikzpicture} \\begin{axis}[xmin=0,xmax=140, xscale=0.6,yscale=0.3,ticks=none]'
    print '    \\addplot[mark=none, color=black] table[x index=0, y index=1] {\\' + rename(f) +'};'
    print '\\end{axis} \\end{tikzpicture} \\caption{' + caption(f) + '} \\end{subfigure} '

print '\n\n\n\n\n'


for f in [l for l in sorted(fs) if l.find('nbbuf')!=-1]:
    print '\\begin{subfigure}[b]{0.3\\textwidth} \\begin{tikzpicture} \\begin{axis}[xmin=0,xmax=140, xscale=0.6,yscale=0.3,ticks=none]'
    print '    \\addplot[mark=none, color=black] table[x index=0, y index=1] {\\' + rename(f) +'};'
    print '\\end{axis} \\end{tikzpicture} \\caption{' + caption(f) + '} \\end{subfigure} '
