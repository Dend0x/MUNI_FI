divisors :: Integer -> [Integer]
divisors n = [ x | x <- [1..n], mod n x == 0 ]

negativeCredit :: [(String, Integer)] -> [String]
negativeCredit xs = [ fst x | x <- xs, ((<0) . snd) x]

allDivisibleSums :: [Integer] -> [Integer] -> Integer -> [(Integer, Integer, Integer)]
allDivisibleSums xs ys d = [ (x,y,x+y) | x <- xs, y <- ys, mod (x+y) d == 0 ]

type UCO = Int

students :: [(UCO, [String])]
students = [(415409, []), (448093, ["IB111", "IB015", "IB000"]),(405541, ["IB111", "IB000", "IB005", "MB151", "MB152"])]

countPassed :: [(UCO, [String])] -> [(UCO, Int)]
countPassed xs = [(fst x, (length . snd) x) | x <- xs]

atLeastTwo :: [(UCO, [String])] -> [UCO]
atLeastTwo xs = [(fst x)| x <- xs, ((>=2). length . snd) x]

passedIB015 :: [(UCO, [String])] -> [UCO]
passedIB015 xs = [(fst x)| x <- xs, elem "IB015" (snd x)]

passedBySomeone :: [(UCO, [String])] -> [String]
passedBySomeone xs = [ y | x <- xs, y <- (snd x)]

naturalsFrom :: Integer -> [Integer]
naturalsFrom n = [ x + n | x <- [0..]]

naturals :: [Integer]
naturals = naturalsFrom 0

maxminhelp :: Ord a => [a] -> a -> a -> (a, a)
maxminhelp [] maxi mini = (maxi, mini)
maxminhelp (x:xs) maxi mini = maxminhelp xs (max x maxi) (min x mini)

maxmin :: Ord a => [a] -> (a, a)
maxmin (x:xs) = maxminhelp xs x x

data Sex = Female | Male

allPairs :: [(String, Sex)] -> [(String, String)]
allPairs xs = [(m, f) | (m, Male) <- xs, (f, Female) <- xs]

squared :: Integer -> [Integer]
squared k = [ n^2 | n <- [1..k]]

f :: [[a]] -> [[a]]
f xs = [ x | x <- xs, ((>3) . length) x]

stars :: [Char]
stars = ['*' | x <- [1..5]]

starsBetter :: [[Char]]
starsBetter = [['*' | y <- [0..x-1]] | x <- [0..]]

listlist :: [[Integer]]
listlist = [[y | y <- [1..x]] | x <- [1..]]

-- map f s
-- [ f x | x <- s]
-- filter p s
-- [ x | x <- s, p x]
-- map f (filter p s)
-- [ f x | x <- s, p x]
-- repeat x
-- [ x | s <- [0..]]
-- replicate n x
-- [ x | s <- [1..n]]
-- filter p (map f s)
-- [ y | y <- [ f x | x <- s], p y]

--potom
permutations :: (Eq a) => [a] -> [[a]]
permutations [] = [[]]
permutations xs = [x : y | x <- xs, y <- permutations (filter (/=x) xs)]

variations :: Int -> [a] -> [[a]]
variations 0 _ = [[]]
variations _ [] = [[]]
variations n xs = [x : y | x <- xs, y <- variations (n - 1) xs]

filter' :: (a -> Bool) -> [a] -> [a]
filter' _ [] = []
filter' p (x : xs) = if p x then x : filter' p xs else filter' p xs

takeWhile' :: (a -> Bool) -> [a] -> [a]
takeWhile' _ [] = []
takeWhile' p (x : xs) = if p x then x : takeWhile' p xs else []

addNumbers :: [String] -> [String]
addNumbers xs = zipWith (number) [1..] xs
    where number x y = show x ++ ". " ++ y

integers :: [Integer]
integers = 0 : [ x * y | x <- [1..], y <- [1, -1]]

threeSum :: [(Integer, Integer, Integer)]
threeSum = [(x,y,x+y) | x <- [0..], y <- [0..x]]

-- repeat True
-- itearate (*2) 1
-- iterate (*9) 1
-- iterate (*9) 3
-- cycle [1, -1]
-- iterate ('*' :) ""
-- cycle [0,1,2,3]

dihfferences :: [Integer] -> [Integer]
dihfferences xs = zipWith (-) xs (tail xs)

values :: (Integer -> Integer) -> [Integer]
values f = map f [0..]

localMinimaRec :: [Integer] -> [Integer]
localMinimaRec (x:y:z:xs) = if x > y && y < z then y : localMinimaRec (y:z:xs) else localMinimaRec (y:z:xs)

localMinima :: (Integer -> Integer) -> [Integer]
localMinima f = head (dihfferences (values f)) : (localMinimaRec (dihfferences (values f)))

fib :: [Integer]
fib = 0 : 1 : zipWith (+) fib (tail fib)

data BinTree a = Node a (BinTree a) (BinTree a) | Empty
    deriving (Show, Eq)

treeTrim :: BinTree a -> Integer -> BinTree a
treeTrim Empty _ = Empty
treeTrim (Node v l r) 0 = (Node v Empty Empty)
treeTrim (Node v l r) h = (Node v (treeTrim l (h - 1)) (treeTrim r (h - 1)))


treeRepeat :: a -> BinTree a
treeRepeat x = (Node x (treeRepeat x) (treeRepeat x))

treeIterate :: (a -> a) -> (a -> a) -> a -> BinTree a
treeIterate lf rf x = (Node x (treeIterate lf rf (lf x)) (treeIterate lf rf (rf x)))

depthTree :: BinTree Integer
depthTree = treeIterate (+1) (+1) 0

nonNegativePairs :: [(Integer, Integer)]
nonNegativePairs = [ (y, x - y) | x <- [0..], y <- [0..x]]

positiveLists = [ l | s <- [0 ..], l <- listsOfSum s ]
    where
        listsOfSum :: Integer -> [[Integer]]
        listsOfSum 0 = [[]]
        listsOfSum n = [x : l | x <- [1 .. n], l <- listsOfSum (n - x)]

product' :: Num a => [a] -> a
product' [x] = x
product' (x:xs) = x * product' xs

length' :: [a] -> Integer
length' [] = 0
length' (x:xs) = 1 + length' xs

map' :: (a -> b) -> [a] -> [b]
map' f [] = []
map' f (x:xs) = f x : map' f xs

sumFold :: Num a => [a] -> a
sumFold = foldr (+) 0

productFold :: Num a => [a] -> a
productFold = foldr1 (*)

orFold :: [Bool] -> Bool
orFold = foldr (||) False

lengthFold :: [a] -> Int
lengthFold = foldr (\x y -> y + 1) 0

maximumFold :: Ord a => [a] -> a
maximumFold = foldr1 (\x y -> max x y)

subtractlist :: Num a => [a] -> a
subtractlist = foldl1 (-)

-- b foldr - (a -> b -> b) -> b -> [a] -> b
-- (.) - (b -> c) -> (a -> b) -> (a -> c)
-- id - a -> a