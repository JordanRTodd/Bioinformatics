# Dictionary of codons and their corresponding amino acids
amino_acids = {
    'aaa': 'F', 'aac': 'V', 'aag': 'L', 'aat': 'I', 'aca': 'C', 'acc': 'G', 'acg': 'R', 'act': 'S',
    'aga': 'S', 'agc': 'A', 'agg': 'P', 'agt': 'T', 'ata': 'Y', 'atc': 'D', 'atg': 'H', 'att': 'N',
    'caa': 'L', 'cac': 'V', 'cag': 'L', 'cat': 'M', 'cca': 'W', 'ccc': 'G', 'ccg': 'R', 'cct': 'R',
    'cga': 'S', 'cgc': 'A', 'cgg': 'P', 'cgt': 'T', 'cta': 'X', 'ctc': 'E', 'ctg': 'Q', 'ctt': 'K',
    'gaa': 'F', 'gac': 'V', 'gag': 'L', 'gat': 'I', 'gca': 'C', 'gcc': 'G', 'gcg': 'R', 'gct': 'S',
    'gga': 'S', 'ggc': 'A', 'ggg': 'P', 'ggt': 'T', 'gta': 'Y', 'gtc': 'D', 'gtg': 'H', 'gtt': 'N',
    'tac': 'V', 'tat': 'I', 'tca': 'X', 'tcc': 'G', 'tcg': 'R', 'tct': 'R', 'tgc': 'A', 'tgg': 'P',
    'tgt': 'T', 'tta': 'X', 'ttc': 'E', 'ttg': 'Q', 'ttt': 'K'
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
print(f"\nCorresponding 5'-3' antisense amino acid string:\n{combined}\n")