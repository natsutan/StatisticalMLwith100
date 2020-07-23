module sigmoid
open FSharp.Charting

let sigmoid beta x :float=
    exp(x * beta) / (1.0 + exp(beta * x))

    

let plotSigmoid path =
    let betas = [ 0.0; 0.2; 0.5; 1.2; 2.0; 10.0 ]
    let mutable chart_list = []

    for beta in betas do
        let sigm = sigmoid beta
        let chart = Chart.Line [for x in -10.0 .. 0.1 .. 10.0 -> x, sigm x ]
        chart_list <- chart :: chart_list

    let chart_comb = Chart.Combine chart_list
    let output_file = path + @"sigmoid.png"
    Chart.Save output_file chart_comb

    None
