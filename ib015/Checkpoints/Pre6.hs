awayMaybe :: Maybe Int -> Int
awayMaybe Nothing = 0
awayMaybe (Just a) = a

data TerTree a = Empty | Node a (TerTree a) (TerTree a) (TerTree a)

leftestTree :: TerTree a -> Int
leftestTree Empty = 0
leftestTree (Node _ l _ _) = 1 + leftestTree l