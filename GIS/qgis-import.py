import csv
with open("/home/alex/rw.csv","r") as file:
  r = csv.reader(file)
  csvr = list(r)
  layer = iface.activeLayer()
  layer.startEditing()
  for f in layer.getFeatures():
    for row in csvr:
      if row[0] == f[10]:
        f[20] = row[1]
        f[21] = row[2]
        layer.updateFeature(f)
