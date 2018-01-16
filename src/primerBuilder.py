def antiSensStrand(sequenceADN):
	seqAntiSensStrand = []
	for i in sequenceADN:
		if i == "A":
			seqAntiSensStrand.append("T")
		if i == "T":
			seqAntiSensStrand.append("A")
		if i == "C":
			seqAntiSensStrand.append("G")
		if i == "G":
			seqAntiSensStrand.append("C")
	seqAntiSensStrand = ''.join(seqAntiSensStrand)
	seqAntiSensStrand = seqAntiSensStrand[::-1]
	return seqAntiSensStrand


def antiSensStrandPrimer(seqSensStrand):
	antiSensStrandPrimer = {}
	delList = []
	for i in range(18,26):
		antiSensStrandPrimer[i]=seqSensStrand[:i]
	for i in antiSensStrandPrimer:
		if antiSensStrandPrimer[i][-1] == "A" or antiSensStrandPrimer[i][-1] == "T":
			delList.append(i)
		else:
			pass
	for i in delList:
		del antiSensStrandPrimer[i]
	
	return antiSensStrandPrimer


def SensStrandPrimer(seqAntiSensStrand):
	SensStrandPrimer = antiSensStrandPrimer(seqAntiSensStrand)
	return SensStrandPrimer


def primerHybridationTemp(primerSequence):
	allTemperature = {}

	for primer in primerSequence:
		hybridTemp = 0
		for nucleotid in primerSequence[primer]:
			if nucleotid == "A" or nucleotid == "T":
				hybridTemp +=2
			elif nucleotid == "C" or nucleotid == "G":
				hybridTemp +=4
		allTemperature[hybridTemp] = primerSequence[primer]

	return allTemperature

def sameHybridationTempPrimer(temperatureDict1, temperatureDict2):
	succes = False
	for key, value in temperatureDict1.items():
		for key2, value2 in temperatureDict2.items():
			if key - key2 == 0:
				samePrimerTemp = [value, value2, key]
				succes = True
				return samePrimerTemp
			else:
				pass

	if succes == False:
		print("Could not find primer with the same hybridiation temperature.")

def primerBuild(dnaContent):
	firstPrimer = antiSensStrandPrimer(dnaContent)
	secondPrimer = SensStrandPrimer(antiSensStrand(dnaContent))
	firstPrimerTemp =primerHybridationTemp(firstPrimer)
	secondPrimerTemp =primerHybridationTemp(secondPrimer)
	result = sameHybridationTempPrimer(firstPrimerTemp, secondPrimerTemp)
	return result

#seq = "actagcatgcatgctgacgttggtctagctgatgcatgcatgctgtgctgactga"
#a =primerBuild(seq)
#print(a)