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

primeDivRec :: Integral a => a -> a -> a
primeDivRec 1 y = 0
primeDivRec x y = if (mod x y) == 0 then 1 + primeDivRec (div x y) y else 0 + primeDivRec x (y + 1 )

primeDivisors :: Integral a => a -> a
primeDivisors x = primeDivRec x 2

plus :: Integral a => a -> a -> a
plus x 0 = x
plus x y = plus (succ x) (pred y)

times :: Integral a => a -> a -> a
times _ 0 = 0
times 0 _ = 0
times x 1 = x
times x y = plus x (times x (y - 1))

plus' :: Integral a => a -> a -> a
plus' x 0 = x
plus' x y = if y > 0 then plus' (succ x) (pred y) else plus' (pred x) (succ y)

times' :: Integral a => a -> a -> a
times' _ 0 = 0
times' 0 _ = 0
times' x y = if y > 0 then plus' x (times' x (y - 1)) else negat (times' x (negat y))
    where negat x = -x

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

getBest :: [(String, Integer)] -> String
getBest [] = "No one"
getBest [(x,y)] = x
getBest ((x,y):(a,b):z) = if y > b then getBest ((x,y):z) else getBest ((a,b):z)

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

deleteEven :: Integral i => [i] -> [i]
deleteEven [] = []
deleteEven (x:y) = if even x then deleteEven y else x : (deleteEven y)

deleteElem :: Eq a => a -> [a] -> [a]
deleteElem _ [] = []
deleteElem a (x:y) = if x == a then deleteElem a y else x : (deleteElem a y)

largestNumber :: [Integer] -> Integer
largestNumber [x] = x
largestNumber (x:y:z) = if x > y then largestNumber (x:z) else largestNumber (y:z)

listsEqual :: Eq a => [a] -> [a] -> Bool
listsEqual [] [] = True
listsEqual _ [] = False
listsEqual [] _ = False
listsEqual (a:b) (x:y) = if a /= x then False else listsEqual b y

multiplyEven :: [Integer] -> [Integer]
multiplyEven [] = []
multiplyEven (x:y) = if even x then (2 * x) : multiplyEven y else multiplyEven y

sqroots :: [Double] -> [Double]
sqroots [] = []
sqroots (x:y) = if x > 0 then sqrt x : sqroots y else x : sqroots y

everyNth' :: Integer -> Integer -> [a] -> [a]
everyNth' _ _ [] = []
everyNth' 0 n (x:y) = x : everyNth' (n - 1) n y
everyNth' c n (_:y) = everyNth' (c - 1) n y

everyNth :: Integer -> [a] -> [a]
everyNth n x = everyNth' 0 n x

brackets' :: Integer -> String -> Integer
brackets' _ [] = 0
brackets' n (x:y) = if n < 0 then -1 else 
    if x == '(' then 1 + brackets' (n + 1) y else -1 + brackets' (n - 1) y

brackets :: String -> Bool
brackets a = 0 == brackets' 0 a

palindrome1 :: String -> String -> String
palindrome1 [] _ = []
palindrome1 (x:y) [] = []
palindrome1 (x:y) [a] = []
palindrome1 (x:y) (a:b:[]) = [x]
palindrome1 (x:y) (a:b:c) = palindrome1 y c ++ [x]

palindrome2 :: String -> String -> String
palindrome2 [] _ = []
palindrome2 (x:y) [] = y
palindrome2 (x:y) [a] = y
palindrome2 (x:y) (a:b:[]) = y
palindrome2 (x:y) (a:b:c) = palindrome2 y c

palindrome :: String -> Bool
palindrome x = palindrome1 x x == palindrome2 x x

prefixLen :: Int -> String -> String -> Int
prefixLen n [] [] = n
prefixLen n x y = if x == y then n else prefixLen (n + 1) (tail x) (init y)

palindromize :: String -> String
palindromize x = x ++ (reverse (take (prefixLen 0 x (reverse x)) x))

getMiddle' :: [a] -> [a] -> a
getMiddle' (x:y) [] = x
getMiddle' (x:y) [a] = x
getMiddle' (x:y) (a:b:[]) = x
getMiddle' (x:y) (a:b:c) = getMiddle' y c

getMiddle :: [a] -> a
getMiddle x = getMiddle' x x
