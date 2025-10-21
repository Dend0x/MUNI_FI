g :: Float -> Integer -> Double
g _ _ = 5

f :: [Float] -> [Double] -> Integer -> [Double]
f [] y z = y
f (x:xs) y z = [g x z]

popCount :: Integer -> Integer
popCount 0 = 0
popCount 1 = 1
popCount x = mod x 2 + popCount (div x 2)

localMinima :: Ord a => [a] -> [a]
localMinima [] = []
localMinima ([_]) = []
localMinima [_,_] = []
localMinima (x:y:z:xs) = if x > y && z > y then y : localMinima (y:z:xs) else localMinima (y:z:xs)

fullAdder :: Bool -> Bool -> Bool -> (Bool, Bool)
fullAdder False a b = (a /= b, a && b)
fullAdder True a b = (a == b, a || b)

binaryAdd :: [Bool] -> [Bool] -> ([Bool], Bool)
binaryAdd xs ys = let (a, c) = addWithCarry (reverse xs) (reverse ys) False in (reverse a, c)
    where addWithCarry :: [Bool] -> [Bool] -> Bool -> ([Bool], Bool)
          addWithCarry [] _ z = ([], z)
          addWithCarry (x:xs) (y:ys) z = let (a, b) = fullAdder x y z
                                             (c, d) = addWithCarry xs ys b
                                         in (a:c, d)

_filter :: (a -> Bool) -> [a] -> [a]
_filter _ [] = []
_filter f (x:xs) = if f x then x : _filter f xs else _filter f xs

_sum :: [Integer] -> Integer
_sum [] = 0
_sum (x:xs) = x + _sum xs

_map :: (a -> b) -> [a] -> [b]
_map _ [] = []
_map f (x:xs) = f x : _map f xs

haveMajority :: [String] -> [(String, Integer)] -> Bool
haveMajority xs ys = _sum (_map snd (_filter (\(a,_) -> elem a xs) ys)) > (div (_sum (_map snd ys)) 2)