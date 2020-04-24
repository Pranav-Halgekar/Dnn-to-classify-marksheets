import os
address=os.getcwd()
def main():
    
    
    for count,filename in enumerate(os.listdir(address)):
        if filename!="campus alpha file renaming code.py":
            src=filename
            dst="campus_alpha"+str(count)+".jpg"
            os.rename(src,dst)
        
        
        
if __name__=='__main__':
    main()