module MyLZW (Codeword, Encoding, compress, decompress) where

import qualified Data.Map as Map
import qualified Control.Monad.State as State

type Codeword = Int
type Encoding = [Codeword]
type CompressionDict = Map.Map String Codeword
type DecompressionDict = Map.Map Codeword String

{-
    This helped a lot
    https://www.youtube.com/watch?v=oKum39FSn8U&t=300s

    Algorithm works by creating a map of letters of the alphabet + 
    later found substrings of the input

    Every letter (or sequence of letters) found in input has its number (encodeNumber), 
    which will be representing that substring in the output, to make it shorter

    The State monad holds current dictionary and nextKey, that will be given the next new found string

    During the making of this code I was learning the State Monad from scratch, therefore I
    am using a lot of comments to make it clear to me
-}


-- | CompressionState contains current dictionary and
-- | key, that should be used next
data CompressionState = CompressionState { dictionary :: CompressionDict,
                                           nextKey :: Codeword }

data DecompressionState = DecompressionState { dictionaryDec :: DecompressionDict,
                                               nextKeyDec :: Codeword }

-- map (:[]) converts Char to String, list generator wont work on Strings
compressionDictInit :: CompressionDict
compressionDictInit = Map.fromDistinctAscList $ ("#", 0) : zip (map (:[]) ['A'..'Z']) [1..26]

compressionStateInit :: CompressionState
compressionStateInit = CompressionState compressionDictInit 27

{-

    case 1 - No more letters to work with
        The function returns a State, which is a Monad and because of that I had to pack the value
        of encodeNumber. I preffer pure, as it is less confusing than using return


    case 2
        Getting the current state and newly created substring

        If the created substring is already in the Map, from the algorithm the function
        is just called again with subString as subString + letter 

        If newSubString is not in the Map, then we have to emit the and save the last used subString
        before the new one, that number is represented as encodeNumber

        then we have to update the State that is currently set, that means:
            Adding newSubsString to the dictionary <=> creating new one
            increment encodeNumber, so identifiers are unique
        
        Setting the new State with updated dictionary and nextKey incremented
        State.put removes the previous state and overwrites it with a new one, 
        or simply updates it
-}
compressionStep :: String -> String -> State.State CompressionState Encoding
compressionStep subString [] = do
    currentState <- State.get
    let currentDictionary = dictionary currentState
    let Just encodeNumber = Map.lookup subString currentDictionary
    pure [encodeNumber]
compressionStep subString (letter:left) = do
    currentState <- State.get
    let currentDictionary = dictionary currentState
    let newSubString = subString ++ [letter]

    case Map.lookup newSubString currentDictionary of
        Just _ -> compressionStep newSubString left
        Nothing -> do
            let Just encodeNumber = Map.lookup subString currentDictionary
            let newDictionary = Map.insert newSubString (nextKey currentState) currentDictionary
            let newState = CompressionState newDictionary (nextKey currentState + 1)
            State.put newState
            restOfString <- compressionStep [letter] left
            pure (encodeNumber : restOfString)


-- | We simply call a recursive function with "" as the list of current substring
-- | and toEncode as list of what is left to be done
compressionState :: String -> State.State CompressionState Encoding
compressionState toEncode = compressionStep "" toEncode

-- | .evalState - Evaluate a state computation with the given initial state and return
-- | the final value, discarding the final state. - Hoogle
-- | When State is "turned on", it uses CompressionState and returns Encoding
-- | The initial state of State is compressionStateInit
compress :: String -> Encoding
compress toEncode = State.evalState (compressionState toEncode) compressionStateInit

decompressionDictInit :: DecompressionDict
decompressionDictInit = Map.fromDistinctAscList $ (0, "#") : zip [1..26] (map (:[]) ['A'..'Z'])

decompressionStateInit :: DecompressionState
decompressionStateInit = DecompressionState decompressionDictInit 27

decompressionState :: Encoding -> State.State DecompressionState String
decompressionState [] = pure ""
decompressionState (encodeNumber:xs) = do
    state <- State.get
    let dict = dictionaryDec state
    let Just encodeString = Map.lookup encodeNumber dict
    xsStrings <- decompressionStep encodeString xs
    pure (encodeString ++ xsStrings)

{-

    Almost the same
    Creating and editing state to update decompresser

    For creation of new strings compresser has to use last used string and new input

-}

decompressionStep :: String -> Encoding -> State.State DecompressionState String
decompressionStep _ [] = pure ""
decompressionStep last (encodeNumber:xs) = do
    state <- State.get
    let dict = dictionaryDec state
    let input = case Map.lookup encodeNumber dict of
                    Just string -> string
                    -- For the case newly created code was used
                    Nothing -> last ++ [head last]
    -- First char of input is what compresser used to make new input to dict
    let newInput = last ++ [head input]

    let newDict = Map.insert (nextKeyDec state) newInput dict
    let newState = DecompressionState newDict (nextKeyDec state + 1)

    State.put newState

    xsStrings <- decompressionStep input xs
    pure (input ++ xsStrings)

decompress :: Encoding -> String
decompress toDecode = State.evalState (decompressionState toDecode) decompressionStateInit
