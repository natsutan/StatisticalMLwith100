module chisquares
open MathNet.Numerics.Distributions
open FSharp.Charting


let plot_chi2(path) =
    
    let mutable chart_list = []
        
    for k in 1 .. 11 do
        let chart = Chart.Line [for x in 0.1 .. 0.01 .. 20.0 -> x, ChiSquared.PDF(float(k), x) ]
        chart_list <- chart :: chart_list


    let chart_comb = Chart.Combine chart_list

    let output_file = path + @"chi2.png"
    Chart.Save output_file chart_comb

    None
