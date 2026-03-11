import Data.Map as M

lengthStats :: [[a]] -> String
lengthStats xs = lengthStatsIn xs (empty :: Map Int Int)

lengthStatsIn :: [[a]] -> Map Int Int -> String
lengthStatsIn xs m = let finalMap = Prelude.foldl (\x y -> M.insertWith (+) (length y) 1 x) m xs
                     in unlines $ Prelude.map (\(a, b) -> "delka " ++ show a ++ ": " ++ show b ++ ",") (M.toList finalMap)