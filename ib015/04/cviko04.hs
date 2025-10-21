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