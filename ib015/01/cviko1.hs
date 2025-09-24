isSucc :: Integer -> Integer -> Bool
isSucc x y = (x + 1) == y

firstNoneZero :: Integer -> Integer -> Integer
firstNoneZero x y = 
    if x /= 0
    then x
    else y

isWeekendDay :: String -> Bool
isWeekendDay "Saturday" = True
isWeekendDay "Sunday" = True
isWeekendDay _ = False

circleArea :: Double -> Double
circleArea r = pi * r ^ 2

snowmanVolume :: Double -> Double -> Double -> Double
snowmanVolume x y z = volume x + volume y + volume z
    where volume r = 4 / 3 * pi * r ^ 3


isRightTriangle :: Double -> Double -> Double -> Bool
isRightTriangle a b c = isCorrect a b c || isCorrect b c a || isCorrect c a b
    where isCorrect a b c = (a * a + b * b) == c * c

max3_v1 :: Integer -> Integer -> Integer -> Integer
max3_v1 a b c = max (max a b) c

max3_v2 :: Integer -> Integer -> Integer -> Integer
max3_v2 a b c = if a > b then if a > c then a else c else if b > c then b else c

mid_1 :: Integer -> Integer -> Integer -> Integer
mid_1 a b c = min_3 (max a b) (max b c) (max a c)
    where min_3 a b c = min (min a b) c

tell :: Integer -> String
tell 1 = "one"
tell 2 = "two"
tell x = if mod x 2 == 0 then "(even)" else "(odd)"

logicalNot :: Bool -> Bool
logicalNot True = False
logicalNot _ = True

logicalAnd :: Bool -> Bool -> Bool
logicalAnd True True = True
logicalAnd _ _ = False

logicalOr :: Bool -> Bool -> Bool
logicalOr False False = False
logicalOr _ _ = True

isSmallVowel :: Char -> Bool
isSmallVowel c = if c >= 'a' && c <= 'z' then True else False

solveQuad :: Double -> Double -> Double -> (Double, Double)
solveQuad 0 b c = (- c / b, - c / b)
solveQuad a b c = (((-b - d ^ 1 / 2) / 2 * a), ((-1 * b + d ^ 1 / 2) / 2 * a))
        where d = b ^ 2 - 4 * a * c

parallelToAxis :: (Integer, Integer) -> (Integer, Integer) -> Bool
parallelToAxis (x1, y1) (x2, y2) = (x1 == x2) || (y1 == y2)

isDivisibleBy :: Integral a => a -> a -> Bool
isDivisibleBy a b = mod a b == 0