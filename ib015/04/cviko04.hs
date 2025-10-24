import Data.Char

oddify :: Integral a => [a] -> [a]
oddify xs = map (\x -> if even x then x + 1 else x) xs

inputWithOddified :: Integral a => [a] -> [(a, a)]
inputWithOddified xs = zip xs (oddify xs)

filterOutShorter :: [String] -> Int -> [String]
filterOutShorter xs n = filter (\x -> length x >= n) xs

getNames :: [(String, Integer)] -> [String]
getNames xs = map fst xs

successfulRecords :: [(String, Integer)] -> [(String, Integer)]
successfulRecords xs = filter (\(_,n) -> n >= 8) xs

successfulNames :: [(String, Integer)] -> [String]
successfulNames = getNames . successfulRecords

successfulStrings :: [(String, Integer)] -> [String]
successfulStrings xs = map display (successfulRecords xs)
    where display (x,y) = "jmeno: " ++ x ++ " " ++ show y ++ " b"

add1 :: Num n => [n] -> [n]
add1 = map (+1)

multiplyN :: Num n => n -> [n] -> [n]
multiplyN n = map (*n)

deleteEven :: Integral i => [i] -> [i]
deleteEven = filter odd

deleteElem :: Eq a => a -> [a] -> [a]
deleteElem e = filter (/=e)

multiplyEven :: [Integer] -> [Integer]
multiplyEven = map (*2)  . filter even

sqroots :: [Double] -> [Double]
sqroots = map sqrt . filter (>0)

toUpperStr :: String -> String
toUpperStr = map toUpper

vowels :: [String] -> [String]
vowels xs = map (filter isVowel) xs
    where isVowel :: Char -> Bool
          isVowel c = elem (toUpper c) "AEIOUY"

assignPrizes :: [String] -> [Integer] -> [(String, Integer)]
assignPrizes = zip

prizeTexts :: [String] -> [Integer] -> [String]
prizeTexts = zipWith display
    where display :: String -> Integer -> String
          display x y = "jmeno: " ++ x ++ " " ++ show y ++ " Kc"

-- map (\(x,y,z) -> if x then y else z) (zip3 [True, False, False, True, False] [1, 2, 3, 4] [16, 42, 7, 1, 666])
-- zipWith3 (\x y z -> max (max x y) z) [7, 4, 11, 2] [5, 7, 1] [16, 5, 0, 1]

neighbors :: [a] -> [(a, a)]
neighbors xs = zip xs (tail xs)

neighborsNumbers :: (Eq a, Num a) => [a] -> Bool
neighborsNumbers xs = or (zipWith (==) xs (tail xs))

myMap :: (a -> b) -> [a] -> [b]
myMap _ [] = []
myMap f (x:xs) = f x : myMap f xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter _ [] = []
myFilter f (x:xs) = if f x then x : myFilter f xs else myFilter f xs

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith _ [] _ = []
myZipWith _ _ [] = []
myZipWith f (x:xs) (y:ys) = f x y : myZipWith f xs ys

anyEven :: [Integer] -> Bool
anyEven = or . map even

allEven :: [Integer] -> Bool
allEven = and . map even

blueless :: [(Int, Int, Int)] -> [(Int, Int, Int)]
blueless = filter (\(x,y,z) -> z == 0)

greyscale :: [(Int, Int, Int)] -> [(Int, Int, Int)]
greyscale = filter (\(x,y,z) -> x == y && y == z)

polychromatic :: [(Int, Int, Int)] -> [(Int, Int, Int)]
polychromatic = filter (\(x,y,z) -> (x > 0 && y > 0) || (y > 0 && z > 0) || (z > 0 && x > 0))

colorsToString :: [(Int, Int, Int)] -> [String]
colorsToString = map (\(x,y,z) -> "r: " ++ show x ++ " g: " ++ show y ++ " b: " ++ show z)

quickSort :: [Integer] -> [Integer]
quickSort [] = []
quickSort (x:xs) = quickSort (filter (<x) xs) ++ [x] ++ quickSort (filter (>=x) xs)

sumLists :: Num a => [a] -> [a] -> [a]
sumLists xs ys = zipWith (+) xs ys

upper :: String -> String
upper xs = map toUpper xs

embrace :: [String] -> [String]
embrace xs = map ("[" ++) (map (++ "]") xs)

sql :: (Ord a, Num a) => [a] -> a -> [a]
sql xs lt = map (^2) (filter (<lt) xs)

-- map even
-- map (a -> b) -> [a] -> [b]
-- even Num a => a -> Bool
-- Num a => [a] -> [Bool]

-- map head . snd
-- map (f -> g) -> [f] -> [g]
-- head [e] -> e
-- . (b - > c) -> (a -> b) -> (a -> b -> c)
-- snd (h, i) -> i
-- map head [[e]] -> [e]
-- h = [[e]]
-- map head . snd (h, [[i]]) -> [i]

-- filter ((4 >) . last)
-- filter (a -> Bool) -> [a] -> [a]
-- last [b] -> b
-- (4 >) Ord c => c -> Bool
-- . (e -> f) -> (d -> e) -> (d -> -> e -> f)
-- ((4 >) . last) Ord b => [b] -> Bool
-- filter ((4 >) . last) (Ord b, Num b) => [[b]] -> [[b]]

-- const const
-- const a -> b -> a
-- const const a -> b -> c -> b

countStudentsByPoints :: Integer -> [(String, Integer)] -> Int
countStudentsByPoints n xs = length (filter (==n) (map snd xs))

studentNamesByPoints :: Integer -> [(String, Integer)] -> [String]
studentNamesByPoints n xs = getNames (filter ((==n) . snd) xs)

studentsStartingWith :: Char -> [(String, Integer)] -> [(String, Integer)]
studentsStartingWith c = filter ((==c) . head . fst)

failing :: [(Int, Char)] -> [Int]
failing = map fst . (filter ((=='F') . snd))

embraceWith :: Char -> Char -> [String] -> [String]
embraceWith l r = map ((l :) . (++[r]))

divisibleBy7 :: [Integer] -> [Integer]
divisibleBy7 = filter ((==0) . (flip mod 7))

letterCaesar :: String -> String
letterCaesar = map (chr . (+3) . ord) . filter isLetter

zp :: (Integral a, Num b) => [a] -> [b] -> [b]
zp = zipWith (flip (^))

negp :: (a -> Bool) -> a -> Bool
negp = (.) not

l2c :: Char -> Int
l2c = flip (-) (ord 'a') . ord

c2l :: Int -> Char
c2l = chr . (+) (ord 'A')

lowAlphaOnly :: String -> String
lowAlphaOnly = filter (((&&) . isLower <*> isAscii))

-- isLower Char -> Bool
-- isAscii Char -> Bool
-- (&&) Bool -> Bool -> Bool
-- filter (a -> Bool) -> [a] -> [a]
-- <*> (a -> b -> c) -> (a -> b) -> a -> c
-- (&&) isLower Char -> Bool -> Bool
-- (&&) isLower <*> - (Char -> Bool) -> Char -> Bool
-- ((&&) isLower <*> isAscii) -> Char -> Bool
-- filter (((&&) isLower <*> isAscii)) -> [Char] -> [Char]

letterVigenere :: String -> String -> String
letterVigenere xs ks = zipWith (\x y -> c2l ((l2c x + l2c y) `mod` 26)) (lowAlphaOnly xs) (lowAlphaOnly ks)

-- l2c Char -> Int
-- c2l Int -> Char
-- (+) -> Num a => a -> a -> a
-- (mod) Integral a => a -> a -> a
-- lowAlphaOnly String -> String
-- zipWith (a -> b -> c) -> [a] -> [b] -> [c]
-- <*> (a -> b -> c) -> (a -> b) -> a -> c
-- (.) (b -> c) -> (a -> b) -> a -> c

-- \x -> (f . g) x = f . g
-- \x -> f . g x = 