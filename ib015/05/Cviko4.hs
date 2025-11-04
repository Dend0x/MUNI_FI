data Day = Mon | Tue | Wed | Thu | Fri | Sat | Sun
    deriving (Show, Eq, Ord)

weekend :: Day -> Bool
weekend Sat = True
weekend Sun = True
weekend _ = False

data Object = Cube Double Double Double -- a, b, c
            | Cylinder Double Double -- r, v

volume :: Object -> Double
volume (Cube a b c) = a * b * c
volume (Cylinder r v) = pi * (r ^ 2) * v

surface :: Object -> Double
surface (Cube a b c) = 2 * (a * b + a * c + b * c)
surface (Cylinder r v) = 2 * pi * (r ^ 2) + v * 2 * pi * r

data Contained a = NoValue | Single a | Pair a a
data Compare a = SameContainer
                | SameValue (Contained a)
                | DifferentContainer

cmpContained :: Eq a => Contained a
                    -> Maybe (Contained a)
                    -> Compare a
cmpContained NoValue (Just NoValue) =
    SameValue NoValue
cmpContained (Single x1) (Just (Single x2)) =
    if x1 == x2
        then SameValue (Single x1)
        else SameContainer
cmpContained (Pair x1 y1) (Just (Pair x2 y2)) =
    if x1 == x2 && y1 == y2
        then SameValue (Pair x1 y1)
        else SameContainer
cmpContained _ _ = DifferentContainer

safeDiv :: Integral a => a -> a -> Maybe a
safeDiv a b = if b == 0 then Nothing else Just (div a b)

valOrDef :: Maybe a -> a -> a
valOrDef Nothing x = x
valOrDef (Just a) _ = a