import string

def termNorm(srcPath, srcFile, tarFile):
    src_sent = ''
    tar_sent = ''
    src = open(srcFile, 'w')
    tar = open(tarFile, 'w')
    punc = string.punctuation
    for line in open(srcPath, 'r'):
        if len(line.strip()) > 1:
            str = line.strip().split('\t')
            if len(src_sent) == 0:
                src_sent = str[0]
                tar_sent = str[2]                
            else:
                if str[0] in punc:
                    src_sent = src_sent
                    tar_sent = tar_sent
                else:
                    src_sent = src_sent + " " + str[0]
                    tar_sent = tar_sent + " " + str[2]
        if len(line.strip()) == 0:
            print(src_sent)
            print(tar_sent)
            src.write(src_sent + ' \n')
            tar.write(tar_sent + ' \n')
            src_sent = ''
            tar_sent = ''
        
if __name__ == '__main__':
    org = '/Users/hjp/MacBook/data/nom/npos_ii.txt'
    src = '/Users/hjp/MacBook/data/tmp/npos_ii_inf.txt'
    tar = '/Users/hjp/MacBook/data/tmp/npos_ii_nom.txt'
    
    termNorm(org, src, tar)
   