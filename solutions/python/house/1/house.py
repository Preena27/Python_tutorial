"""This programm recite the nursery rhyme 'This is the House that Jack Built'."""

PHRASES = [['the', 'house', 'that', 'Jack', 'built.'],
           ['lay'],
           ['ate', 'the', 'malt'],
           ['killed', 'the', 'rat'],
           ['worried', 'the', 'cat'],
           ['tossed', 'the', 'dog'],
           ['milked', 'the', 'cow', 'with', 'the', 'crumpled', 'horn'],
           ['kissed', 'the', 'maiden', 'all', 'forlorn'],
           ['married', 'the', 'man', 'all', 'tattered', 'and', 'torn'],
           ['woke', 'the', 'priest', 'all', 'shaven', 'and', 'shorn'],
           ['kept', 'the', 'rooster', 'that', 'crowed', 'in', 'the', 'morn'],
           ['belonged to', 'the', 'farmer', 'sowing', 'his', 'corn'],
           ['what?', 'the', 'horse', 'and', 'the', 'hound', 'and', 'the', 'horn']]


def recite(start_verse, end_verse):
    verse: list[str] = []
    check = start_verse == 1
    if check:
        verse.append('This is ' + ' '.join(PHRASES[start_verse-1]))
    for i in range(start_verse + check, end_verse+1):
        string = 'This is ' + ' '.join(PHRASES[i][1:])
        for j in range(i-1, 0, -1):
            string += ' that ' + ' '.join(PHRASES[j])
        string += ' in ' + ' '.join(PHRASES[0])
        verse.append(string)
    return verse