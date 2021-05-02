To install the packages, use anaconda. (mainly for the reason of dlib refusing to be compiled with or without cmake by using pip)

1 > create a new env  
2 > activate it  
3 > run `anaconda -c conda-forge install dlib`  
4 > install the other packages using pip either `cat requirements.txt | xargs -n 1 pip install`, or just `pip install -r requirements`    
