// Learn more about F# at http://fsharp.org
// See the 'F# Tutorial' project for more help.
open MathNet.Numerics.Distributions
open FSharp.Charting

let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\chap1\LinearRegression\fig\"
let N = 100

//Pythonのrandn
let randn():double = 
    Normal(mean=0.0, stddev=1.0).Sample()

let makeData(N:int) =
    let a = Normal(mean=2.0, stddev=1.0).Sample() 
    let rnd = System.Random()
    let b = rnd.NextDouble()
    
    let xs = Array.init N (fun _ -> randn())
    let ys = Array.map (fun x -> a * x + b + randn()) xs 

    xs, ys

let min_sq(xs, ys) = 
    let x_bar = Array.average xs
    let y_bar = Array.average ys
    // (x-x_bar), (y-y_bar)
    let x_x_bar = Array.map (fun x -> x - x_bar) xs
    let y_y_bar = Array.map (fun y -> y - y_bar) ys

    //内積
    let dot_xy = Array.map2 (fun x y -> x * y) x_x_bar y_y_bar |> Array.sum
    let norm = Array.map (fun x -> x * x) x_x_bar |> Array.sum

    let a = dot_xy / norm
    let b = y_bar - a * x_bar

    a, b
    
let plot_data(xs, ys, a, b) =
    
    let chart0 = Array.zip xs ys |> Chart.Point
    let chart1 = Chart.Line [for x in -2.0 .. 2.0 -> x, x * a + b]
    let chart_comb = Chart.Combine [chart0; chart1]

    let output_file = path + @"plot.png"
    Chart.Save output_file chart_comb

    None

[<EntryPoint>]
let main argv = 

    let xs, ys = makeData N
    let a, b = min_sq(xs, ys)
    plot_data(xs, ys, a, b) |> ignore
    printf "a = %A, b = %A" a b

    0 // return an integer exit code
