import Data.Char (isUpper)

nth :: [a] -> Int -> a
nth n = (head . (flip drop n))

firstUppercase :: String -> Char
firstUppercase str = if length xs == 0 then '-' else head xs
                where xs = dropWhile (not . isUpper) str

everyNth :: [a] -> Int -> [a]
everyNth xs n = map snd (filter ((==0) . (flip mod n) . fst) (zip [0..] xs))

binmap :: (a -> a -> b) -> [a] -> [b]
binmap _ [] = []
binmap f (x:xs) = map (\x -> f (fst x) (snd x)) (zip (x:xs) xs)

-- Eq a => a -> a -> a -> Bool = 3
-- (a -> Bool) -> ([a] -> Int) = 2
-- [Int -> Int -> Int] = 0
-- Int -> Integer -> String -> String = 3
-- (Int -> Integer) -> String -> String = 2
-- Int -> Integer -> (String -> String) = 3
-- Int -> Integer -> [String -> String] = 2
-- (a -> b -> c) -> b -> a -> c = 3-4

-- cm _ [] = []
-- cm x (y : z) = x y ++ cm x z
-- (a -> [a]) -> [a] -> [a]
-- mm [] = (maxBound, minBound)
-- (x:xs) = let (a, b) = mm xs in (min a x, max b x)
-- (maxBound a, Ord a) => [a] -> (a, a)
-- c x y = \z -> x (y z)
-- (b -> c) -> (a -> b) -> a -> c

-- \x y -> map y x
-- [a] -> (a -> b) -> [b]
-- \x -> flip replicate
-- replicate :: c -> Int -> a -> [a]
-- flip replicate :: a -> Int -> [a]
-- a -> Int -> [a]
-- \x y -> take y [fst x, snd x]
-- (a, a) -> Int -> [a]
-- \x y -> map x . filter y
-- (a -> b) -> (a -> Bool) -> [b] -> [c]
-- \x y -> fromIntegral x `div` y
-- fromIntegral :: (Integral a, Num b) => a -> b
-- div :: (Integral a) => a -> a -> a
-- (Integral a, Num b) => a -> a -> b

-- flip map
-- flip :: (a -> b -> c) -> b -> a -> c
-- map :: (a -> b) -> [a] -> [b]
-- [a] -> (a -> b) -> [b]
-- 2
-- (not . null)
-- not :: Bool -> Bool
-- null :: [a] -> Bool
-- [a] -> Bool
-- 1
-- (\f p -> filter p . map f)
-- filter :: (a -> Bool) -> [a] -> [a]
-- map :: (a -> b) -> [a] -> [b]
-- (a -> b) -> (b -> Bool) -> [b] -> [b]
-- 3
-- (\x -> x 1 || x 2)
-- Num a => (a -> Bool) -> Bool
-- 1
-- flip (not .)
-- flip :: (a -> b -> c) -> b -> a -> c
-- (.) :: (b -> c) -> (a -> b) -> a -> c
-- not :: Bool -> Bool
-- (not .) :: (a -> Bool) -> a -> Bool
-- flip (not .) :: a -> (a -> Bool) -> Bool
-- 2
-- zipWith id
-- id :: a -> a
-- zipWith :: (a -> b -> c) -> [a] -> [b] -> [c]

f :: (Num a, Ord a) => a -> String -> Bool -> String
f x y True = if x > 42 then y else []
f _ (_ : s) False = s
f _ _ _ = "IB015"

-- last [42, 3.14, 16]
-- 16
-- zipWith mod [3, 5, 7, 4] [4, 2, 3]
-- [3, 1, 1]
-- (concat . map (replicate 4)) ['a', 'b', 'c']
-- "aaaabbbbcccc"
-- head (filter ((> 3) . length) ["hi!", "ahoj", "hello"])
-- "ahoj"
-- cycle [3, 2, 4] !! 10
-- 2
-- (head . drop 3 . iterate (^ 2)) 2
-- 256

data PadMode = PadLeft
                | PadRight
                | PadCenter
                deriving Show

pad :: Int -> Char -> PadMode -> String -> String
pad n ch PadLeft xs = if n <= length xs then xs else replicate (n - length xs) ch ++ xs
pad n ch PadRight xs = if n <= length xs then xs else xs ++ replicate (n - length xs) ch
pad n ch PadCenter xs = if n <= length xs then xs else replicate (n - length xs - div (n - length xs) 2) ch ++ xs ++ replicate (div (n - length xs) 2) ch

take' :: Int -> [a] -> [a]
take' _ [] = []
take' 0 _ = []
take' n (x:xs) = x : take' (n - 1) xs

breaks :: (a -> Bool) -> [a] -> [[a]]
breaks f [] = []
breaks f xs = fst (break f xs) : breaks f (snd (break f xs))