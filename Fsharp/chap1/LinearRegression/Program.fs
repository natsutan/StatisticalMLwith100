module Program

let path = @"C:\home\myproj\StatisticalMLwith100\Fsharp\chap1\LinearRegression\fig\"
let N = 100

let LRrun = false
let NErun = false
let C2run = false

[<EntryPoint>]
let main argv = 
    // 1.1 線形回帰
    if LRrun then
        let xs, ys = LR.makeData N
        let a, b = LR.min_sq(xs, ys)
        LR.plot_data(xs, ys, a, b, path) |> ignore
        printf "a = %A, b = %A\n" a b

    if NErun then
        let X, y = NormalEquation.makedata N
        let beta_hat = NormalEquation.lsm(X, y)

        printf "beta = %A\n" beta_hat

    if C2run then
        chisquares.plot_chi2(path) |> ignore
        printf "chi2"

    student_t.plot_student_t(path)

    0 // return an integer exit code


