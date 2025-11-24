g :: Double -> Bool -> Float
g _ _ = 2

f :: Maybe Double -> Bool -> Float -> Maybe [Float]
f Nothing _ _ = Nothing
f (Just x) y z = Just [(g x y), z]

data Filesystem = Folder String [Filesystem]
                | File String
                  deriving (Show)

removeStartingByA :: Filesystem -> Filesystem
removeStartingByA (File name) = (File name)
removeStartingByA (Folder name []) = (Folder name [])
removeStartingByA (Folder name ((Folder foldername others):folders)) = if head foldername == 'a' then let (Folder _ names) = removeStartingByA (Folder foldername folders) in (Folder name names) else let (Folder _ names) = removeStartingByA (Folder foldername folders) in (Folder name (removeStartingByA (Folder foldername others):names))
removeStartingByA (Folder name ((File filename):folders)) = if head filename == 'a' then let (Folder _ names) = removeStartingByA (Folder name folders) in (Folder name names) else let (Folder _ names) = removeStartingByA (Folder name folders) in (Folder name (File filename:names))

data BinTree a = Empty
               | Node a (BinTree a) (BinTree a)
               deriving (Show, Eq)

data TreeDirection = LeftChild
                   | RightChild
                   deriving (Show, Eq)

t1 = Node 1
  (Node 4
    (Node 5 Empty Empty)
    (Node 6 Empty Empty))
  (Node 5
    (Node 8 Empty Empty)
    (Node 1 Empty Empty))

t2 = Node "Elwing"
  (Node "Dior"
    (Node "Beren"
      (Node "Barahir" Empty Empty)
      (Node "Emeldir" Empty Empty))
    (Node "Luthien"
      (Node "Elwe" Empty Empty)
      (Node "Melian" Empty Empty)))
  (Node "Nimloth" Empty Empty)

right :: (Eq a) => Maybe [TreeDirection] -> a -> BinTree a -> Maybe [TreeDirection]
right (Just d) v r = Just (RightChild : d)
right Nothing _ _ = Nothing

left :: (Eq a) => Maybe [TreeDirection] -> a -> BinTree a -> Maybe [TreeDirection]
left (Just d) v r = Just (LeftChild : d)
left Nothing v r = right (treeFind v r) v r

treeFind :: (Eq a) => a -> BinTree a -> Maybe [TreeDirection]
treeFind _ Empty = Nothing
treeFind v (Node fv l r) = if v == fv then Just [] else left (treeFind v l) v r

data Direction = North | East | South | West deriving (Show, Eq)
data State = State Int Int Direction deriving (Show, Eq)
data Instruction = TurnLeft | TurnRight | Forward Int deriving (Show, Eq)

leftt :: Direction -> Direction
leftt North = West
leftt East = North
leftt South = East
leftt West = South

rightt :: Direction -> Direction
rightt North = East
rightt East = South
rightt South = West
rightt West = North

move :: Int -> State -> State
move l (State x y North) = (State x (y + l) North)
move l (State x y East) = (State (x + l) y East)
move l (State x y South) = (State x (y - l) South)
move l (State x y West) = (State (x - l) y West)

executeInstructions :: [Instruction] -> State -> State
executeInstructions [] x = x
executeInstructions (TurnLeft:xs) (State x y dir) = executeInstructions xs (State x y (leftt dir))
executeInstructions (TurnRight:xs) (State x y dir) = executeInstructions xs (State x y (rightt dir))
executeInstructions ((Forward l):xs) state = executeInstructions xs (move l state)