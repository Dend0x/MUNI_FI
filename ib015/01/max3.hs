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