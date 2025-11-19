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
