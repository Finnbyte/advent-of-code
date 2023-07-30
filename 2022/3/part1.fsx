let readLines (filePath: string) = System.IO.File.ReadLines(filePath) |> Seq.toList

let rec delete (element: 'T) (list: 'T list) : 'T list =
    match list with
    | head :: tail -> 
        if head = element then
            delete element tail
        else
            head :: delete element tail
    | [] -> []

let rec mutuals (list1: 'T list) (list2: 'T list) : 'T list =
    match list1 with
    | head :: tail ->
        if List.contains head list2 then
            [head] @ mutuals tail (delete head list2)
        else
            mutuals tail list2
    | [] -> []

let splitCompartments (rucksack: string) =
    (rucksack.Length / 2, Seq.toList rucksack) ||> List.splitAt

let values = 
    (seq { 'a'..'z' } |> Seq.mapi (fun idx x -> x, idx+1) |> Seq.toList) @ 
    (seq { 'A'..'Z' } |> Seq.mapi (fun idx x -> x, idx+27) |> Seq.toList) |> Map.ofList

let priorities = 
    readLines "input.txt"
    |> List.map (fun s -> 
    let (fst, snd) = splitCompartments s
    printfn "%A %A" fst snd
    List.head (mutuals fst snd)) |> List.map (fun x -> values[x])

priorities
|> List.sum
|> printfn "%i"
