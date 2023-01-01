with open("app.js","r") as f:
     lines = f.readlines()
     for line in lines:
             if "base64" in line:
                     #strip after base64 string is found in the file
                     mid = line.split("base64,")[1]
                     #strip the last /n character from the above string to get base64 output only
                     base64out = (mid.split("//")[0])[:-2]
                     with open("base6.out","a") as r:
                          r.writelines(base64out)
                          r.write('\n')
