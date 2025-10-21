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
successfulRecords xs = filter (\x -> snd x >= 8) xs

successfulNames :: [(String, Integer)] -> [String]
successfulNames xs = (getNames . successfulRecords) xs

successfulStrings :: [(String, Integer)] -> [String]
successfulStrings xs = map (\x -> "jmeno: " ++ fst x ++ " " ++ show (snd x)) (successfulRecords xs)

toUpperStr :: String -> String
toUpperStr xs = map toUpper xs

isVowel :: Char -> Bool
isVowel 'A' = True
isVowel 'E' = True
isVowel 'I' = True
isVowel 'O' = True
isVowel 'U' = True
isVowel 'Y' = True
isVowel _ = False

assignPrizes :: [String] -> [Integer] -> [(String, Integer)]
assignPrizes xs ys = zip xs ys

prizeTexts :: [String] -> [Integer] -> [String]
prizeTexts xs ys = map display (assignPrizes xs ys)
    where display x = fst x ++ ": " ++ show (snd x) ++ " Kc"

-- map (\(t,x,y) -> if t then x else y) (zip3 [True, False, False, True, False] [1, 2, 3, 4] [16, 42, 7, 1, 666])
-- zipWith3 (\x y z -> max (max x y) z) [7, 4, 11, 2] [5, 7, 1] [16, 5, 0, 1]

neighbors :: [a] -> [(a, a)]
neighbors xs = zip xs (tail xs)

isTrue :: [Bool] -> Bool
isTrue [] = False
isTrue [x] = x
isTrue (True:x) = True
isTrue xs = isTrue (tail xs)

same :: Eq a => [a] -> Bool
same xs = isTrue (zipWith (\x y -> x == y) xs (tail xs))

-- Integral a => [a] -> [Bool]
-- Znova (e, [[x]]) -> [x]
-- Num a, Ord a => [[a]] -> [[a]]
-- a -> b -> c -> a

countStudentsByPoints :: Integer -> [(String, Integer)] -> Int
