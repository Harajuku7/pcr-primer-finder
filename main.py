import optparse
from src.fastaReader import *
from src.primerBuilder import *

def main():
	p = optparse.OptionParser(description='PCR-Primer finder')
	p.add_option('-f', '--fasta', dest="filename", metavar="FILE", help='Fasta file name')
	p.add_option('-b', '--begin', dest="beginRegion", help='Begining of Region to amplify by PCR', type=int)
	p.add_option('-e', '--end', dest="endRegion", help='End of Region to amplify by PCR', type=int)

	options, arguments = p.parse_args()

	if options.filename and options.beginRegion and options.endRegion:
		content = fastaOpen(options.filename)
		cleanContent = fastaConvert(content)
		result = primerBuild(cleanContent[1][options.beginRegion-1:options.endRegion-1])
		if result[0]:
			print("Primer 1: " , result[1][0])
			print("Primer 2: " , result[1][1])
			print("Primer Hybridation temp: " , result[1][2], "°C")
		else:
			print(result[1])
	else:
		p.print_help()

def fastaOpen(filename):
	file_object  = open(filename, "r")
	content = file_object.read()
	return content

if __name__ == "__main__":
	main()