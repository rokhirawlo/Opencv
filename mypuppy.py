import cv2

img = cv2.imread('dog.jpg')



while true:
    
    cv2.imshow('Puppy', img)
    
    #if we waited at least 1 ms AND we have pressed the esc
    if cv2.waitKey(1)  & 0xFF == 27:
        break
        
        
cv2.destroyAllWindows()        