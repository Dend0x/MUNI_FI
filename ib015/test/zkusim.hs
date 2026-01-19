data LeafTree a = LNode (LeafTree a) (LeafTree a) | LLeaf a
    deriving Show

strom = (LNode (LNode (LLeaf 5) (LLeaf 9)) (LLeaf 12))

mapLeaf :: (a -> b) -> LeafTree a -> LeafTree b
mapLeaf f (LLeaf a) = (LLeaf (f a))
mapLeaf f (LNode l r) = (LNode (mapLeaf f l) (mapLeaf f r))

foldLeafTree :: (b -> b -> b) -> (a -> b) -> LeafTree a -> b
foldLeafTree nf lf (LLeaf a) = lf a
foldLeafTree nf lf (LNode l r) = nf (foldLeafTree nf lf l) (foldLeafTree nf lf r)

countLeaves :: LeafTree a -> Int
countLeaves = foldLeafTree (+) (\_ -> 1)

h :: [Int] -> [Int]
h xs = map (\x -> maximum (take x xs) - xs !! (x - 1)) [1..length xs]

help' :: Int -> [Int] -> [Int]
help' _ [] = []
help' n (x:xs) = max x n - x : help' (max x n) xs

h' :: [Int] -> [Int]
h' xs = help' 0 xs