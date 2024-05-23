
amino_acids = {'aaa':'F','aac':'L','aag':'F','aat':'L','aca':'C','acc':'W','acg':'C','act':'X','aga':'S','agc':'S','agg':'S','agt':'S','ata':'Y','atc':'X','atg':'Y','att':'X','caa':'V','cac':'V','cag':'V','cat':'V','cca':'G','ccc':'G','ccg':'G','cct':'G','cga':'A','cgc':'A','cgg':'A','cgt':'A','cta':'D','ctc':'E','ctg':'D','ctt':'E','gaa':'L','gac':'L','gag':'L','gat':'L','gca':'R','gcc':'R','gcg':'R','gct':'R','gga':'P','ggc':'P','ggg':'P','ggt':'P','gta':'H','gtc':'Q','gtg':'H','gtt':'Q','tac':'M','tat':'I','tca':'S','tcc':'R','tcg':'S','tct':'R','tgc':'T','tgg':'T','tgt':'T','tta':'N','ttc':'K','ttg':'N','ttt':'K'}



def breakdown(data):
    array=[]
    for i in range(0,len(data),3):
        if (i+3>len(data)):
            upper = len(data)
        else:
            upper =i+3
        seq=data[i:upper]
        try:
            array.append(amino_acids[seq])
        except KeyError :
            array.append('unknown')
    return array
        
output=breakdown('atg')
print (output)
combined=''
for acid in output:
    combined =combined+acid
    
print(combined)
    


  


