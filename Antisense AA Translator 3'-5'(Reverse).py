# Dictionary of codons and their corresponding amino acids
amino_acids = {
    'aaa': 'F', 'aac': 'L', 'aag': 'F', 'aat': 'L', 'aca': 'C', 'acc': 'W', 'acg': 'C', 'act': 'X',
    'aga': 'S', 'agc': 'S', 'agg': 'S', 'agt': 'S', 'ata': 'Y', 'atc': 'X', 'atg': 'Y', 'att': 'X',
    'caa': 'V', 'cac': 'V', 'cag': 'V', 'cat': 'V', 'cca': 'G', 'ccc': 'G', 'ccg': 'G', 'cct': 'G',
    'cga': 'A', 'cgc': 'A', 'cgg': 'A', 'cgt': 'A', 'cta': 'D', 'ctc': 'E', 'ctg': 'D', 'ctt': 'E',
    'gaa': 'L', 'gac': 'L', 'gag': 'L', 'gat': 'L', 'gca': 'R', 'gcc': 'R', 'gcg': 'R', 'gct': 'R',
    'gga': 'P', 'ggc': 'P', 'ggg': 'P', 'ggt': 'P', 'gta': 'H', 'gtc': 'Q', 'gtg': 'H', 'gtt': 'Q',
    'tac': 'M', 'tat': 'I', 'tca': 'S', 'tcc': 'R', 'tcg': 'S', 'tct': 'R', 'tgc': 'T', 'tgg': 'T',
    'tgt': 'T', 'tta': 'N', 'ttc': 'K', 'ttg': 'N', 'ttt': 'K'
}

def breakdown(data):
    array = []
    for i in range(0, len(data), 3):
        seq = data[i:i+3]
        if len(seq) == 3:
            array.append(amino_acids.get(seq, 'unknown'))
    return array

output = breakdown(input("\nEnter a sense strand mRNA string:\n"))
combined = ''.join(output)
print(f"\nCorresponding 3'-5' antisense amino acid string:\n{combined}\n")