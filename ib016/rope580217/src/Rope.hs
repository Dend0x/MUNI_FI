module MyLib (stringToRope, ropeToString, indexRope, updateRope, concatRopes, splitRope, insertIntoRope) where

import Data.Array

type CharArray = Array Int Char

data Rope
    = Leaf CharArray -- ˆ Leaf, contains a single string
    | Concat -- ˆ Inner node, represents a concatenation
        Int -- ˆ Weight
        Rope -- ˆ Left child
        Rope -- ˆ Right child
    deriving (Show)

wikiTestRope :: Rope
wikiTestRope = b
    where
        b = concatRopes c d
        c = concatRopes e f
        d = concatRopes g h
        e = stringToRope "Hello "
        f = stringToRope "my "
        g = concatRopes j k
        h = concatRopes m n
        j = stringToRope "na"
        k = stringToRope "me i"
        m = stringToRope "s"
        n = stringToRope " Simon"

smallTestRope :: Rope
smallTestRope =
    Concat 6
        (Concat 2
            (stringToRope "I ")
            (stringToRope "love"))
        (stringToRope " Haskell!")

test :: Rope
test = Concat 2 (stringToRope "na") (stringToRope "me i")

-- Array has to take range (i, i) of indices used na then the elements
-- an element here is tuple (i, char)

stringToRope :: String -> Rope
stringToRope str = Leaf (array (0, len - 1) $ zip [0..] str)
    where len = length str

-- Found on Hoogle
-- elems :: Array i e -> [e]
-- The list of elements of an array in index order.

ropeToString :: Rope -> String
ropeToString (Leaf arr) = elems arr
ropeToString (Concat _ l r) = ropeToString l ++ ropeToString r

{-
    Checks wether the index is on the left or right
    Only important think is, that the weight must be subtracted
    from idx so it counts only in the right area
-}

indexRope :: Rope -> Int -> Maybe Char
indexRope (Leaf arr) idx
    | idx <= snd (bounds arr) && idx >= 0 = Just (arr ! idx)
    | otherwise              = Nothing
indexRope (Concat weight l r) idx
    | idx < weight = indexRope l idx
    | otherwise    = indexRope r (idx - weight)

{-
    Similar to indexRope, but I have to reconstruct the tree on the way
    (//) :: Ix i => Array i e -> [(i, e)] -> Array i e
    A function from Data.Array that returns array with values changed on indices
    with characters
    Hoogle
-}

updateRope :: Rope -> Int -> Char -> Maybe Rope
updateRope (Leaf arr) idx newChar
    | idx <= snd (bounds arr) && idx >= 0 = Just (Leaf $ arr//[(idx, newChar)])
    | otherwise               = Nothing
updateRope (Concat weight l r) idx newChar
    | idx < weight =
        case lRope of
            Just lr -> Just (Concat weight lr r)
            Nothing -> Nothing
    | otherwise    =
        case rRope of
            Just rr -> Just (Concat weight l rr)
            Nothing -> Nothing
    where lRope = updateRope l idx newChar
          rRope = updateRope r (idx - weight) newChar

{-
    Calculates the right side of the Rope,
    so the weight is correct
-}

rWeight :: Rope -> Int
rWeight (Leaf arr) = snd (bounds arr) + 1
rWeight (Concat weight _ r) = weight + rWeight r

{-
    Connects two ropes, not much more to explain
-}

concatRopes :: Rope -> Rope -> Rope
concatRopes r1 r2 = Concat (rWeight r1) r1 r2

{-
    Sets bounds for index so there is not error
-}

clamp :: Int -> Int -> Int -> Int
clamp x lo hi
  | x < lo = lo
  | x > hi = hi
  | otherwise = x

{-
    A help function, that also tracks the weights of both subtrees
    On the other hand, I have to track both sides, so I have to use
    the rWeight functions, that adds a bit of time complexity
    Still its O(log n)
    The result is but much more usable in real use
-}

splitRopeHelp :: Rope -> Int -> (Rope, Int, Rope, Int)
splitRopeHelp (Leaf arr) idx = (stringToRope $ take i elemsArr, i, stringToRope $ drop i elemsArr, len - i)
    where elemsArr = elems arr
          len = length elemsArr
          i = clamp idx 0 len
splitRopeHelp (Concat weight l r) idx
    | idx == weight = (l, weight, r, rWeight r)
    | idx < weight  =
        let (l1, l1l, r1, r1l) = splitRopeHelp l idx
        in (l1, l1l, Concat r1l r1 r, r1l + rWeight r)
    | otherwise     =
        let (l2, l2l, r2, r2l) = splitRopeHelp r (idx - weight)
        in (Concat weight l l2, weight + l2l, r2, r2l)

--   A wrapper function for splitRopeHelp

splitRope :: Rope -> Int -> (Rope, Rope)
splitRope rope idx = (l, r)
    where (l, _, r, _) = splitRopeHelp rope idx

{-
    Splits the rope into two parts at the index given
    Then connects the inserted string like this:
        L_ROPE ++ string ++ R_ROPE
-}

insertIntoRope :: Rope -> Int -> String -> Rope
insertIntoRope rope idx toInsert = concatRopes (concatRopes l ins) r
    where (l, r) = splitRope rope idx
          ins    = stringToRope toInsert

