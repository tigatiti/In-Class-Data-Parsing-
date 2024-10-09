import argparse
import json
import csv
import xml.etree.ElementTree as ET

def convert_to_json(input_file, output_file):
  """Converts a text file to JSON."""
  data = []
  with open(input_file, 'r', encoding='ISO-8859-1') as f:
    for line in f:
      data.append(line.strip())
  with open(output_file, 'w', encoding='ISO-8859-1') as f:
    json.dump(data, f, indent=4)


def convert_to_csv(input_file, output_file):
  """Converts a text file to CSV."""
  with open(input_file, 'r', encoding='ISO-8859-1') as f_in, open(output_file, 'w', newline='', encoding='ISO-8859-1') as f_out:
    writer = csv.writer(f_out)
    for line in f_in:
      writer.writerow([line.strip()])


def convert_to_xml(input_file, output_file):
  """Converts a text file to XML."""
  root = ET.Element("data")
  with open(input_file, 'r', encoding='ISO-8859-1') as f:
    for line in f:
      element = ET.SubElement(root, "line")
      element.text = line.strip()
  tree = ET.ElementTree(root)
  tree.write(output_file, encoding="utf-8", xml_declaration=True)


def main():
  parser = argparse.ArgumentParser(description='Convert text file to JSON, CSV, or XML.')
  parser.add_argument('input_file', help='Path to the input text file')
  parser.add_argument('-j', '--json', action='store_true', help='Output JSON format')
  parser.add_argument('-c', '--csv', action='store_true', help='Output CSV format')
  parser.add_argument('-x', '--xml', action='store_true', help='Output XML format')
  args = parser.parse_args()

  output_file = args.input_file.rsplit('.', 1)[0]

  if args.json:
    convert_to_json(args.input_file, output_file + '.json')
  elif args.csv:
    convert_to_csv(args.input_file, output_file + '.csv')
  elif args.xml:
    convert_to_xml(args.input_file, output_file + '.xml')
  else:
    print("Please specify output format using -j, -c, or -x")


if __name__ == '__main__':
  main()


  