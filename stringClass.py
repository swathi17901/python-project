#sample string
sample_string="good thinks"
#capitalize()
capitalized_string=sample_string.capitalize()
print("capitalize:",capitalized_string)
#casefold
casefolded_string=sample_string.casefold()
print("casefold:",casefolded_string)
#center
centered_string=sample_string.center(20,'.')
print("center:",centered_string)
#count
counted=sample_string.count('o')
print("count:",counted)
#encode
encoded_string=sample_string.encode(encoding='utf-8')
print("encoded_string:",encoded_string)
#endswith
ends_with=sample_string.endswith('r')
print("endswith:",ends_with)
#expandtabs
expand_string="good\tthinks".expandtabs(4)
print("expandtabs:",expand_string)
#find
position=sample_string.find('i')
print("find:",position)
#index
index_position=sample_string.index('good')
print("index:",index_position)
#formatmap
values={'quantity':10,'price':200}
formated_map="I bought a {quantity} chocolates,its cost {price}".format_map(values)
print("formatmap:",formated_map)

