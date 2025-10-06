doubleFirst :: [a] -> [a]
doubleFirst (x:s) = x:x:s

dupliAndLast :: [a] -> [a]
dupliAndLast x = x ++ x ++ [head x]

isPalindrome ::  Eq a => [a] -> Bool
isPalindrome x = x == reverse x

plusBiggerMultiply :: (Num a, Ord a) => [a] -> Bool
plusBiggerMultiply x = sum x > product x

isEvenArray :: Integral a => [a] -> Bool
isEvenArray x = length x == length (filter even x)

myLength :: Num a => [a] -> a
myLength x = sum (map f x)
    where f _ = 1

swapDouble :: [(a, b)] -> [(b, a)]
swapDouble x = map swap x
    where swap (a, b) = (b, a)

myLast :: [a] -> a
myLast (x:[]) = x
myLast (x:s) = myLast s

myBody :: [a] -> [a]
myBody (_:[]) = []
myBody (x:s) = x : myBody s