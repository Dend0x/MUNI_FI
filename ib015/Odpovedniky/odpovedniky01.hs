sign :: Integer -> Integer
sign 0 = 0
sign x = if x > 0 then 1 else -1

fullAdder :: Bool -> Bool -> Bool -> (Bool, Bool)
fullAdder False False False = (False, False)
fullAdder True True True = (True, True)
fullAdder x y z = if not ((x && y) || (x && z) || (y && z)) then (True, False) else (False, True)

classifyIP :: (Int, Int, Int, Int) -> String
classifyIP (147, 251, 49, 10) = "IS"
classifyIP (172, x, _, _) = if x >= 16 && x <= 31 then "FI" else "Other"
classifyIP (147, 251, 58, _) = "FI"
classifyIP (147, 251, x, _) = if x >= 42 && x <= 53 then "FI" else "MUNI"
classifyIP (_, _, _, _) = "Other"

is3DCloser :: (Integer, Integer, Integer) -> (Integer, Integer, Integer) -> (Integer, Integer, Integer) -> Bool
is3DCloser (x1, y1, z1) (x2, y2, z2) (x3, y3, z3) = distance x1 y1 z1 x2 y2 z2 < distance x1 y1 z1 x3 y3 z3
    where distance x1 y1 z1 x2 y2 z2 = (x1 - x2) ^ 2 + (y1 - y2) ^ 2 + (z1 - z2) ^ 2

pointsCount :: (Integer, Integer, Integer) -> Integer
pointsCount (x, y, z) = 5 * x + 2 * y + 3 * z

moreThan4t :: Integer -> Integer
moreThan4t x = if x >= 4 then 1 else 0

lessThanSeven :: Integer -> Integer -> Integer
lessThanSeven x y = if x - 7 <= y then 1 else 0

matchPoints :: (Integer, Integer, Integer) -> (Integer, Integer, Integer) -> (Integer, Integer)
matchPoints (t1, c1, d1) (t2, c2, d2) =
    if pointsCount (t1, c1, d1) == pointsCount (t2, c2, d2)
        then (2 + moreThan4t t1, 2 + moreThan4t t2)
        else if pointsCount (t1, c1, d1) > pointsCount (t2, c2, d2)
            then (4 + moreThan4t t1, moreThan4t t2 + lessThanSeven (pointsCount (t1, c1, d1)) (pointsCount (t2, c2, d2)))
            else (moreThan4t t1 + lessThanSeven (pointsCount (t2, c2, d2)) (pointsCount (t1, c1, d1)), 4 + moreThan4t t2)