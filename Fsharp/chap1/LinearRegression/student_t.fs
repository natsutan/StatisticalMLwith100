module student_t

open MathNet.Numerics.Distributions
open FSharp.Charting

let plot_student_t(path) =
    
    let mutable chart_list = []
    let chart = Chart.Line( [for x in -10.0 .. 0.1 .. 10.0 -> x, Normal.PDF(0.0, 1.0, x) ], Color=System.Drawing.Color.Red, Name="Norm")
              |> Chart.WithLegend()

    chart_list <- chart :: chart_list
        
    for v in 1 .. 10 do
        let chart = Chart.Line ( [for x in -10.0 .. 0.1 .. 10.0 -> x, StudentT.PDF(0.0, 1.0, double(v), x)] , Name=string(v))
                    |> Chart.WithLegend()
        chart_list <- chart :: chart_list


    let chart_comb = List.rev chart_list |> Chart.Combine 

    let output_file = path + @"t.png"
    Chart.Save output_file chart_comb

    None
