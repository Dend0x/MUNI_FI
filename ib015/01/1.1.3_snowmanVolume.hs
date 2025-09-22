snowmanVolume :: Double -> Double -> Double -> Double
snowmanVolume x y z = volume x + volume y + volume z
    where volume r = 4 / 3 * pi * r ^ 3