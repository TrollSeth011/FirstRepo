import pygal

piechart = pygal.Pie()
barchart = pygal.Bar()

file = open('pets.txt', 'r')

for line in file.read().splitlines():
    label, value = line.split(' ')
    piechart.add(label, int(value))
    barchart.add(label, int(value))
file.close()


piechart.title = 'Popular Pets'
piechart.render_in_browser()


barchart.title = 'Popular Pets'
barchart.render_in_browser()
