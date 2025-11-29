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
map' _ [] = []
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
maximumFold (x:xs) = foldl (max) x xs

subtractlist :: Num a => [a] -> a
subtractlist = foldl1 (-)

-- foldr :: (a -> b -> b) -> b -> [a] -> b
-- (.) :: (d -> c) -> (e -> d) -> (e -> c)
-- id :: f -> f

-- (d -> c) -> (e -> d) -> (e -> c) = (a -> b -> b)
-- f -> f = b

-- e = f = d = c
-- :: [f -> f] -> f -> f

append' :: [a] -> [a] -> [a]
append' = flip (foldr (\x y -> x : y))

reverse' :: [a] -> [a]
reverse' = foldl (\x y -> y : x) []

concatFold :: [[a]] -> [a]
concatFold = foldr (\x y -> x ++ y) []

listifyFold :: [a] -> [[a]]
listifyFold = foldr (\x y -> [x] : y) []

nullFold :: [a] -> Bool
nullFold = foldr (\x y -> y && False) True

composeFold :: [a -> a] -> a -> a
composeFold = flip (foldr (\x y -> x y))

idFold :: [a] -> [a]
idFold = foldr (:) []

mapFold :: (a -> b) -> [a] -> [b]
mapFold f = foldr (\x y -> f x : y) []

headFold :: [a] -> a
headFold = foldr1 const

lastFold :: [a] -> a
lastFold = foldl1 (\x y -> y)

maxminFold :: Ord a => [a] -> (a, a)
maxminFold (x:xs) = foldr (\x y -> (max x (fst y), min x (snd y))) (x, x) xs

suffixFold :: [a] -> [[a]]
suffixFold = foldr (\x y -> (x : head y) : y) [[]]

filterFold :: (a -> Bool) -> [a] -> [a]
filterFold f = foldr (\x y -> if f x then x : y else y) []

oddEvenFold :: [a] -> ([a], [a])
oddEvenFold = foldr (\ x y -> (x : snd y, fst y)) ([], [])

takeWhileFold :: (a -> Bool) -> [a] -> [a]
takeWhileFold f = foldr (\x y -> if f x then x : y else []) []

dropWhileFold :: (a -> Bool) -> [a] -> [a]
dropWhileFold f = foldl (\x y -> if f y && length x == 0 then [] else x ++ [y]) []

foldl' :: (a -> b -> a) -> a -> [b] -> a
foldl' f = foldr (\x y -> f y x)

insert :: Ord a => a -> [a] -> [a]
insert x [] = [x]
insert x (y:ys) = if x <= y then x : y : ys else y : insert x (ys)

insertSort :: Ord a => [a] -> [a]
insertSort = foldl (\x y -> insert y x) []

tree01 :: BinTree Int
tree01 = Node 2 (Node 3 (Node 5 Empty Empty) Empty)
                (Node 4 (Node 1 Empty Empty) (Node 1 Empty Empty))

tree02 :: BinTree String
tree02 = Node "C" (Node "A" Empty (Node "B" Empty Empty))
                  (Node "E" (Node "D" Empty Empty) Empty)

tree03 :: BinTree (Int,Int)
tree03 = Node (3,3) (Node (2,1) Empty Empty) (Node (1,1) Empty Empty)

tree04 :: BinTree a
tree04 = Empty

tree05 :: BinTree Bool
tree05 = Node False (Node False Empty (Node True Empty Empty))
                    (Node False Empty Empty)

tree06 :: BinTree (Int, Int -> Bool)
tree06 = Node (0,even)
              (Node (1,odd) (Node (2,(== 1)) Empty Empty) Empty)
              (Node (3,(< 5)) Empty
                              (Node (4,((== 0) . mod 12)) Empty Empty))

treeFold :: (a -> b -> b -> b) -> b -> BinTree a -> b
treeFold _ e Empty = e
treeFold f e (Node v l r) = f v (treeFold f e l) (treeFold f e r)

treeSize :: BinTree a -> Int
treeSize = treeFold (\x y z -> 1 + y + z) 0

treeHeight :: BinTree a -> Int
treeHeight = treeFold (\x y z -> 1 + max y z) 0

treeList :: BinTree a -> [a]
treeList = treeFold (\x y z -> y ++ [x] ++ z) []

treeConcat :: BinTree [a] -> [a]
treeConcat = treeFold (\x y z -> y ++ x ++ z) []

treeMax :: (Ord a, Bounded a) => BinTree a -> a
treeMax (Node v l r) = treeFold (\x y z -> if x > y && x > z then x else max y z) v (Node v l r)

treeFlip :: BinTree a -> BinTree a
treeFlip = treeFold (\x y z -> (Node x z y)) Empty

treeId :: BinTree a -> BinTree a
treeId = treeFold (\x y z -> (Node x y z)) Empty

rightMostBranch :: BinTree a -> [a]
rightMostBranch = treeFold (\x y z -> x : z) []

treeRoot :: BinTree a -> a
treeRoot = treeFold (\x y z -> x) undefined

treeNull :: BinTree a -> Bool
treeNull = treeFold (\x y z -> False) True

leavesCount :: BinTree a -> Int
leavesCount = treeFold (\x y z -> if y == 0 && z == 0 then 1 else y + z) 0

leavesList :: BinTree a -> [a]
leavesList = treeFold (\x y z -> if length y == 0 && length z == 0 then [x] else y ++ z) []

treeMap :: (a -> b) -> BinTree a -> BinTree b
treeMap f = treeFold (\x y z -> (Node (f x) y z)) Empty

treeAny :: (a -> Bool) -> BinTree a -> Bool
treeAny f = treeFold (\x y z -> if f x then True else y || z) False

treePair :: Eq a => BinTree (a,a) -> Bool
treePair = treeFold (\x y z -> if fst x /= snd x then False else y && z) True

subtreeSums :: Num a => BinTree a -> BinTree a
subtreeSums = treeFold (\x y z -> (Node (x + root y + root z) y z)) Empty
    where root (Node x _ _) = x
          root Empty = 0

data RoseTree a = RoseNode a [RoseTree a]
        deriving Show

roseTreeFold :: (a -> [b] -> b) -> RoseTree a -> b
roseTreeFold f (RoseNode x xs) = f x (map (roseTreeFold f) xs)