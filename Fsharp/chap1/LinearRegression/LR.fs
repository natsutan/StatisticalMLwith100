module LR
open FSharp.Charting
open MathNet.Numerics.Distributions


let makeData(N:int) =
    let a = Normal(mean=2.0, stddev=1.0).Sample() 
    let rnd = System.Random()
    let b = rnd.NextDouble()
    
    let xs = Array.init N (fun _ -> lib.randn())
    let ys = Array.map (fun x -> a * x + b + lib.randn()) xs 

    xs, ys

let min_sq(xs : double [], ys :double []) = 
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
    
let plot_data(xs, ys, a, b, path) =
    
    let chart0 = Array.zip xs ys |> Chart.Point
    let chart1 = Chart.Line [for x in -2.0 .. 2.0 -> x, x * a + b]
    let chart_comb = Chart.Combine [chart0; chart1]

    let output_file = path + @"plot.png"
    Chart.Save output_file chart_comb

    None
