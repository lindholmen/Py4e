import pyfiglet
import termcolor
#help(pyfiglet)

#print_figlet(text, font='standard', colors=':', **kwargs)

mytext = pyfiglet.figlet_format("gongzhanghuanniubi")
asciitext = termcolor.colored(mytext, color = "magenta", attrs=["bold"])
print(asciitext)

pyfiglet.print_figlet("GZH")

f = pyfiglet.Figlet(font='doh')
#f = pyfiglet.Figlet(font='isometric3')
#http://www.figlet.org/examples.html
#f = pyfiglet.Figlet(font='nipples')



print(f.renderText('GZH'))