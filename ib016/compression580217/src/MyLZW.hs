module MyLZW (Codeword, Encoding, compress, decompress) where

type Codeword = Int
type Encoding = [Codeword]

compress :: String -> Encoding

decompress :: Encoding -> String
