with open("names.txt",'r')as namef:
    with open("body.txt",'r')as bodyf:
        body=bodyf.read()
        for n in namef:
            bo=body+n
            with open(n.strip()+".txt",'w')as mailf:
                mailf.write(bo)
