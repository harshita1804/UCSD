import os 
def split_by_n(fname,n=3):
    '''
    Split files into sub files of near same size
    fname : Input file name
    n is the number of segments
    '''
    
    assert isinstance(fname, str)
    assert isinstance(n, int)
    assert n>0
    
    file_size = os.stat(fname).st_size
  
    chunk_size = file_size/n
    list_of_sentences = []
    
    with open(fname, 'r') as input_file:
        while True:
            line = input_file.readline()
            if not line:
                break
            list_of_sentences.append(line)
            
    
    track_size = 0
    track_line = 0
    
    for i in range(n):
        file_name = fname+'_'+str(i).zfill(3)+'.txt'
        with open(file_name, 'wt') as write_file:
            #line = list_of_sentences[track_line]
            while(track_size + len(list_of_sentences[track_line])<=chunk_size*(i+1)):
                write_file.write(list_of_sentences[track_line])
                track_size+=len(list_of_sentences[track_line])
                track_line+=1
                if(track_line>=len(list_of_sentences)):
                    break
