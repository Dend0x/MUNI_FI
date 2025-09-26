isEmpty :: [a] -> Bool
isEmpty (_:_) = False
isEmpty _ = True

myHead :: [a] -> a
myHead (x:_) = x

myTail :: [a] -> [a]
myTail (_:x) = x

neck :: a -> [a] -> a
neck _ (_:x:_) = x
neck x _= x

isEven :: Integer -> Bool
isEven 0 = True
isEven 1 = False
isEven x = isEven (x - 2)