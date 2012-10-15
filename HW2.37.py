#! /usr/bin/python

# Get sequence input from user
sequence = raw_input('Enter a DNA sequence: ')

# Get pattern input from user
pattern = raw_input('Enter the pattern: ')

# Reverse the pattern
reversedPattern = pattern[::-1]

# Find pattern and length of the sequence
patternIndex = sequence.find(pattern) + len(pattern)

# Find reversed pattern of the sequence starting after patternIndex in case the reverse pattern appears before the forward pattern
reversedPatternIndex = sequence.find(reversedPattern,patternIndex)

# Find beginning of the sequence
beginSequence = sequence[:patternIndex]

# Find end of the sequence
endSequence = sequence[reversedPatternIndex:]

# Find the middle of the squence
middleSequence = sequence[patternIndex:reversedPatternIndex]

# Reverse the middle sequence
mutatedDNA = middleSequence[::-1]

# Add beginning sequence, mutated DNA, and ending sequence
outputMutatedDNA = beginSequence + mutatedDNA + endSequence

# Print the outputMutatedDNA
print 'Mutated DNA sequence: ', outputMutatedDNA