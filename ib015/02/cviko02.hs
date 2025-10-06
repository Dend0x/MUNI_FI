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

mod3 :: Integral a => a -> a
mod3 0 = 0
mod3 1 = 1
mod3 2 = 2
mod3 x = mod3 (x - 3)

div3 :: Integral a => a -> a
div3 0 = 0
div3 1 = 0
div3 2 = 0
div3 x = 1 + div3 (x - 3)

fact :: Integral a => a -> a
fact 0 = 1
fact x = x * fact (x - 1)

power :: (Num a, Integral b) => a -> b -> a
power x 1 = x
power x n = x * power x (n - 1)

isPower2 :: (Fractional a, Ord a) => a -> Bool
isPower2 0 = False
isPower2 1 = True
isPower2 x = if x < 1 then False else isPower2 (x / 2)

digitSum :: Integral a => a -> a
digitSum 0 = 0
digitSum x = (mod x 10) + digitSum (div x 10)

mygcd :: (Integral a, Ord a) => a -> a -> a
mygcd a 0 = a
mygcd 0 b = b
mygcd a b = if a > b then mygcd (a - b) b else mygcd a (b - a)

addHead :: a -> [a] -> [a]
addHead x y = x:y

getLast :: [a] -> a
getLast (x:[]) = x
getLast (x:y) = getLast y

stripLast :: [a] -> [a]
stripLast (x:[]) = []
stripLast (x:y) = x : stripLast y

len :: [a] -> Integer
len [] = 0
len (_:y) = 1 + len y

nth :: Int -> [a] -> a
nth 0 x = head x
nth n (x:y) = nth (n - 1) y

contains :: Eq a => [a] -> a -> Bool
contains [] n = False
contains (x:y) n = x == n || contains y n

containsNtimes :: Eq a => Integer -> a -> [a] -> Bool
containsNtimes _ _ [] = False
containsNtimes 0 _ _ = True
containsNtimes n x (h:y) = if h == x then containsNtimes (n - 1) x y else containsNtimes n x y

getPoints :: String -> [(String, Integer)] -> Integer
getPoints _ [] = 0
getPoints a ((x,y):z) = if x == a then y else getPoints a z

append :: [a] -> [a] -> [a]
append [] y = y
append x y = append (tail x) ((last x) : y)

pairs :: [a] -> [(a, a)]
pairs [] = []
pairs [x] = []
pairs (x:y:z) = [(x,y)] ++ pairs z

listSum :: Num n => [n] -> n
listSum [] = 0
listSum (x:y) = x + listSum y

oddLengthRec :: Bool -> [a] -> Bool
oddLengthRec False [] = False
oddLengthRec True [] = True
oddLengthRec b (x:y) = oddLengthRec (not b) y

oddLength :: [a] -> Bool
oddLength x = oddLengthRec False x

add1 :: Num n => [n] -> [n]
add1 [] = []
add1 (x:y) = [x + 1] ++ add1 y

multiplyN :: Num n => n -> [n] -> [n]
multiplyN _ [] = []
multiplyN n (x:y) = [x * n] ++ multiplyN n y