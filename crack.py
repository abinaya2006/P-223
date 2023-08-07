import zipfile
import time

folderPath = "./C_P.zip"
zipf = zipfile.ZipFile(folderPath)

if not zipf:
    print("Folder is not protected , you can open it.")
else:
    print("Folder is protected")
    startT = time.time()
    result = 0
    t = 0 
    characters=['0','1','2','3','4','5','6','7','8','9', 'a','b','c','d','e','f','g','h','i','j','l','k','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

    print("Brute force started")

    if( result ==0): #eg.0124
        for i in characters: #first char - 0
            for j in characters:#2nd ch - 1
                for k in characters:#3rd ch -2
                    for l in characters: #4th ch - 4
                        guess = str(i)+str(j)+str(k)+str(l)
                        password  = guess.encode("utf-8").strip()
                        t+=1
                        try:
                            with zipfile.ZipFile(folderPath,"r") as f:
                                f.extractall(pwd=password)
                                print("Got it! The password is "  + guess)
                                endT = time.time()
                                result =1
                                break
                        
                        except: pass

                    if result==1:
                        break
                
                if result==1:
                    break
            
            if result ==1:
                break
        
        if result==0:
            duration = endT-startT
            print("Sorry password not found" + str(t) + " possible combinations we tried " + str(duration) + "seconds")
        else:
            duration = endT-startT
            print("Congratulations , password found after" + str(t) +" tries , in  "+ str(duration) +"seconds")
                            


