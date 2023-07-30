let readLines (filePath: string) = System.IO.File.ReadLines(filePath) |> Seq.toList

let rec delete (element: 'T) (list: 'T list) : 'T list =
    match list with
    | head :: tail -> 
        if head = element then
            delete element tail
        else
            head :: delete element tail
    | [] -> []

let rec mutuals (xs: 'T list) (ys: 'T list) (zs: 'T list): 'T list =
    match xs with
    | head :: tail ->
        if List.contains head ys && List.contains head zs then
            [head] @ mutuals xs (delete head ys) (delete head zs)
        else mutuals tail ys zs
    | _ -> []

let values = 
    (seq { 'a'..'z' } |> Seq.mapi (fun idx x -> x, idx+1) |> Seq.toList) @ 
    (seq { 'A'..'Z' } |> Seq.mapi (fun idx x -> x, idx+27) |> Seq.toList) |> Map.ofList

let rec badges (groups: string list list) =
    match groups with
    | [first; second; third] :: tail -> 
        let badge = mutuals (Seq.toList first) (Seq.toList second) (Seq.toList third) |> List.head
        [badge] @ badges tail
    | [] -> []
    | _ -> []

let splitToThree (list: 'T list) : 'T list list =
    let folder (acc: 'a list list) (elem: 'a) =
        match elem with
        | _ when List.length (List.head acc) = 3 -> [elem] :: acc // Start a new subarray when predicate is true
        | _ -> (List.head acc @ [elem]) :: List.tail acc // Append the element to the current subarray

    List.fold folder [[]] list 
    |> List.rev

readLines "input.txt"
|> splitToThree
|> badges
|> List.map (fun x -> values[x])
|> List.sum
|> printfn "%i"

